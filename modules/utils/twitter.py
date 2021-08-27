import os
import simplejson as json
from string import Template
import requests
from typing import List
from simplejson import JSONDecodeError

from utils.util import merge_dicts
from utils.load_event_history_data import ActivityHistoryItem

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data")
TWITTER_FILE_NAME = "memgraph_orbit_twitter_accounts.json"
TWITTER_FILE_PATH = os.path.join(DATA_DIR, TWITTER_FILE_NAME)
MAX_FOLLOWING_ACCOUNTS_ON_REQUEST = 20
# TODO(gitbuda): Figure out how to pass these environment variables into the query module.
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAA0lTAEAAAAANrpndxI81KFXLjieXcj0ZjxhbVQ%3DrMUx9pSfeiNOW3vJbaMYkxaUMkhYsozzlYJdpw0bLx8BXqpM5v"


class TwitterAccount:
    CYP_CREATE_NODE = Template(
        """
        CREATE (n:Twitter {
            username: "$username",
            name: "$name",
            profile_image_url: "$profile_image_url",
            url: "$url"
        });
    """
    )
    CYP_MERGE_NODE = Template(
        """
        MERGE (n:Twitter {username: "$username"})
        ON CREATE SET n += {name: "$name", profile_image_url: "$profile_image_url", url: "$url"}
        ON MATCH SET n += {name: "$name", profile_image_url: "$profile_image_url", url: "$url"}
    """
    )
    CYP_FOLLOWS = Template(
        """
        MATCH (n:Twitter {username: "$source"}), (m:Twitter {username: "$target"}) MERGE (n)-[:FOLLOWS]->(m);
    """
    )

    def __init__(self, name, username, profile_image_url, id):
        self.name = name
        self.username = username
        self.profile_image_url = profile_image_url
        self.id = id
        self.url = "https://twitter.com/%s" % self.username
        self.is_processed = False
        self.following: List[str] = []

    def __str__(self):
        return (
            "id={id},"
            "name={name},"
            "username={username},"
            "profile_image_url={profile_image_url},"
            "is_processed={is_processed}"
            "following:{following}".format(
                id=self.id,
                name=self.name,
                username=self.username,
                profile_image_url=self.profile_image_url,
                following=",".join(self.following),
                is_processed=self.is_processed,
            )
        )

    def cyp_create_node(self):
        return TwitterAccount.CYP_CREATE_NODE.substitute(
            username=self.username,
            name=self.name,
            profile_image_url=self.profile_image_url,
            url=self.url,
        )

    def cyp_merge_node(self):
        return TwitterAccount.CYP_MERGE_NODE.substitute(
            username=self.username,
            name=self.name,
            profile_image_url=self.profile_image_url,
            url=self.url,
        )

    def cyp_follows(self, other):
        return TwitterAccount.CYP_FOLLOWS.substitute(source=self.username, target=other)


def send_twitter_users_by_usernames_request(usernames: List[str]):
    headers = {"Authorization": "Bearer %s" % BEARER_TOKEN}

    url = "https://api.twitter.com/2/users/by?usernames={usernames}&user.fields=id,name,username,profile_image_url".format(
        usernames=",".join(usernames)
    )

    response = requests.get(url, headers=headers)
    if not response.ok:
        print("names:", ",".join(usernames), ",response content:", response.content)
        return None

    return response.json()


def send_twitter_users_following_request(id):
    headers = {"Authorization": "Bearer %s" % BEARER_TOKEN}
    url = "https://api.twitter.com/2/users/{id}/following?max_results={n}&user.fields=id,name,username,profile_image_url".format(
        n=MAX_FOLLOWING_ACCOUNTS_ON_REQUEST, id=id
    )

    response = requests.get(url, headers=headers)
    if not response.ok:
        print(response.content)
        return None

    return response.json()


def parse_key(json_obj, key):
    return json_obj[key] if key in json_obj else ""


def parse_twitter_account(twitter_account_json) -> TwitterAccount:
    return TwitterAccount(
        name=parse_key(twitter_account_json, "name"),
        username=parse_key(twitter_account_json, "username"),
        profile_image_url=parse_key(twitter_account_json, "profile_image_url"),
        id=parse_key(twitter_account_json, "id"),
    )


