from typing import Any, Dict, Iterator

from orbit_graph.database import Memgraph
from orbit_graph.database.config import MG_PORT, MG_HOST, MG_ENCRYPTED, MG_USERNAME, MG_PASSWORD

from orbit_graph.database.orbit_models import (
    MemberConstants,
    create_activity,
    create_github,
    create_twitter,
    create_member,
    create_empty_github,
    create_empty_twitter,
    create_member_node,
    create_member_graph_edge,
    NOT_ACCEPTED_DETAILS,
    get_community_name,
    Legend,
)

db = Memgraph(host=MG_HOST, port=MG_PORT, username=MG_USERNAME, password=MG_PASSWORD, encrypted=MG_ENCRYPTED)


def query(command: str) -> Iterator[Dict[str, Any]]:
    """Queries Memgraph database and returns iterator of results"""
    yield from db.execute_and_fetch(command)


def _get_avatar_from_member(props):
    avatar = props[MemberConstants.AVATAR]
    if avatar not in NOT_ACCEPTED_DETAILS:
        return avatar

    username = props[MemberConstants.USERNAME]

    twitter_query = f"MATCH (m:Member {{username: '{username}'}})-[:HAS]->(t:Twitter) RETURN t.profile_image_url"
    twitter_result = list(db.execute_and_fetch(twitter_query))
    avatar = twitter_result[0]["t.profile_image_url"] if len(twitter_result) > 0 else None
    if avatar not in NOT_ACCEPTED_DETAILS:
        return avatar

    github_query = f"MATCH (m:Member {{username: '{username}'}})-[:HAS]->(g:Github) RETURN g.avatar"
    github_result = list(db.execute_and_fetch(github_query))
    avatar = github_result[0]["g.avatar"] if len(github_result) > 0 else None

    return avatar


def _max_min_importance():
    importance_max_min_query = f"MATCH (m:Member) WITH MAX(m.importance) AS max_importance, MIN(m.importance) AS min_importance RETURN max_importance, min_importance"
    result_min_max = list(db.execute_and_fetch(importance_max_min_query))[0]
    max, min = result_min_max["max_importance"], result_min_max["min_importance"]
    return max, min


def dbLegend():
    return Legend()


def dbMemberGraph():
    max, min = _max_min_importance()

    member_graph_query = f"MATCH (n)-[c:CONNECTS]->(m) return n, c, m"
    results = db.execute_and_fetch(member_graph_query)

    member_graph_nodes = []
    member_graph_edges = []

    member_node_ids = set()
    for result in results:
        id = result["n"]._id

        if id not in member_node_ids:
            props = result["n"]._properties
            avatar = _get_avatar_from_member(props)
            props["avatar"] = avatar
            member_node = create_member_node(id, props, max, min)
            member_node.avatar = avatar
            member_graph_nodes.append(member_node)
            member_node_ids.add(id)

        id2 = result["m"]._id

        if id2 not in member_node_ids:
            props2 = result["m"]._properties
            avatar = _get_avatar_from_member(props2)
            props2["avatar"] = avatar
            member_node = create_member_node(id2, props2, max, min)
            member_graph_nodes.append(member_node)
            member_node_ids.add(id2)

        member_edge = create_member_graph_edge(id, id2)
        member_graph_edges.append(member_edge)

    return MemberGraph(member_graph_nodes, member_graph_edges)


def dbActivities():
    activity_query = f"MATCH (n:Activity)<-[:MADE]-(m:Member) RETURN n,m ORDER BY n.date DESC LIMIT 10;"
    results = list(db.execute_and_fetch(activity_query))

    activities = []
    for result in results:
        avatar = _get_avatar_from_member(result["m"]._properties)
        activity = create_activity(result["n"]._properties)
        activity.avatar = avatar
        activities.append(activity)

    return Activities(activities)


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
    max, min = _max_min_importance()

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

    return UserDetails(member_model, github_model, twitter_model, max, min)


class UserDetails:
    def __init__(self, member, github, twitter, max_importance, min_importance):
        self.username = member.username
        self.avatar = (
            member.avatar
            if member.avatar is not None
            else github.avatar
            if github.avatar is not None
            else twitter.profile_image_url
        )
        self.name = member.name if member.name is not None else twitter.name
        self.name = self.name if self.name not in NOT_ACCEPTED_DETAILS else "Unknown"

        self.community = get_community_name(member.community)

        self.love = member.love
        self.love = self.love if self.love is not None else "Unknown"

        self.importance = 25 + 75 * (member.importance - min_importance) / (max_importance - min_importance)
        self.importance = "{:.2f}".format(self.importance)

        self.location = member.location if member.location not in NOT_ACCEPTED_DETAILS else "Unknown"

        self.company = github.company if github.company not in NOT_ACCEPTED_DETAILS else "Unknown"

        self.hireable = github.hireable if github.hireable not in NOT_ACCEPTED_DETAILS else False

        self.githubAccount = github.url
        self.twitterAccount = twitter.url

        self.githubUsername = github.username if github.username not in NOT_ACCEPTED_DETAILS else member.username
        self.twitterUsername = twitter.username if twitter.username not in NOT_ACCEPTED_DETAILS else member.username


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


class Activities:
    def __init__(self, activities):
        self.activities = activities