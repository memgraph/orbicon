# Memgraph Query Modules

## ETL

Please ensure Memgraph has correctly loaded the transform script by running the following query:

```Cypher
CALL mg.transformations() YIELD *;
```

Once the transform script is loaded, please create the stream:

```Cypher
CREATE STREAM orbitStream
TOPICS orbit-events
TRANSFORM transform.kafka2graph_transform;
```

To start the stream, the following has to be executed:

```Cypher
START STREAM orbitStream;
```

To see the stream status run:

```Cypher
SHOW STREAMS;
```

## Algorithms

Before any edge is added to graph, we need to initialize `node2vec_online` module

```Cypher
CALL node2vec_online.set_streamwalk_updater() YIELD *;
```

```Cypher
CALL node2vec_online.set_word2vec_learner(4,0.01,True,10) YIELD *;
```

After that part is done, we can create triggers. We need to create one trigger.
This one is for `orbit_graph_calculus module` to update `communityId`.

```Cypher
CREATE TRIGGER orbit_graph_calculus_set_lables ON --> CREATE AFTER COMMIT
EXECUTE CALL node2vec_online.update(createdEdges) YIELD *
WITH 1 as x
CALL node2vec_online.get() YIELD node,embedding
WITH COLLECT(node) as nodes, COLLECT(embedding) as embeddings
CALL orbit_graph_calculus.get_labels(nodes,embeddings) YIELD node,label
SET node.communityId=label;
```
