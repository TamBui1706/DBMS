from DBMS.Classes.DatabaseObjectManagement.metadata_node import MetadataNode

class Column(MetadataNode):
    def __init__(self, name: str = None, type: str = None):
        self.name = name
        self.type = type
        self.nullable = True

    def get_metadata(self) -> dict:
        return {
            "type": "Column",
            "name": self.name,
            "col_type": self.type
        }
