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
