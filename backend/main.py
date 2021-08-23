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
import re
from typing import Any

logging.basicConfig(format="%(asctime)-15s [%(levelname)s]: %(message)s")
logger = logging.getLogger("orbit_graph")
logger.setLevel(logging.INFO)


def _hello(name: str) -> None:
    from orbit_graph import hello

    print(hello(name))


def _query(command: str) -> None:
    from orbit_graph import query

    for result in query(command):
        print(result)


def main(args: dict[str, Any]) -> None:
    if args["hello"]:
        return _hello(args["NAME"])

    if args["query"]:
        return _query(args["CYPHER"])


if __name__ == "__main__":
    from docopt import docopt

    args = docopt(__doc__)
    main(args)
