from abc import ABC, abstractmethod
from typing import Any, List, Iterator, Dict
from src.enums import ScanDirection, LatchMode
from src.node_layout import RecordID, IndexEntry, BTreeNode, LeafNode
from src.key_evaluator import IKeyComparator
from src.concurrency_control import IIndexConcurrencyManager
from src.tree_operations import BTreeEngine

class IIndexAccessMethod(ABC):
    @abstractmethod
    def point_search(self, key: Any) -> List[RecordID]: pass
    @abstractmethod
    def range_scan(self, start_key: Any, end_key: Any, direction: ScanDirection) -> Iterator[IndexEntry]: pass
    @abstractmethod
    def insert(self, key: Any, rid: RecordID) -> bool: pass
    @abstractmethod
    def delete(self, key: Any, rid: RecordID) -> bool: pass
    @abstractmethod
    def update(self, old_key: Any, new_key: Any, rid: RecordID) -> bool: pass

class RangeIterator(Iterator[IndexEntry]):
    def __init__(self, 
                 starting_leaf: LeafNode, 
                 start_key: Any, 
                 end_key: Any, 
                 direction: ScanDirection,
                 concurrency_manager: IIndexConcurrencyManager,
                 key_comparator: IKeyComparator,
                 page_directory: Dict[int, Any]):
        self._current_leaf = starting_leaf
        self._start_key = start_key
        self._end_key = end_key
        self._direction = direction
        self._concurrency = concurrency_manager
        self._comparator = key_comparator
        self._page_directory = page_directory
        self._current_idx = 0

    def __next__(self) -> IndexEntry:
        raise NotImplementedError("TDD Stub")

class BTreeAccessMethod(IIndexAccessMethod):
    def __init__(self, metadata: Any, engine: BTreeEngine):
        self._metadata = metadata
        self._engine = engine

    def point_search(self, key: Any) -> List[RecordID]:
        raise NotImplementedError("TDD Stub")

    def range_scan(self, start_key: Any, end_key: Any, direction: ScanDirection = ScanDirection.FORWARD) -> Iterator[IndexEntry]:
        raise NotImplementedError("TDD Stub")

    def insert(self, key: Any, rid: RecordID) -> bool:
        raise NotImplementedError("TDD Stub")

    def delete(self, key: Any, rid: RecordID) -> bool:
        raise NotImplementedError("TDD Stub")

    def update(self, old_key: Any, new_key: Any, rid: RecordID) -> bool:
        raise NotImplementedError("TDD Stub")
