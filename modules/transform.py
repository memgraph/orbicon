import mgp
import json


def json_print(data):
    print(json.dumps(data, indent=4, sort_keys=True))


def dumps_utf8(obj):
    return json.dumps(obj).encode('utf-8')


class JsonDataAccessor(object):
    def __init__(self, data):
        self._data = data

    def take_n(self, *args):
        data = self._data
        for arg in args:
            if arg not in data:
                return None
            data = data[arg]
        return data


def take_type_from_array(array, item_type):
    for item in array:
        if "type" not in item:
            continue
        if item["type"] == item_type:
            return item


@mgp.transformation
def kafka2graph_transform(
    messages: mgp.Messages,
) -> mgp.Record(query=str, parameters=mgp.Nullable[mgp.Map]):
    queries = []

    for i in range(messages.total_messages()):
        # TODO(gitbuda): Figure out different message types.
        message_str = messages.message_at(i).payload().decode("utf-8")
        # For some reason the payload is wrapped twice.
        payload = json.loads(json.loads(message_str)["event_payload"])["event_payload"]
        accessor = JsonDataAccessor(payload)
        member_id = accessor.take_n("data", "relationships", "member", "data", "id")
        included = accessor.take_n("included")
        # TODO(gitbuda): If something fails stream is stopped.
        print(member_id)
        print(take_type_from_array(included, "member"))
        print(dumps_utf8(take_type_from_array(included, "twitter_identity")))
        print(dumps_utf8(take_type_from_array(included, "github_identity")))
        queries.append(
            mgp.Record(
                query="CREATE (:Test {id: $i});",
                parameters={
                    "i": i}))

    return queries
