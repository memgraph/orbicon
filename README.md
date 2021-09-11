# 🔍 Explore Your Community - Orbicon 🧑

![orbit_and_memgraph](https://user-images.githubusercontent.com/4950251/131040062-d2df128e-423b-490d-b357-0c95004587c7.png)

**Orbicon** is a centralized place where you can find anything about your developer community. [Orbit](https://orbit.love) aggregates all sorts of different events comming from the community, while [Memgraph](https://memgraph.com) enriches data and provides advanced insights based on incremental graph algorithms.

Orbit provides the **Love** metric, which tells how much a given community member loves your brand. In addition to data coming from Orbit, Memgraph scrapes social graph data from Github and Twitter. Based on these social networks, Memgraph constructs an entirely new membership graph. Memgraph then analyzes the membership graph by applying the following graph algorithms:

* [PageRank](https://memgraph.com/blog/influencers-among-computer-scientists) telling how important a member is
* [Community Detection](https://memgraph.com/blog/community_detection-algorithms_with_python_networkx) revealing deeper insights about sub-communities

## Data Model

![orbicon_data_model](https://user-images.githubusercontent.com/4950251/132960622-c5ebe0b6-1cd5-46d7-9791-67e252aa67d8.png)

## Try It Out!

* [Portal](http://orbit.memgraph.com/)
* Data - **bolt://orbit.memgraph.com:7687** (to explore, please download [Memgraph Lab](https://memgraph.com/product/lab))

## Find out More About Memgraph

* [Memgraph Docs](https://docs.memgraph.com)
* [Memgraph Download](https://memgraph.com/download)
