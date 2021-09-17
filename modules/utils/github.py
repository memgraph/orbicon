import os
import simplejson as json
from string import Template
import requests
from typing import List
from simplejson import JSONDecodeError

from utils.util import merge_dicts, load_token
from utils.load_event_history_data import ActivityHistoryItem

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data")
GITHUB_FILE_NAME = "memgraph_orbit_github_accounts.json"
GITHUB_FILE_PATH = os.path.join(DATA_DIR, GITHUB_FILE_NAME)
GITHUB_TOKEN_PATH = os.getenv('GITHUB_TOKEN_PATH', "/github_token.txt")
OAUTH_TOKEN = load_token(GITHUB_TOKEN_PATH)


class GithubAccount:
    CYP_CREATE_NODE = Template(
        """
        CREATE (n:Github {
            username: "$username",
            avatar: "$avatar",
            company:"$company",
            hireable:"$hireable",
            url: "$url"
        });
    """
    )
    CYP_MERGE_NODE = Template(
        """
        MERGE (n:Github {username: "$username"})
        ON CREATE SET n += {avatar: "$avatar", company:"$company", hireable:"$hireable", url: "$url"}
        ON MATCH SET n += {avatar: "$avatar", company:"$company", hireable:"$hireable", url: "$url"};
    """
    )
    CYP_FOLLOWS = Template(
        """
        MATCH (n:Github {username: "$source"}), (m:Github {username: "$target"}) MERGE (n)-[:FOLLOWS]->(m);
    """
    )

    def __init__(self, avatar, company, bio, hireable, login, id, url):
        self.hireable = hireable
        self.avatar = avatar
        self.company = company
        # TODO(gitbuda): Figure out how to store bio to the database.
        self.bio = bio
        self.login = login
        self.id = id
        self.url = "https://github.com/%s" % login if not url else url
        self.following: List[str] = []
        self.is_processed: bool = False

    def __str__(self):
        return (
            "id={id},"
            "is_processed={is_processed},"
            "avatar={avatar},"
            "company={company},"
            "login={login},"
            "hireable:{hireable},"
            "following:{following}".format(
                id=self.id,
                company=self.company,
                login=self.login,
                avatar=self.avatar,
                hireable=self.hireable,
                following=",".join(self.following),
                is_processed=self.is_processed,
            )
        )

    def cyp_create_node(self):
        return GithubAccount.CYP_CREATE_NODE.substitute(
            avatar=self.avatar,
            company=self.company,
            hireable=self.hireable,
            username=self.login,
            url=self.url,
        )

    def cyp_merge_node(self):
        return GithubAccount.CYP_MERGE_NODE.substitute(
            avatar=self.avatar,
            company=self.company,
            hireable=self.hireable,
            username=self.login,
            url=self.url,
        )

    def cyp_follows(self, other):
        return GithubAccount.CYP_FOLLOWS.substitute(source=self.login, target=other)


def send_github_users_request(name):
    headers = {"Authorization": "token %s" % OAUTH_TOKEN}
    response = requests.get(
        "https://api.github.com/users/{name}".format(name=name),
        params={"accept": "application/vnd.github.v3+json"},
        headers=headers,
    )
    if not response.ok:
        print("name:", name, ",response content:", response.content)
        return None

    return response.json()


def send_github_users_following_request(name):
    headers = {"Authorization": "token %s" % OAUTH_TOKEN}
    response = requests.get(
        "https://api.github.com/users/{name}/following".format(name=name),
        params={"accept": "application/vnd.github.v3+json"},
        headers=headers,
    )
    if not response.ok:
        return None

    return response.json()


def parse_key(json_obj, key):
    return json_obj[key] if key in json_obj else ""


def parse_github_account(github_account_json) -> GithubAccount:
    return GithubAccount(
        avatar=parse_key(github_account_json, "avatar_url"),
        company=parse_key(github_account_json, "company"),
        bio=parse_key(github_account_json, "bio"),
        hireable=parse_key(github_account_json, "hireable"),
        login=parse_key(github_account_json, "login"),
        id=parse_key(github_account_json, "id"),
        url=parse_key(github_account_json, "html_url"),
    )


def create_github_account_obj(name):
    github_dict = {}
    github_user_response = send_github_users_request(name)

    if github_user_response is None:
        return github_dict

    github_user_following_response = send_github_users_following_request(name)

    # get main account
    github_main_account = parse_github_account(github_user_response)
    github_main_account.is_processed = True

    github_dict[name] = github_main_account

    if github_user_following_response is None:
        github_main_account.is_processed = False
        return github_dict

    # get accounts that main follows
    github_following_accounts = list(
        map(parse_github_account, github_user_following_response)
    )

    # expand the dictionary with new accounts to process
    for github_following_account in github_following_accounts:
        github_main_account.following.append(github_following_account.login)
        github_dict[github_following_account.login] = github_following_account

    return github_dict


def get_github_recursive_following(github_dict, depth_following_level=1):
    """
    github_dict :
    if value is None or is_processed=False - not processed yet
    processing - get main account + add accounts it follows in dict for further processing (level+1)
    """
    for _ in range(depth_following_level):
        new_github_dict = {}

        for name, github_account in github_dict.items():

            if github_account is not None and github_account.is_processed:
                continue

            new_github_account_dict = create_github_account_obj(name)
            new_github_dict = merge_dicts(new_github_dict, new_github_account_dict)

        github_dict = merge_dicts(github_dict, new_github_dict)

    return github_dict


def get_github_members(orbit_events: List[ActivityHistoryItem]):
    github_members = list(filter(lambda x: x["member_github"], orbit_events))
    github_members_names = set(map(lambda x: x["member_github"], github_members))

    return github_members_names


def load_github_already_processed():
    github_dict_processed = {}
    with open(GITHUB_FILE_PATH) as json_file:
        try:
            github_accounts_json: List[GithubAccount] = json.load(json_file)
        except JSONDecodeError:
            return github_dict_processed

    for github_key in github_accounts_json:
        github_account_json = github_accounts_json[github_key]
        if len(github_account_json) == 0:
            github_dict_processed[github_key] = None
            continue
        github_account = GithubAccount(
            avatar=github_account_json["avatar"],
            company=github_account_json["company"],
            bio=github_account_json["bio"],
            hireable=github_account_json["hireable"],
            login=github_account_json["login"],
            id=github_account_json["id"],
            url=parse_key(github_account_json, "url"),
        )
        github_account.following = github_account_json["following"]
        github_account.is_processed = github_account_json["is_processed"]

        github_dict_processed[github_account.login] = github_account

    return github_dict_processed


def process_github_history(orbit_events_json: List[ActivityHistoryItem]):
    github_members_names = get_github_members(orbit_events_json)
    process_github(github_members_names)


def process_github(users):
    github_dict = {}
    for github_name in users:
        github_dict[github_name] = None
    github_dict = get_github_recursive_following(github_dict, depth_following_level=1)

    github_dict_processed = load_github_already_processed()
    github_dict = merge_dicts(github_dict_processed, github_dict)

    github_json_dict = {}
    for key, value in github_dict.items():
        github_json_dict[key] = vars(value) if value is not None else ""

    with open(GITHUB_FILE_PATH, "w") as jsonFile:
        jsonFile.write(json.dumps(github_json_dict, indent=4, ignore_nan=True))

    return {username: github_dict[username] for username in users}


if __name__ == "__main__":
    with open(os.path.join(DATA_DIR, "memgraph_orbit_events.json")) as json_file:
        orbit_events_json: List[ActivityHistoryItem] = json.load(json_file)
    process_github_history(orbit_events_json)
