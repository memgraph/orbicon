import random

NOT_ACCEPTED_DETAILS = ["", "None", None]

colors = ["#2a2d34", "#009ddc", "#f26430", "#6761a8", "009b72"]


class Member:
    def __init__(self, username: str, name: str, love: str, location: str, avatar: str, importance: str):
        self.username = username if username not in NOT_ACCEPTED_DETAILS else None
        self.name = name if name not in NOT_ACCEPTED_DETAILS else None
        self.love = love if love not in NOT_ACCEPTED_DETAILS else None
        self.location = location if location not in NOT_ACCEPTED_DETAILS else None
        self.avatar = avatar if avatar not in NOT_ACCEPTED_DETAILS else None
        self.importance = importance if importance not in NOT_ACCEPTED_DETAILS else 0


class Twitter:
    def __init__(self, username: str, name: str, profile_image_url: str, url: str):
        self.username = username if username not in NOT_ACCEPTED_DETAILS else None
        self.name = name if name not in NOT_ACCEPTED_DETAILS else None
        self.profile_image_url = profile_image_url if profile_image_url not in NOT_ACCEPTED_DETAILS else None
        self.url = url if url not in NOT_ACCEPTED_DETAILS else None


class Github:
    def __init__(self, username: str, company: str, hireable: str, avatar: str, url: str):
        self.username = username if username not in NOT_ACCEPTED_DETAILS else None
        self.company = company if company not in NOT_ACCEPTED_DETAILS else None
        self.hireable = hireable if hireable not in NOT_ACCEPTED_DETAILS else None
        self.avatar = avatar if avatar not in NOT_ACCEPTED_DETAILS else None
        self.url = url if url not in NOT_ACCEPTED_DETAILS else None


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
    COMMUNITY_ID = "communityId"


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
        props[MemberConstants.IMPORTANCE] if MemberConstants.IMPORTANCE in props else 0,
        #TODO: Change this and call pagerank every time on webhook
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
    def __init__(
        self, id, importance, community_id, community_name, love, username, avatar, max_importance, min_importance
    ):
        self.id = id
        self.label = username
        self.shape = "circularImage"
        self.image = avatar

        tmp_importance = 25 + 75 * (importance - min_importance) / (max_importance - min_importance)
        self.importance = "{:.2f}".format(tmp_importance)

        self.size = tmp_importance
        self.community_name = community_name
        self.love = love if love not in NOT_ACCEPTED_DETAILS else "Unknown"

        self.borderWidth = 8
        self.color = {}
        self.color["border"] = colors[community_id]


class MemberGraphEdge:
    def __init__(self, from_edge, to_edge):
        self.from_edge = from_edge
        self.to_edge = to_edge
        self.length = 500


def create_member_node(id, props, community_names, max_importance, min_importance):
    community_id = int(props[MemberConstants.COMMUNITY_ID])
    community_name = community_names[community_id]

    return MemberGraphNode(
        id,
        props[MemberConstants.IMPORTANCE],
        community_id,
        community_name,
        props[MemberConstants.LOVE],
        props[MemberConstants.USERNAME],
        props[MemberConstants.AVATAR],
        max_importance,
        min_importance,
    )


def create_member_graph_edge(id1, id2):
    return MemberGraphEdge(id1, id2)


left_part = [
    "admiring",
    "adoring",
    "agitated",
    "amazing",
    "angry",
    "awesome",
    "backstabbing",
    "berserk",
    "big",
    "boring",
    "clever",
    "cocky",
    "compassionate",
    "condescending",
    "cranky",
    "desperate",
    "determined",
    "distracted",
    "dreamy",
    "drunk",
    "ecstatic",
    "elated",
    "elegant",
    "evil",
    "fervent",
    "focused",
    "furious",
    "gigantic",
    "gloomy",
    "goofy",
    "grave",
    "happy",
    "high",
    "hopeful",
    "hungry",
    "insane",
    "jolly",
    "jovial",
    "kickass",
    "lonely",
    "loving",
    "mad",
    "modest",
    "naughty",
    "nauseous",
    "nostalgic",
    "pedantic",
    "pensive",
    "prickly",
    "reverent",
    "romantic",
    "sad",
    "serene",
    "sharp",
    "sick",
    "silly",
    "sleepy",
    "small",
    "stoic",
    "stupefied",
    "suspicious",
    "tender",
    "thirsty",
    "tiny",
    "trusting",
]

right_part = [
    "albattani",
    "allen",
    "almeida",
    "archimedes",
    "ardinghelli",
    "aryabhata",
    "austin",
    "babbage",
    "banach",
    "bardeen",
    "bartik",
    "bassi",
    "bell",
    "bhabha",
    "bhaskara",
    "blackwell",
    "bohr",
    "booth",
    "borg",
    "bose",
    "boyd",
    "brahmagupta",
    "brattain",
    "brown",
    "carson",
    "chandrasekhar",
    "colden",
    "cori",
    "cray",
    "curie",
    "darwin",
    "davinci",
    "dijkstra",
    "dubinsky",
    "easley",
    "einstein",
    "elion",
    "engelbart",
    "euclid",
    "euler",
    "fermat",
    "fermi",
    "feynman",
    "franklin",
    "galileo",
    "gates",
    "goldberg",
    "goldstine",
    "goldwasser",
    "golick",
    "goodall",
    "hamilton",
    "hawking",
    "heisenberg",
    "heyrovsky",
    "hodgkin",
    "hoover",
    "hopper",
    "hugle",
    "hypatia",
    "jang",
    "jennings",
    "jepsen",
    "joliot",
    "jones",
    "kalam",
    "kare",
    "keller",
    "khorana",
    "kilby",
    "kirch",
    "knuth",
    "kowalevski",
    "lalande",
    "lamarr",
    "leakey",
    "leavitt",
    "lichterman",
    "liskov",
    "lovelace",
    "lumiere",
    "mahavira",
    "mayer",
    "mccarthy",
    "mcclintock",
    "mclean",
    "mcnulty",
    "meitner",
    "meninsky",
    "mestorf",
    "minsky",
    "mirzakhani",
    "morse",
    "murdock",
    "newton",
    "nobel",
    "noether",
    "northcutt",
    "noyce",
    "panini",
    "pare",
    "pasteur",
    "payne",
    "perlman",
    "pike",
    "poincare",
    "poitras",
    "ptolemy",
    "raman",
    "ramanujan",
    "ride",
    "ritchie",
    "roentgen",
    "rosalind",
    "saha",
    "sammet",
    "shaw",
    "shirley",
    "shockley",
    "sinoussi",
    "snyder",
    "spence",
    "stallman",
    "stonebraker",
    "swanson",
    "swartz",
    "swirles",
    "tesla",
    "thompson",
    "torvalds",
    "turing",
    "varahamihira",
    "visvesvaraya",
    "volhard",
    "wescoff",
    "williams",
    "wilson",
    "wing",
    "wozniak",
    "wright",
    "yalow",
    "yonath",
]


def choose_names(community_size):
    community_names = []

    for i in range(community_size):
        left = random.choice(left_part).capitalize()
        right = random.choice(right_part).capitalize()

        community_names.append(f"{left} {right}")

    return community_names