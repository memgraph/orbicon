from string import Template

import mgclient
from utils.github import load_github_already_processed
from utils.twitter import load_twitter_already_processed
from utils.orbit import load_orbit_already_processed

edge_github_cypher_template = Template(
    'MATCH (n:Github {username: "$source"}), (m:Github {username: "$target"}) MERGE (n)-[:FOLLOWS]->(m);')
edge_twitter_cypher_template = Template(
    'MATCH (n:Twitter {username: "$source"}), (m:Twitter {username: "$target"}) MERGE (n)-[:FOLLOWS]->(m);')
edge_orbit_github_template = Template(
    'MATCH (n:Member {username: "$source"}), (m:Github {username: "$target"}) MERGE (n)-[:HAS]->(m);')
edge_orbit_twitter_template = Template(
    'MATCH (n:Member {username: "$source"}), (m:Twitter {username: "$target"}) MERGE (n)-[:HAS]->(m);')
edge_orbit_cypher_template = Template(
    'MATCH (n:Member {username: "$source"}), (m:Member {username: "$target"}) MERGE (n)-[:FOLLOWS]->(m);')

conn = mgclient.connect(host='ec2-34-241-136-34.eu-west-1.compute.amazonaws.com', port=7687)
conn.autocommit = True
conn.cursor().execute("CREATE INDEX ON :Github(username);")
conn.cursor().execute("CREATE INDEX ON :Member(username);")
conn.cursor().execute("CREATE INDEX ON :Twitter(username);")

# GITHUB
for username, account in load_github_already_processed().items():
    if account is None:
        continue
    conn.cursor().execute(account.get_node_cypher())
    for following in account.following:
        conn.cursor().execute(edge_github_cypher_template.substitute(source=account.login, target=following))

# TWITTER
for username, account in load_twitter_already_processed().items():
    if account is None:
        continue
    conn.cursor().execute(account.get_node_cypher())
    for following in account.following:
        conn.cursor().execute(edge_twitter_cypher_template.substitute(source=account.username, target=following))

# ORBIT
for username, account in load_orbit_already_processed().items():
    if account is None:
        continue
    conn.cursor().execute(account.get_node_cypher())
    conn.cursor().execute(edge_orbit_github_template.substitute(source=account.slug, target=account.github))
    conn.cursor().execute(edge_orbit_twitter_template.substitute(source=account.slug, target=account.twitter))
