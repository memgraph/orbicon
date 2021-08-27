
Create Github member connections

```Cypher
MATCH (n:Member)-[:HAS]->(m:Github), (n1:Member)-[:HAS]->(m1:Github), (m)-[:FOLLOWS]->(m1)
WHERE n.username != n1.username
MERGE (n)-[:CONNECTS]->(n1);
```


Create Twitter member connections


```Cypher
MATCH (n:Member)-[:HAS]->(m:Twitter), (n1:Member)-[:HAS]->(m1:Twitter), (m)-[:FOLLOWS]-(m1)
WHERE n.username != n1.username
MERGE (n)-[:CONNECTS]->(n1);
```