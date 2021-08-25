# Memgraph Query Modules

```Cypher
CALL mg.transformations() YIELD *;
```

```Cypher
CREATE STREAM orbitStream
TOPICS orbit-events
TRANSFORM transform.kafka2graph_transform;
```
