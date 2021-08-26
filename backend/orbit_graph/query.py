from typing import Any, Dict, Iterator

from orbit_graph.database import Memgraph
from orbit_graph.database.config import MG_PORT, MG_HOST, MG_ENCRYPTED, MG_USERNAME, MG_PASSWORD

from orbit_graph.database.orbit_models import (
    create_member,
    create_github,
    create_twitter,
    create_empty_github,
    create_empty_twitter,
)

db = Memgraph(host=MG_HOST, port=MG_PORT, username=MG_USERNAME, password=MG_PASSWORD, encrypted=MG_ENCRYPTED)


def query(command: str) -> Iterator[Dict[str, Any]]:
    """Queries Memgraph database and returns iterator of results"""
    yield from db.execute_and_fetch(command)


def dbUsernames():
    usernamesQuery = f"MATCH (n:Member) RETURN n.username"
    return _dbUsernamesExecution(usernamesQuery)


def dbUsernamesPrefix(prefix):
    lower_prefix = prefix.lower()
    usernamesQuery = f'MATCH (n:Member) WHERE STARTSWITH(TOLOWER(n.username), "{lower_prefix}") RETURN n.username'
    return _dbUsernamesExecution(usernamesQuery)


def _dbUsernamesExecution(query):
    usernamesResults = db.execute_and_fetch(query)

    usernames = []
    for result in usernamesResults:
        usernames.append(Username(result["n.username"]))
        if len(usernames) > 5:
            break

    return Usernames(usernames)


def dbUserDetails(username):
    memberQuery = f'MATCH (n:Member) WHERE n.username = "{username}" RETURN n'
    member_results = list(db.execute_and_fetch(memberQuery))

    member_model = create_member(member_results[0]["n"]._properties) if len(member_results) > 0 else None

    if member_model is None:
        return None

    twitterQuery = f'MATCH (n:Member)-[:HAS]->(m:Twitter) WHERE n.username = "{username}" RETURN m'
    twitter_results = list(db.execute_and_fetch(twitterQuery))
    twitter_model = (
        create_twitter(twitter_results[0]["m"]._properties) if len(twitter_results) > 0 else create_empty_twitter()
    )

    githubQuery = f'MATCH (n:Member)-[:HAS]->(m:Github) WHERE n.username = "{username}" RETURN m'
    github_results = list(db.execute_and_fetch(githubQuery))
    github_model = (
        create_github(github_results[0]["m"]._properties) if len(github_results) > 0 else create_empty_github()
    )

    return UserDetails(member_model, github_model, twitter_model)


class UserDetails:
    NOT_ACCEPTED_DETAILS = ["", "None", None]

    def __init__(self, member, github, twitter):
        self.username = member.username
        self.avatar = (
            member.avatar
            if member.avatar is not None
            else github.avatar
            if github.avatar is not None
            else twitter.profile_image_url
        )
        self.name = member.name if member.name is not None else twitter.name
        self.name = self.name if self.name not in UserDetails.NOT_ACCEPTED_DETAILS else "Unknown"

        self.love = member.love
        self.love = self.love if self.love is not None else "Unknown"

        self.importance = member.love
        self.importance = self.importance if self.importance is not None else "Unknown"

        self.location = member.location if member.location not in UserDetails.NOT_ACCEPTED_DETAILS else "Unknown"

        self.company = github.company if github.company not in UserDetails.NOT_ACCEPTED_DETAILS else "Unknown"

        self.hireable = github.hireable if github.hireable not in UserDetails.NOT_ACCEPTED_DETAILS else False

        self.githubAccount = "https://github.com/gitbuda"
        self.twitterAccount = "https://twitter.com/mbudiselicbuda"

        self.githubUsername = (
            github.username if github.username not in UserDetails.NOT_ACCEPTED_DETAILS else member.username
        )
        self.twitterUsername = (
            twitter.username if twitter.username not in UserDetails.NOT_ACCEPTED_DETAILS else member.username
        )


class Usernames:
    def __init__(self, usernames):
        self.usernames = usernames


class Username:
    def __init__(self, username):
        self.username = username


class MemberGraph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges


class MemberGraphNode:
    def __init__(self, id, importance, community_id, love, username, avatar):
        self.id = id
        self.importance = importance
        self.communityId = community_id
        self.love = love
        self.username = username
        self.avatar = avatar


class MemberGraphEdge:
    def __init__(self, from_edge, to_edge):
        self.from_edge = from_edge
        self.to_edge = to_edge

    def __dict__(self):
        return {"from": self.from_edge, "to": self.to_edge}


class Activity:
    def __init__(self, username, action, description, date):
        self.username = username
        self.action = action
        self.description = description
        self.date = date
