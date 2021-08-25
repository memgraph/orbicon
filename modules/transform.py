import mgp


@mgp.transformation
def kafka2graph_transform(
    messages: mgp.Messages,
) -> mgp.Record(query=str, parameters=mgp.Nullable[mgp.Map]):
    return []
