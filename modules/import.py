import mgclient

from utils.github import load_github_already_processed
from utils.twitter import load_twitter_already_processed
from utils.orbit import load_orbit_already_processed


if __name__ == "__main__":
    conn = mgclient.connect(host="localhost", port=7687)
    conn.autocommit = True
    conn.cursor().execute("CREATE INDEX ON :Github(username);")
    conn.cursor().execute("CREATE INDEX ON :Member(username);")
    conn.cursor().execute("CREATE INDEX ON :Twitter(username);")

    # GITHUB
    for _, account in load_github_already_processed().items():
        if account is None:
            continue
        conn.cursor().execute(account.cyp_merge_node())
    for _, account in load_github_already_processed().items():
        if account is None:
            continue
        for following in account.following:
            conn.cursor().execute(account.cyp_follows(following))

    # TWITTER
    for _, account in load_twitter_already_processed().items():
        if account is None:
            continue
        conn.cursor().execute(account.cyp_merge_node())
    for _, account in load_twitter_already_processed().items():
        if account is None:
            continue
        for following in account.following:
            conn.cursor().execute(account.cyp_follows(following))

    # ORBIT
    for _, account in load_orbit_already_processed().items():
        if account is None:
            continue
        conn.cursor().execute(account.cyp_merge_node())
        if account.github:
            conn.cursor().execute(account.cyp_has_github(account.github))
        if account.twitter:
            conn.cursor().execute(account.cyp_has_twitter(account.twitter))
