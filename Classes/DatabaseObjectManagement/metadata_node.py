from abc import ABC, abstractmethod

class MetadataNode(ABC):
    """
    Component interface for the Composite Pattern.
    All database objects (Database, Schema, Table, Column, Constraint) must implement this.
    """
    @abstractmethod
    def get_metadata(self) -> dict:
        pass
