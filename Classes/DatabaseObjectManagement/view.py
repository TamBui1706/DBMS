from Classes.DatabaseObjectManagement.metadata_node import MetadataNode

class View(MetadataNode):
    def __init__(self, name: str = None, queryDefinition: str = None):
        self.name = name
        self.queryDefinition = queryDefinition

    def get_metadata(self) -> dict:
        return {
            "type": "View",
            "name": self.name,
            "query": self.queryDefinition
        }
