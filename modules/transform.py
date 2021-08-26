import mgp
import json
import importlib
import utils.github as github
import utils.twitter as twitter


def json_print(data):
    print(json.dumps(data, indent=4, sort_keys=True))


def dumps_utf8(obj):
    return json.dumps(obj).encode('utf-8')


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


def merge_member_query(slug):
    return f"""MERGE (:Member {{slug: \"{slug}\"}});"""


def merge_github_query(username):
    return f"""MERGE (:Github {{username: \"{username}\"}});"""


def merge_twitter_query(username):
    return f"""MERGE (:Twitter {{username: \"{username}\"}});"""


def create_record(query):
    return mgp.Record(query=query, parameters={})


@mgp.transformation
def kafka2graph_transform(
    messages: mgp.Messages,
) -> mgp.Record(query=str, parameters=mgp.Nullable[mgp.Map]):
    importlib.reload(github)
    importlib.reload(twitter)
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
            if member_slug is not None or member_github is None or member_twitter is None:
                if member_slug is not None:
                    queries.append(create_record(merge_member_query(member_slug)))
                if member_github is not None:
                    queries.append(create_record(merge_github_query(member_github)))
                if member_twitter is not None:
                    queries.append(create_record(merge_twitter_query(member_twitter)))

            # ORBIT EVENT
            # For some reason the payload is wrapped twice.
            event_payload = accessor.take_n("event_payload")
            if event_payload is not None:  # Event.
                accessor = JsonDataAccessor(json.loads(payload["event_payload"])["event_payload"])
                # member_id = accessor.take_n("data", "relationships", "member", "data", "id")
                included = accessor.take_n("included")
                member_data = take_type_from_array(included, "member")
                if member_data:
                    member_accessor = JsonDataAccessor(member_data)
                    slug = member_accessor.take_n("attributes", "slug")
                    queries.append(create_record(merge_member_query(slug)))
                github_data = take_type_from_array(included, "github_identity")
                if github_data:
                    github_accessor = JsonDataAccessor(github_data)
                    username = github_accessor.take_n("attributes", "username")
                    github_accounts = github.process_github([username])
                    for username, account in github_accounts.items():
                        print(account.following)
                    # TODO(gitbuda): Create Github account node and followers.
                    queries.append(create_record(merge_member_query(username)))
                twitter_data = take_type_from_array(included, "twitter_identity")
                if twitter_data:
                    twitter_accessor = JsonDataAccessor(twitter_data)
                    username = twitter_accessor.take_n("attributes", "username")
                    twitter_accounts = twitter.process_twitter([username])
                    for username, account in twitter_accounts.items():
                        print(account.following)
                    # TODO(gitbuda): Create Twitter account node and followers.
                    queries.append(create_record(merge_member_query(username)))
        except Exception as e:
            print("Failed to process message %s" % i)
            print(e)
            import traceback
            traceback.print_exc()

    for query in queries:
        print(query)

    return queries
