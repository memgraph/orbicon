# Memgraph Query Modules

```Cypher
CALL mg.transformations() YIELD *;
```

```Cypher
CREATE STREAM orbitStream
TOPICS orbit-events
TRANSFORM transform.kafka2graph_transform;
```

##Algorithms

Before any edge is added to graph, we need to initialize `node2vec_online` module

```Cypher
CALL node2vec_online.set_streamwalk_updater() YIELD *;
```

```Cypher
CALL node2vec_online.set_word2vec_learner(4,0.01,True,10) YIELD *;
```

After that part is done, we can create triggers. We need to have two triggers.
First one is for node2vec_online module embedding calculation.

```Cypher
CREATE TRIGGER node2vec_update_embedding ON --> CREATE BEFORE COMMIT
EXECUTE CALL node2vec_online.update(createdEdges) YIELD *;
```

Second one is for `orbit_graph_calculus module` to update `communityId`

```Cypher
CREATE TRIGGER orbit_graph_calculus_set_lables ON --> CREATE AFTER COMMIT
EXECUTE CALL node2vec_online.get() YIELD node,embedding 
WITH COLLECT(node) as nodes, COLLECT(embedding) as embeddings 
CALL orbit_graph_calculus.get_labels(nodes,embeddings) YIELD node,label
SET node.communityId=label;
```
