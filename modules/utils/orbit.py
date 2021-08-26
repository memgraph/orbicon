from string import Template

from utils.abstract import NodeAbstract
from utils.data_provider import get_orbit_json_events


class MemberNode(NodeAbstract):
    template = Template(
        'MERGE (n:Member {love: "$love", name: "$name", username: "$username", avatar: "$avatar", location: "$location"});'
    )

    def __init__(self, love, name, slug, avatar, location, github, twitter):
        self.love = love
        self.name = name
        self.slug = slug
        self.avatar = avatar
        self.location = location
        self.github = github
        self.twitter = twitter

    def get_node_cypher(self):
        return MemberNode.template.substitute(
            love=self.love,
            name=self.name,
            username=self.slug,
            avatar=self.avatar,
            location=self.location,
        )


def load_orbit_already_processed():
    return {
        event["member_slug"]: MemberNode(
            love=None,
            name=event["member_name"],
            slug=event["member_slug"],
            avatar=None,
            location=None,
            github=event["member_github"],
            twitter=event["member_twitter"],
        )
        for event in get_orbit_json_events()
    }
