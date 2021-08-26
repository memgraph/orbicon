from string import Template

from utils.data_provider import get_orbit_json_events


class MemberNode:
    CYP_CREATE_NODE = Template(
        """
        CREATE (n:Member {love: "$love",
                          name: "$name",
                          username: "$username",
                          avatar: "$avatar",
                          location: "$location"});
    """
    )
    CYP_MERGE_NODE = Template(
        """
        MERGE (n:Member {username: "$username"})
        ON CREATE SET n += {love: "$love", name: "$name", avatar: "$avatar", location: "$location"}
        ON MATCH SET n += {love: "$love", name: "$name", avatar: "$avatar", location: "$location"};
    """
    )
    CYP_HAS_GITHUB = Template(
        """
        MATCH (n:Member {username: "$source"}), (m:Github {username: "$target"}) MERGE (n)-[:HAS]->(m);
    """
    )
    CYP_HAS_TWITTER = Template(
        """
        MATCH (n:Member {username: "$source"}), (m:Twitter {username: "$target"}) MERGE (n)-[:HAS]->(m);
    """
    )
    CYP_FOLLOWS = Template(
        """
        MATCH (n:Member {username: "$source"}), (m:Member {username: "$target"}) MERGE (n)-[:FOLLOWS]->(m);
    """
    )

    def __init__(self, love, name, slug, avatar, location, github, twitter):
        self.love = love
        self.name = name
        self.slug = slug
        self.avatar = avatar
        self.location = location
        self.github = github
        self.twitter = twitter

    def cyp_create_node(self):
        return MemberNode.CYP_CREATE_NODE.substitute(
            love=self.love,
            name=self.name,
            username=self.slug,
            avatar=self.avatar,
            location=self.location,
        )

    def cyp_merge_node(self):
        return MemberNode.CYP_MERGE_NODE.substitute(
            love=self.love,
            name=self.name,
            username=self.slug,
            avatar=self.avatar,
            location=self.location,
        )

    def cyp_has_github(self, username):
        return MemberNode.CYP_HAS_GITHUB.substitute(source=self.slug, target=username)

    def cyp_has_twitter(self, username):
        return MemberNode.CYP_HAS_TWITTER.substitute(source=self.slug, target=username)

    def cyp_follows(self, other):
        return MemberNode.CYP_FOLLOWS.substitute(source=self.slug, target=other)


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
