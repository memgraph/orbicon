from abc import ABC, abstractmethod


class NodeAbstract(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_node_cypher(self):
        pass
