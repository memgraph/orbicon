import collections

import simplejson as json
from string import Template

import requests
from typing import List

from abc import ABC, abstractmethod

from simplejson import JSONDecodeError

from backend.scripts.load_event_history_data import ActivityHistoryItem

edge_github_cypher_template = Template(
    'MATCH (n:Github {id: "$source"}), (m:Github {id: "$target"}) MERGE (n)-[:FOLLOWS]->(m);')

OAUTH_TOKEN = ""

GITHUB_FILE_NAME = "memgraph_orbit_github_accounts.json"


class NodeAbstract(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_node_cypher(self):
        pass


class GithubNode(NodeAbstract):
    template = Template('MERGE (n:Github {avatar: "$avatar", company:"$company", bio:"$bio", hireable:"$hireable"});')

    def __init__(self, avatar, company, bio, hireable):
        super().__init__()
        self.hireable = hireable
        self.avatar = avatar
        self.company = company
        self.bio = bio

    def get_node_cypher(self):
        return GithubNode.template.substitute(avatar=self.avatar, company=self.company, bio=self.bio,
                                              hireable=self.hireable)


class TwitterNode:
    def __init__(self, name, username, profile_image_url):
        self.name = name
        self.username = username
        self.profile_image_url = profile_image_url


class MemberNode:
    def __init__(self, id, love, name, avatar, location):
        self.id = id
        self.love = love
        self.name = name
        self.avatar = avatar
        self.location = location


###############################################
# GITHUB FUNCTIONS
###############################################

class GithubAccount:
    def __init__(self, avatar, company, bio, hireable, login, id):
        self.hireable = hireable
        self.avatar = avatar
        self.company = company
        self.bio = bio
        self.login = login
        self.id = id
        self.following: List[str] = []
        self.is_processed: bool = False

    def __str__(self):
        return "id={id}," \
               "is_processed={is_processed}," \
               "avatar={avatar}," \
               "company={company}," \
               "login={login}," \
               "hireable:{hireable}," \
               "following:{following}".format(id=self.id, company=self.company, login=self.login, avatar=self.avatar,
                                              hireable=self.hireable, following=",".join(self.following),
                                              is_processed=self.is_processed)


def send_github_users_request(name):
    headers = {'Authorization': 'token %s' % OAUTH_TOKEN}
    response = requests.get("https://api.github.com/users/{name}".format(name=name),
                            params={"accept": "application/vnd.github.v3+json"}, headers=headers)
    if not response.ok:
        print("name:", name, ",response content:", response.content)
        return None

    return response.json()


def send_github_users_following_request(name):
    headers = {'Authorization': 'token %s' % OAUTH_TOKEN}
    response = requests.get("https://api.github.com/users/{name}/following".format(name=name),
                            params={"accept": "application/vnd.github.v3+json"}, headers=headers)
    if not response.ok:
        return None

    return response.json()


def parse_key(json_obj, key):
    return json_obj[key] if key in json_obj else ""


def parse_github_account(github_account_json) -> GithubAccount:
    return GithubAccount(avatar=parse_key(github_account_json, "avatar_url"),
                         company=parse_key(github_account_json, "company"),
                         bio=parse_key(github_account_json, "bio"),
                         hireable=parse_key(github_account_json, "hireable"),
                         login=parse_key(github_account_json, "login"),
                         id=parse_key(github_account_json, "id"))


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
    github_following_accounts = list(map(parse_github_account, github_user_following_response))

    # expand the dictionary with new accounts to process
    for github_following_account in github_following_accounts:
        github_main_account.following.append(github_following_account.login)
        github_dict[github_following_account.login] = github_following_account

    return github_dict


def get_github_recursive_following(github_dict: {}, depth_following_level=1):
    """
    github_dict :
    if value is None or is_processed=False - not processed yet
    processing - get main account + add accounts it follows in dict for further processing (level+1)
    """
    for i in range(depth_following_level):
        new_github_dict = {}
        for name, github_account in github_dict.items():

            if github_account is not None and github_account.is_processed:
                continue

            new_github_account_dict = create_github_account_obj(name)
            new_github_dict = {**new_github_dict, **new_github_account_dict}

        github_dict = {**github_dict, **new_github_dict}

    return github_dict


def get_github_members(orbit_events: List[ActivityHistoryItem]):
    github_members = list(filter(lambda x: x["member_github"], orbit_events))
    github_members_names = set(map(lambda x: x["member_github"], github_members))

    return github_members_names


def load_github_already_processed():
    data_dir = "../data"
    filename = f"{data_dir}/{GITHUB_FILE_NAME}"

    github_dict_processed = {}
    with open(filename) as json_file:
        try:
            github_accounts_json: List[GithubAccount] = json.load(json_file)
        except JSONDecodeError:
            return github_dict_processed



    for github_key in github_accounts_json:
        github_account_json = github_accounts_json[github_key]
        if len(github_account_json) == 0:
            github_dict_processed[github_key] = None
            continue
        github_account = GithubAccount(avatar=github_account_json["avatar"],
                                       company=github_account_json["company"],
                                       bio=github_account_json["bio"],
                                       hireable=github_account_json["hireable"],
                                       login=github_account_json["login"],
                                       id=github_account_json["id"])
        github_account.following = github_account_json["following"]
        github_account.is_processed = github_account_json["is_processed"]

        github_dict_processed[github_account.login] = github_account

    return github_dict_processed


def process_github(orbit_events_json: List[ActivityHistoryItem]):
    github_members_names = get_github_members(orbit_events_json)

    github_dict = {}
    for github_name in github_members_names:
        github_dict[github_name] = None

    github_dict_processed = load_github_already_processed()

    github_dict = {**github_dict, **github_dict_processed}

    github_dict = get_github_recursive_following(github_dict, depth_following_level=1)

    github_json_dict = {}
    for key, value in github_dict.items():
        github_json_dict[key] = vars(value) if value is not None else ""

    with open(f"{data_dir}/{GITHUB_FILE_NAME}", "w") as jsonFile:
        jsonFile.write(json.dumps(github_json_dict, indent=4, ignore_nan=True))

    print(len(github_json_dict))


def create_members_cypher_queries(nodes: List[NodeAbstract]):
    nodes_cypher = []
    for node in nodes:
        nodes_cypher.append(node.get_node_cypher())
    print(nodes_cypher)


if __name__ == "__main__":
    data_dir = "../data"

    filename = f"{data_dir}/memgraph_orbit_events.json"
    with open(filename) as json_file:
        orbit_events_json: List[ActivityHistoryItem] = json.load(json_file)

    process_github(orbit_events_json)
