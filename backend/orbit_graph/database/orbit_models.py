NOT_ACCEPTED_DETAILS = ["", "None", None]


class Member:
    def __init__(self, username: str, name: str, love: str, location: str, avatar: str, importance: str):
        self.username = username if username not in [None, "None"] else None
        self.name = name if name not in [None, "None"] else None
        self.love = love if love not in [None, "None"] else None
        self.location = location if location not in [None, "None"] else None
        self.avatar = avatar if avatar not in [None, "None"] else None
        self.importance = importance if importance not in [None, "None"] else 0


class Twitter:
    def __init__(self, username: str, name: str, profile_image_url: str, url: str):
        self.username = username if username not in [None, "None"] else None
        self.name = name if name not in [None, "None"] else None
        self.profile_image_url = profile_image_url if profile_image_url not in [None, "None"] else None
        self.url = url if url not in [None, "None"] else None


class Github:
    def __init__(self, username: str, company: str, hireable: str, avatar: str, url: str):
        self.username = username if username not in [None, "None"] else None
        self.company = company if company not in [None, "None"] else None
        self.hireable = hireable if hireable not in [None, "None"] else None
        self.avatar = avatar if avatar not in [None, "None"] else None
        self.url = url if url not in [None, "None"] else None


class Activity:
    def __init__(self, id, action, date, url, username):
        self.id = id
        self.action = action
        self.date = date
        self.url = url
        self.username = username


class ActivityConstants:
    ID = "id"
    ACTION = "action"
    DATE = "date"
    URL = "url"
    USERNAME = "username"
    AVATAR = "avatar"


class MemberConstants:
    USERNAME = "username"
    NAME = "name"
    LOVE = "love"
    LOCATION = "location"
    AVATAR = "avatar"
    IMPORTANCE = "importance"


class TwitterConstants:
    USERNAME = "username"
    NAME = "name"
    PROFILE_IMAGE_URL = "profile_image_url"
    URL = "url"


class GithubConstants:
    USERNAME = "username"
    COMPANY = "company"
    HIREABLE = "hireable"
    AVATAR = "avatar"
    URL = "url"


def create_member(props):
    return Member(
        props[MemberConstants.USERNAME],
        props[MemberConstants.NAME],
        props[MemberConstants.LOVE],
        props[MemberConstants.LOCATION],
        props[MemberConstants.AVATAR],
        props[MemberConstants.IMPORTANCE],
    )


def create_empty_twitter():
    return Twitter(None, None, None, None)


def create_empty_github():
    return Github(None, None, None, None, None)


def create_twitter(props):
    return Twitter(
        props[TwitterConstants.USERNAME],
        props[TwitterConstants.NAME],
        props[TwitterConstants.PROFILE_IMAGE_URL],
        props[TwitterConstants.URL],
    )


def create_github(props):
    return Github(
        props[GithubConstants.USERNAME],
        props[GithubConstants.COMPANY],
        props[GithubConstants.HIREABLE],
        props[GithubConstants.AVATAR],
        props[GithubConstants.URL],
    )


def create_activity(props_activity):
    return Activity(
        props_activity[ActivityConstants.ID],
        props_activity[ActivityConstants.ACTION],
        props_activity[ActivityConstants.DATE].replace("UTC", ""),
        props_activity[ActivityConstants.URL],
        props_activity[ActivityConstants.USERNAME],
    )


class MemberGraphNode:
    def __init__(self, id, importance, community_id, love, username, avatar):
        self.id = id
        self.label = username
        self.shape = "circularImage"
        self.image = avatar

        tmp_importance = importance
        tmp_importance = tmp_importance if tmp_importance not in NOT_ACCEPTED_DETAILS else 25
        if tmp_importance == 0:
            tmp_importance = 25
        self.size = tmp_importance

        self.title = f"Importance: {tmp_importance}\nLove: {love}\nCommunity class: {community_id}"
        self.borderWidth = 5
        self.color = {}
        self.color["border"] = "#000"


class MemberGraphEdge:
    def __init__(self, from_edge, to_edge):
        self.from_edge = from_edge
        self.to_edge = to_edge


def create_member_node(id, props):
    return MemberGraphNode(
        id,
        props[MemberConstants.IMPORTANCE],
        1,
        props[MemberConstants.LOVE],
        props[MemberConstants.USERNAME],
        props[MemberConstants.AVATAR],
    )


def create_member_graph_edge(id1, id2):
    return MemberGraphEdge(id1, id2)