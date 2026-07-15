from abc import ABC, abstractmethod
from typing import Any
from src.node_layout import LeafNode
from src.tree_operations import BTreeEngine

class IIndexMaintenance(ABC):
    @abstractmethod
    def vacuum(self, index_id: int) -> int: pass
    @abstractmethod
    def compress_nodes(self, node: LeafNode) -> None: pass

class IndexVacuumWorker(IIndexMaintenance):
    def __init__(self, engine: BTreeEngine, lifecycle_manager: Any = None):
        self._engine = engine
        self._lifecycle_manager = lifecycle_manager

    def vacuum(self, index_id: int) -> int:
        raise NotImplementedError("TDD Stub")

    def compress_nodes(self, node: LeafNode) -> None:
        raise NotImplementedError("TDD Stub")
