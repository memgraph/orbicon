from string import Template

from utils.data_provider import get_orbit_json_events


class ActivityNode:
    CYP_CREATE_NODE = Template(
        """
        CREATE (n:Activity {
            id: "$id",
            date: "$date",
            url: "$url",
            action: "$action",
            username: "$username"
        });
    """
    )
    CYP_MERGE_NODE = Template(
        """
        MERGE (n:Activity {id: "$id"})
        ON CREATE SET n += {date: "$date", url: "$url", action: "$action", username: "$username"}
        ON MATCH SET n += {date: "$date", url: "$url", action: "$action", username: "$username"}
    """
    )
    CYP_MADE = Template(
        """
        MATCH (n:Member {username: "$source"}), (m:Activity {id: "$target"}) MERGE (n)-[:MADE]->(m);
    """
    )

    def __init__(self, id, date, url, action, username):
        self.id = str(id)
        self.date = date
        self.url = url
        self.action = action
        self.username = username

    def cyp_create_node(self):
        return ActivityNode.CYP_CREATE_NODE.substitute(
            id=self.id,
            date=self.date,
            url=self.url,
            action=self.action,
            username=self.username,
        )

    def cyp_merge_node(self):
        return ActivityNode.CYP_MERGE_NODE.substitute(
            id=self.id,
            date=self.date,
            url=self.url,
            action=self.action,
            username=self.username,
        )

    def cyp_made(self):
        return ActivityNode.CYP_MADE.substitute(source=self.username, target=self.id)


def load_activity_already_processed():
    return {
        event["id"]: ActivityNode(
            id=event["id"],
            date=event["occured_at"],
            url=event["orbit_url"],
            action=event["activity_type"],
            username=event["member_slug"],
        )
        for event in get_orbit_json_events()
    }
