import mgp
import json
import importlib

import utils.github as github
import utils.twitter as twitter
import utils.orbit as orbit
import utils.activity as activity


def json_print(data):
    print(json.dumps(data, indent=4, sort_keys=True))


def dumps_utf8(obj):
    return json.dumps(obj).encode("utf-8")


class JsonDataAccessor(object):
    def __init__(self, data):
        self._data = data

    def take_n(self, *args):
        if not isinstance(self._data, dict):
            return None
        data = self._data
        for arg in args:
            if arg not in data:
                return None
            data = data[arg]
        return data


def take_type_from_array(array, item_type):
    for item in array:
        if "type" not in item:
            continue
        if item["type"] == item_type:
            return item


def create_record(query):
    return mgp.Record(query=query, parameters={})


@mgp.transformation
def kafka2graph_transform(
    messages: mgp.Messages,
) -> mgp.Record(query=str, parameters=mgp.Nullable[mgp.Map]):
    importlib.reload(github)
    importlib.reload(twitter)
    importlib.reload(orbit)
    importlib.reload(activity)
    queries = []
    for i in range(messages.total_messages()):
        try:
            message_str = messages.message_at(i).payload().decode("utf-8")
            payload = json.loads(message_str)
            accessor = JsonDataAccessor(payload)

            # HISTORIC EVENT
            member_slug = accessor.take_n("member_slug")
            member_github = accessor.take_n("member_github")
            member_twitter = accessor.take_n("member_twitter")
            if (
                member_slug is not None
                or member_github is not None
                or member_twitter is not None
            ):
                print(
                    "TODO(gitbuda): Implement processing of historic events if needed."
                )

            # ORBIT EVENT
            # For some reason the payload is wrapped twice.
            event_payload = accessor.take_n("event_payload")
            if event_payload is not None:  # Event.
                accessor = JsonDataAccessor(event_payload)
                included = accessor.take_n("included")
                activity_id = accessor.take_n("data", "id")
                activity_url = accessor.take_n("data", "attributes", "orbit_url")
                activity_time = accessor.take_n("data", "attributes", "occurred_at")
                activity_type = None
                activity_data = take_type_from_array(included, "activity_type")
                if activity_data:
                    activity_accessor = JsonDataAccessor(activity_data)
                    activity_type = activity_accessor.take_n("attributes", "key")

                member_account = None
                github_account = None
                twitter_account = None

                member_data = take_type_from_array(included, "member")
                if member_data:
                    member_accessor = JsonDataAccessor(member_data)
                    print(dumps_utf8(member_accessor._data))
                    name = member_accessor.take_n("attributes", "name")
                    love = member_accessor.take_n("attributes", "love")
                    slug = member_accessor.take_n("attributes", "slug")
                    avatar = member_accessor.take_n("attributes", "avatar_url")
                    location = member_accessor.take_n("attributes", "location")
                    member_github = member_accessor.take_n("attributes", "github")
                    member_twitter = member_accessor.take_n("attributes", "twitter")
                    member_account = orbit.MemberAccount(
                        name=name,
                        love=love,
                        slug=slug,
                        avatar=avatar,
                        location=location,
                        github=member_github,
                        twitter=member_twitter,
                    )
                    queries.append(create_record(member_account.cyp_merge_node()))

                github_data = take_type_from_array(included, "github_identity")
                if github_data:
                    github_accessor = JsonDataAccessor(github_data)
                    print(dumps_utf8(github_accessor._data))
                    username = github_accessor.take_n("attributes", "username")
                    source_host = github_accessor.take_n("attributes", "source_host")
                    github_account = github.GithubAccount(
                        avatar=None,
                        company=None,
                        bio=None,
                        hireable=None,
                        login=username,
                        id=None,
                        url="https://%s/%s" % (source_host, username),
                    )
                    queries.append(create_record(github_account.cyp_merge_node()))
                    github_accounts = github.process_github([username])
                    for username, account in github_accounts.items():
                        print("GITHUB:", username, "FOLLOWS:", account.following)
                        queries.append(create_record(account.cyp_merge_node()))
                        for follows in account.following:
                            queries.append(create_record(account.cyp_follows(follows)))

                twitter_data = take_type_from_array(included, "twitter_identity")
                if twitter_data:
                    twitter_accessor = JsonDataAccessor(twitter_data)
                    print(dumps_utf8(twitter_accessor._data))
                    username = twitter_accessor.take_n("attributes", "username")
                    twitter_account = twitter.TwitterAccount(
                        name=None, username=username, profile_image_url=None, id=None
                    )
                    queries.append(create_record(twitter_account.cyp_merge_node()))
                    twitter_accounts = twitter.process_twitter(
                        [username], single_request=True
                    )
                    for username, account in twitter_accounts.items():
                        print("TWITTER:", username, "FOLLOWS:", account.following)
                        queries.append(create_record(account.cyp_merge_node()))
                        for follows in account.following:
                            queries.append(create_record(account.cyp_follows(follows)))

                if member_account and twitter_account:
                    queries.append(
                        create_record(
                            member_account.cyp_has_twitter(twitter_account.username)
                        )
                    )
                if member_account and github_account:
                    queries.append(
                        create_record(
                            member_account.cyp_has_github(github_account.login)
                        )
                    )

                if member_account and activity_id:
                    activity_node = activity.ActivityNode(
                        id=activity_id,
                        date=activity_time,
                        url=activity_url,
                        action=activity_type,
                        username=member_account.slug,
                    )
                    queries.append(create_record(activity_node.cyp_merge_node()))
                    queries.append(create_record(activity_node.cyp_made()))
            # ORBIT EVENT

        except Exception as e:
            print("Failed to process message %s" % i)
            print(e)
            import traceback

            traceback.print_exc()

    return queries
