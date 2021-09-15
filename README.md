<h1 align="center">
  Orbicon
</h1>
<h2 align="center">
  🔍 Explore Your Community 🧑
</h2>

<p align="center">
  <a href="https://github.com/memgraph/orbicon/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/memgraph/orbicon" alt="license" title="license"/>
  </a>
  <a href="https://github.com/memgraph/orbicon">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="build" title="build"/>
  </a>
  <a href="#contributors-">
    <img src="https://img.shields.io/badge/all_contributors-3-green.svg?style=flat" />
  </a>
</p>

<p align="center">
    <a href="https://twitter.com/intent/follow?screen_name=memgraphdb"><img
    src="https://img.shields.io/twitter/follow/memgraphdb.svg?label=Follow%20@memgraphdb"
    alt="Follow @memgraphdb" /></a>
</p>

<p align="center">
  <a href="https://github.com/memgraph/orbicon">
    <img src="https://public-assets.memgraph.com/github-readme-images/orbicon-01.png" 
         alt="orbit_and_memgraph" 
         title="orbit_and_memgraph"
         style="width: 80%"/>
  </a>
</p>

**Orbicon** is a centralized place where you can find anything about your
developer community. **[Orbit](https://orbit.love)** aggregates all sorts of
different events coming from the community, while
**[Memgraph](https://memgraph.com)** enriches the data and provides advanced
insights based on incremental graph algorithms.

Orbit provides the **Love** metric, which indicates how much a given community
member loves your brand. In addition to data coming from Orbit, Memgraph scrapes
social graph data from Github and Twitter. Based on these social networks,
Memgraph constructs an entirely new membership graph. Memgraph then analyzes
this membership graph by applying the following graph algorithms:

* **[PageRank](https://memgraph.com/blog/influencers-among-computer-scientists)**:
  This algorithm tells us how important each member is.
* **[Community
  Detection](https://memgraph.com/blog/community_detection-algorithms_with_python_networkx)**:
  This algorithm reveals deeper insights about the network structure and
  possible sub-communities.

## 📚 Data model

<img
         src="https://user-images.githubusercontent.com/4950251/132960622-c5ebe0b6-1cd5-46d7-9791-67e252aa67d8.png"
         alt="reddit-network-explorer" title="reddit-network-explorer"
         style="width: 80%"/>
    
## 👉 Try it out!

* The demo application - **[orbit.memgraph.com](http://orbit.memgraph.com/)**
* The Memgraph instance - **bolt://orbit.memgraph.com:7687**

To explore the data, please download [Memgraph
Lab](https://memgraph.com/product/lab). The endpoint is `orbit.memgraph.com` and
the port is `7687`.

## 🖥️ Run the app locally

### Running the backend service

The first thing to do in the root directory is to create a Python virtual
environment:
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

Position yourself in the frontend directory, install the dependencies with *npm*
and run using the following commands:
```
cd frontend
npm install
npm run serve
```

## ❔ Find out more about Memgraph

Memgraph makes creating real-time streaming graph applications accessible to
every developer. Spin up an instance, consume data directly from Kafka, and
build on top of everything from super-fast graph queries to PageRank and
Community Detection.
* [Memgraph Docs](https://docs.memgraph.com)
* [Memgraph Download](https://memgraph.com/download)

## Contributors ✨

Thanks goes to these wonderful people ([emoji
key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Josipmrden"><img src="https://avatars.githubusercontent.com/u/22621791?v=4" width="100px;" alt=""/><br /><sub><b>Josip Mrden</b></sub></a></td>
    <td align="center"><a href="https://github.com/gitbuda"><img src="https://avatars.githubusercontent.com/u/4950251?v=4" width="100px;" alt=""/><br /><sub><b>Marko Budiselic</b></sub></a></td>
    <td align="center"><a href="https://github.com/antoniofilipovic"><img src="https://avatars.githubusercontent.com/u/61245998?v=4" width="100px;" alt=""/><br /><sub><b>Antonio Filipovic
</b></sub></a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the
[all-contributors](https://github.com/all-contributors/all-contributors)
specification. Contributions of any kind welcome!
