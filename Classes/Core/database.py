from typing import List
from Classes.DatabaseObjectManagement.metadata_node import MetadataNode

class Database(MetadataNode):
    def __init__(self, name: str = None):
        self.name = name
        self.children: List[MetadataNode] = []

    def open(self):
        pass

    def add_child(self, node: MetadataNode):
        self.children.append(node)

    def get_metadata(self) -> dict:
        return {
            "type": "Database",
            "name": self.name,
            "children": [child.get_metadata() for child in self.children]
        }