def create_twitter_accounts_obj_batch(names: List[str]):
    twitter_dict = {}
    twitter_users_response = send_twitter_users_by_usernames_request(names)

    if twitter_users_response is None:
        return twitter_dict

    twitter_users_json = twitter_users_response["data"]

    for twitter_user_json in twitter_users_json:
        twitter_main_account = parse_twitter_account(twitter_user_json)
        twitter_dict[twitter_main_account.username] = twitter_main_account
        twitter_following_users_response = send_twitter_users_following_request(
            twitter_main_account.id
        )

        if twitter_following_users_response is None:
            twitter_main_account.is_processed = False
            continue

        twitter_following_users_json = twitter_following_users_response["data"]

        for twitter_following_user_json in twitter_following_users_json:
            twitter_following_user_account = parse_twitter_account(
                twitter_following_user_json
            )
            twitter_dict[
                twitter_following_user_account.username
            ] = twitter_following_user_account
            twitter_main_account.following.append(
                twitter_following_user_account.username
            )

        twitter_main_account.is_processed = True

    return twitter_dict


def get_twitter_recursive_following(twitter_dict, depth_following_level=1, single_request=False):
    """
    twitter_dict :
    if value is None or is_processed=False - not processed yet
    processing - get main account + add accounts it follows in dict for further processing (level+1)
    """
    for _ in range(depth_following_level):
        new_twitter_dict = {}
        batch_twitter_names = []
        for name, twitter_account in twitter_dict.items():
            if twitter_account is not None and twitter_account.is_processed:
                continue

            batch_twitter_names.append(name)
            if (
                not single_request and len(batch_twitter_names) != 10
            ):  # twitter magic number for number of accounts you are allowed in a pull
                continue

            new_twitter_account_dict = create_twitter_accounts_obj_batch(
                batch_twitter_names
            )

            new_twitter_dict = merge_dicts(new_twitter_dict, new_twitter_account_dict)

            batch_twitter_names = []

        twitter_dict = merge_dicts(twitter_dict, new_twitter_dict)

    return twitter_dict


def get_twitter_members(orbit_events: List[ActivityHistoryItem]):
    twitter_members = list(filter(lambda x: x["member_twitter"], orbit_events))
    twitter_members_names = set(map(lambda x: x["member_twitter"], twitter_members))

    return twitter_members_names


def load_twitter_already_processed():
    twitter_dict_processed = {}
    with open(TWITTER_FILE_PATH) as json_file:
        try:
            twitter_accounts_json: List[TwitterAccount] = json.load(json_file)
        except JSONDecodeError:
            return twitter_dict_processed

    for twitter_key in twitter_accounts_json:
        twitter_account_json = twitter_accounts_json[twitter_key]
        if len(twitter_account_json) == 0:
            twitter_dict_processed[twitter_key] = None
            continue

        twitter_account = parse_twitter_account(twitter_account_json)
        twitter_account.following = twitter_account_json["following"]
        twitter_account.is_processed = twitter_account_json["is_processed"]

        twitter_dict_processed[twitter_account.username] = twitter_account

    return twitter_dict_processed


def process_twitter_history(orbit_events_json: List[ActivityHistoryItem]):
    twitter_members_names = get_twitter_members(orbit_events_json)
    process_twitter(twitter_members_names)


def process_twitter(users, single_request=False):
    twitter_dict = {}
    for twitter_name in users:
        twitter_dict[twitter_name] = None
    twitter_dict = get_twitter_recursive_following(
        twitter_dict, depth_following_level=1, single_request=single_request
    )

    twitter_dict_processed = load_twitter_already_processed()
    twitter_dict = merge_dicts(twitter_dict, twitter_dict_processed)

    twitter_json_dict = {}
    for key, value in twitter_dict.items():
        twitter_json_dict[key] = vars(value) if value is not None else ""

    with open(TWITTER_FILE_PATH, "w") as jsonFile:
        jsonFile.write(json.dumps(twitter_json_dict, indent=4, ignore_nan=True))

    return {username: twitter_dict[username] for username in users}


if __name__ == "__main__":
    with open(os.path.join(DATA_DIR, "memgraph_orbit_events.json")) as json_file:
        orbit_events_json: List[ActivityHistoryItem] = json.load(json_file)
    process_twitter(orbit_events_json)
