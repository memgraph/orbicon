import mgp
import kmeans

NUMBER_OF_GROUPS = 5

@mgp.read_proc
def get_labels(ctx: mgp.ProcCtx, nodes: mgp.List[mgp.Vertex], embeddings: mgp.List[mgp.List[mgp.Number]]) -> mgp.Record(
    node=mgp.Vertex, label=mgp.Number):
    nodes_new = []
    for node in nodes:
        nodes_new.append(node)

    embeddings_new = []
    for embedding in embeddings:
        embeddings_new.append([float(e) for e in embedding])

    for i in range(len(nodes_new)):
        print(nodes_new[i], embeddings_new[i])

    dict, nodes_labels_list = kmeans.get_groups(NUMBER_OF_GROUPS, embeddings_new, nodes_new)

    return [
        mgp.Record(node=node, label=int(label))
        for node, label in nodes_labels_list
    ]
