class Member:
    def __init__(self, username: str, name: str, love: str, location: str, avatar: str):
        self.username = username if username not in [None, "None"] else None
        self.name = name if name not in [None, "None"] else None
        self.love = love if love not in [None, "None"] else None
        self.location = location if location not in [None, "None"] else None
        self.avatar = avatar if avatar not in [None, "None"] else None


class Twitter:
    def __init__(self, username: str, name: str, profile_image_url):
        self.username = username if username not in [None, "None"] else None
        self.name = name if name not in [None, "None"] else None
        self.profile_image_url = profile_image_url if profile_image_url not in [None, "None"] else None


class Github:
    def __init__(self, username: str, company: str, hireable: str, avatar: str):
        self.username = username if username not in [None, "None"] else None
        self.company = company if company not in [None, "None"] else None
        self.hireable = hireable if hireable not in [None, "None"] else None
        self.avatar = avatar if avatar not in [None, "None"] else None


def create_member(props):
    return Member(props["username"], props["name"], props["love"], props["location"], props["avatar"])


def create_twitter(props):
    return Twitter(props["username"], props["name"], props["profile_image_url"])


def create_github(props):
    return Github(props["username"], props["company"], props["hireable"], props["avatar"])