from abc import ABC, abstractmethod
from typing import Iterable, Dict
from src.enums import IndexType, IndexState
from src.node_layout import IndexEntry
from src.metadata import IndexMetadata
from src.tree_operations import BTreeEngine

class IIndexLifecycleManager(ABC):
    @abstractmethod
    def create_index(self, metadata: IndexMetadata) -> bool: pass
    @abstractmethod
    def drop_index(self, index_id: int) -> bool: pass
    @abstractmethod
    def rebuild_index(self, index_id: int) -> bool: pass
    @abstractmethod
    def bulk_load(self, index_id: int, entries: Iterable[IndexEntry]) -> bool: pass
    @abstractmethod
    def validate_index(self, index_id: int) -> bool: pass

class BTreeLifecycleManager(IIndexLifecycleManager):
    def __init__(self, engine: BTreeEngine, metadata_directory: Dict[int, IndexMetadata] = None):
        self._engine = engine
        self._metadata_directory = metadata_directory if metadata_directory is not None else {}

    def create_index(self, metadata: IndexMetadata) -> bool:
        raise NotImplementedError("TDD Stub")

    def drop_index(self, index_id: int) -> bool:
        raise NotImplementedError("TDD Stub")

    def rebuild_index(self, index_id: int) -> bool:
        raise NotImplementedError("TDD Stub")

    def bulk_load(self, index_id: int, entries: Iterable[IndexEntry]) -> bool:
        raise NotImplementedError("TDD Stub")

    def validate_index(self, index_id: int) -> bool:
        raise NotImplementedError("TDD Stub")
