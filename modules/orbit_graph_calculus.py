import mgp
import networkx as nx

import kmeans
from mgp_networkx import PropertiesDictionary


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

    NUMBER_OF_GROUPS = 2

    if len(nodes_new)>100:
        NUMBER_OF_GROUPS=5

    dict, nodes_labels_list = kmeans.get_groups(NUMBER_OF_GROUPS, embeddings_new, nodes_new)

    return [
        mgp.Record(node=node, label=int(label))
        for node, label in nodes_labels_list
    ]


@mgp.read_proc
def pagerank(
    ctx: mgp.ProcCtx,
    vertices: mgp.List[mgp.Vertex],
    edges: mgp.List[mgp.Edge]
) -> mgp.Record(node=mgp.Vertex, rank=float):
    def to_properties_dictionary(prop):
        return None if prop is None else PropertiesDictionary(ctx, prop)

    alpha= 0.85
    personalization = None
    max_iter = 100
    tol = 1e-06
    nstart = None
    weight= "weight"
    dangling = None

    print(vertices)

    g = nx.DiGraph()
    g.add_nodes_from(vertices)
    g.add_edges_from([(edge.from_vertex, edge.to_vertex) for edge in edges])
    g.add_edges_from([(edge.from_vertex, edge.to_vertex) for edge in edges])

    pg = nx.pagerank(
        g,
        alpha=alpha,
        personalization=to_properties_dictionary(personalization),
        max_iter=max_iter,
        tol=tol,
        nstart=to_properties_dictionary(nstart),
        weight=weight,
        dangling=to_properties_dictionary(dangling),
    )

    return [mgp.Record(node=k, rank=v) for k, v in pg.items()]