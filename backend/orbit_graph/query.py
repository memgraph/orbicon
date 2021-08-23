from collections.abc import Iterator
from typing import Any

from orbit_graph.database import Memgraph


def query(command: str) -> Iterator[dict[str, Any]]:
    """Queries Memgraph database and returns iterator of results"""
    db = Memgraph()
    yield from db.execute_and_fetch(command)
