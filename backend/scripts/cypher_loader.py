"""
Loads Cypher commands to Memgraph

Cypher file should have a Cypher command per line

Usage:
    cypher_loader.py CYPHER_FILE
    cypher_loader.py -h | --help

Arguments:
    -h --help   Show this screen
"""

import logging
from collections.abc import Iterator
from typing import Any, Optional

logging.basicConfig(format="%(asctime)-15s [%(levelname)s]: %(message)s")
logger = logging.getLogger("cypher_loader")
logger.setLevel(logging.INFO)


def load(cypher_stream: Iterator[str], total_count: Optional[int] = None) -> None:
    from orbit_graph.database import Memgraph

    db = Memgraph()

    one_percentage: Optional[int] = None
    if total_count:
        one_percentage = int(round(total_count / 100, 0)) if total_count > 100 else 1

        for index, cypher_command in enumerate(cypher_stream):
            db.execute_query(cypher_command)
            if one_percentage and index % one_percentage == 0:
                percentage: int = int(round((index + 1) * 100 / total_count, 0))
                logger.info(f"Loading progress: [{percentage:2}%] {index + 1}/{total_count} commands")


def _get_file_line_count(filename: str) -> int:
    logger.info(f"Counting number of lines in files {filename}...")
    with open(filename) as f:
        return sum(1 for _ in f)


def main(args: dict[str, Any]) -> None:
    filename = args["CYPHER_FILE"]
    line_count = _get_file_line_count(filename)

    with open(filename) as f:
        logger.info(f"Started loading cypher commands from file {filename}...")
        load(f, total_count=line_count)


if __name__ == "__main__":
    from docopt import docopt

    main(docopt(__doc__))
