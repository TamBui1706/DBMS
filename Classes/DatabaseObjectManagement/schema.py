from typing import List
from DBMS.Classes.DatabaseObjectManagement.metadata_node import MetadataNode

class Schema(MetadataNode):
    def __init__(self, name: str = None):
        self.name = name
        self.children: List[MetadataNode] = []

    def createTable(self):
        pass

    def add_child(self, node: MetadataNode):
        self.children.append(node)

    def get_metadata(self) -> dict:
        return {
            "type": "Schema",
            "name": self.name,
            "children": [child.get_metadata() for child in self.children]
        }
