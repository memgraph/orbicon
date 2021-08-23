"""
orbit_graph

Usage:
    main.py hello NAME
    main.py query CYPHER
    main.py -h | --help

Arguments:
    -h --help   Shows this screen.
    NAME        Set name to print out
"""

import logging
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return _hello("Memgraph!")

logging.basicConfig(format="%(asctime)-15s [%(levelname)s]: %(message)s")
logger = logging.getLogger("orbit_graph")
logger.setLevel(logging.INFO)


def _hello(name: str) -> None:
    from orbit_graph import hello

    return hello(name)


def _query(command: str) -> None:
    from orbit_graph import query

    for result in query(command):
        print(result)


