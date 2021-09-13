<h1 align="center">
  Orbicon
</h1>
<h2 align="center">
  🔍 Explore Your Community 🧑
</h2>

<p align="center">
  <a href="https://github.com/memgraph/orbicon/LICENSE">
    <img src="https://img.shields.io/github/license/memgraph/orbicon" alt="license" title="license"/>
  </a>
  <a href="https://github.com/memgraph/orbicon">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="build" title="build"/>
  </a>
  <a href="https://github.com/memgraph/orbicon/stargazers">
    <img src="https://img.shields.io/badge/maintainer-Josipmrden-yellow" alt="maintainer" title="maintainer"/>
  </a>
</p>

<p align="center">
    <a href="https://twitter.com/intent/follow?screen_name=memgraphdb"><img
    src="https://img.shields.io/twitter/follow/memgraphdb.svg?label=Follow%20@memgraphdb"
    alt="Follow @memgraphdb" /></a>
</p>

<p align="center">
  <a href="https://github.com/memgraph/orbicon">
    <img src="https://user-images.githubusercontent.com/4950251/131040062-d2df128e-423b-490d-b357-0c95004587c7.png" alt="orbit_and_memgraph" title="orbit_and_memgraph"/>
  </a>
</p>

**Orbicon** is a centralized place where you can find anything about your developer community. **[Orbit](https://orbit.love)** aggregates all sorts of different events coming from the community, while **[Memgraph](https://memgraph.com)** enriches the data and provides advanced insights based on incremental graph algorithms.

Orbit provides the **Love** metric, which indicates how much a given community member loves your brand. In addition to data coming from Orbit, Memgraph scrapes social graph data from Github and Twitter. Based on these social networks, Memgraph constructs an entirely new membership graph. Memgraph then analyzes this membership graph by applying the following graph algorithms:

* **[PageRank](https://memgraph.com/blog/influencers-among-computer-scientists)**: This algorithm tells us how important each member is.
* **[Community Detection](https://memgraph.com/blog/community_detection-algorithms_with_python_networkx)**: This algorithm reveals deeper insights about the network structure and possible sub-communities.

## 📚 Data model

![orbicon_data_model](https://user-images.githubusercontent.com/4950251/132960622-c5ebe0b6-1cd5-46d7-9791-67e252aa67d8.png)

## 👉 Try it out!

* The demo application - **[orbit.memgraph.com](http://orbit.memgraph.com/)**
* The Memgraph instance - **bolt://orbit.memgraph.com:7687**

To explore the data, please download [Memgraph Lab](https://memgraph.com/product/lab) or visit [lab.memgraph.com](https://lab.memgraph.com/login). The endpoint is `orbit.memgraph.com` and the port is '7687'.

## 🖥️ Run the app locally

### Running the backend service

The first thing to do in the root directory is to create a Python virtual environment:
```
python3 -m venv .venv
source .venv/bin/activate
```

After that, install all the dependencies with `Poetry`:
```
cd backend
poetry install
```

Finally, start the backend service with:
```
python3 main.py
```

### Running the frontend service

Position yourself in the frontend directory, install the dependencies with *npm* and run using the following commands:
```
cd frontend
npm install
npm run serve
```

## ❔ Find out more about Memgraph

Memgraph makes creating real-time streaming graph applications accessible to every developer. Spin up an instance, consume data directly from Kafka, and build on top of everything from super-fast graph queries to PageRank and Community Detection.
* [Memgraph Docs](https://docs.memgraph.com)
* [Memgraph Download](https://memgraph.com/download)
