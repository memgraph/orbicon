import os
import pandas as pd
import simplejson as json

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


class ActivityHistoryItemConstants:
    ID = "Id"
    ActivityChannel = "ActivityChannel"
    ActivityType = "ActivityType"
    MemberName = "MemberName"
    MemberSlug = "MemberSlug"
    OrbitUrl = "OrbitUrl"
    OccurredAt = "OccurredAt"
    MemberGithub = "MemberGithub"
    MemberTwitter = "MemberTwitter"
    MemberEmail = "MemberEmail"
    MemberDiscourse = "MemberDiscourse"
    Key = "Key"
    CreatedAt = "CreatedAt"
    UpdatedAt = "UpdatedAt"
    G = "G"
    GTitle = "GTitle"
    GNumber = "GNumber"
    GHtmlUrl = "GHtmlUrl"
    GMerged = "GMerged"
    IsPullRequest = "IsPullRequest"
    ActivityLink = "ActivityLink"
    CustomDescription = "CustomDescription"
    CustomLink = "CustomLink"
    CustomLinkText = "CustomLinkText"
    CustomTitle = "CustomTitle"
    CustomType = "CustomType"


class ActivityHistoryItem:
    def __init__(
        self,
        id: int,
        activity_channel: str,
        activity_type: str,
        member_name: str,
        member_slug: str,
        orbit_url: str,
        occured_at: str,
        member_github: str,
        member_twitter: str,
        member_email: str,
        member_discourse: str,
        key: str,
        created_at: str,
        updated_at: str,
        github: str,
        github_title: str,
        github_number: str,
        github_html_url: str,
        github_merged: str,
        is_pull_request: str,
        activity_link: str,
        custom_description: str,
        custom_link: str,
        custom_link_text: str,
        custom_title: str,
        custom_type: str,
    ):
        self.id = id
        self.activity_channel = activity_channel
        self.activity_type = activity_type
        self.member_name = member_name
        self.member_slug = member_slug
        self.orbit_url = orbit_url
        self.occured_at = occured_at
        self.member_github = member_github
        self.member_twitter = member_twitter
        self.member_email = member_email
        self.member_discourse = member_discourse
        self.key = key
        self.created_at = created_at
        self.updated_at = updated_at
        self.github = github
        self.github_title = github_title
        self.github_number = github_number
        self.github_html_url = github_html_url
        self.github_merged = github_merged
        self.is_pull_request = is_pull_request
        self.activity_link = activity_link
        self.custom_description = custom_description
        self.custom_link = custom_link
        self.custom_link_text = custom_link_text
        self.custom_title = custom_title
        self.custom_type = custom_type


if __name__ == "__main__":
    data_dir = os.path.join(SCRIPT_DIR, "..", "data")

    input_path = os.path.join(data_dir, "memgraph_orbit_events_2021_08_23.txt")
    df = pd.read_csv(input_path)
    events = []
    for index, row in df.iterrows():
        data_item = ActivityHistoryItem(
            id=row[ActivityHistoryItemConstants.ID],
            activity_channel=row[ActivityHistoryItemConstants.ActivityChannel],
            activity_type=row[ActivityHistoryItemConstants.ActivityType],
            member_name=row[ActivityHistoryItemConstants.MemberName],
            member_slug=row[ActivityHistoryItemConstants.MemberSlug],
            orbit_url=row[ActivityHistoryItemConstants.OrbitUrl],
            occured_at=row[ActivityHistoryItemConstants.OccurredAt],
            member_github=row[ActivityHistoryItemConstants.MemberGithub],
            member_twitter=row[ActivityHistoryItemConstants.MemberTwitter],
            member_email=row[ActivityHistoryItemConstants.MemberEmail],
            member_discourse=row[ActivityHistoryItemConstants.MemberDiscourse],
            key=row[ActivityHistoryItemConstants.Key],
            created_at=row[ActivityHistoryItemConstants.CreatedAt],
            updated_at=row[ActivityHistoryItemConstants.UpdatedAt],
            github=row[ActivityHistoryItemConstants.G],
            github_title=row[ActivityHistoryItemConstants.GTitle],
            github_number=row[ActivityHistoryItemConstants.GNumber],
            github_html_url=row[ActivityHistoryItemConstants.GHtmlUrl],
            github_merged=row[ActivityHistoryItemConstants.GMerged],
            is_pull_request=row[ActivityHistoryItemConstants.IsPullRequest],
            activity_link=row[ActivityHistoryItemConstants.ActivityLink],
            custom_description=row[ActivityHistoryItemConstants.CustomDescription],
            custom_link=row[ActivityHistoryItemConstants.CustomLink],
            custom_link_text=row[ActivityHistoryItemConstants.CustomLinkText],
            custom_title=row[ActivityHistoryItemConstants.CustomTitle],
            custom_type=row[ActivityHistoryItemConstants.CustomType],
        )
        events.append(vars(data_item))

    output_path = os.path.join(data_dir, "memgraph_orbit_events.json")
    with open(output_path, "w") as jsonFile:
        jsonFile.write(json.dumps(events, indent=4, ignore_nan=True))
