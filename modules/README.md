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
