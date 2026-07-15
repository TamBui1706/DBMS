from typing import Any, Dict, Iterable
from src.enums import NodeType, LatchMode
from src.node_layout import BTreeNode, InternalNode, LeafNode, NodeHeader, RecordID, IndexEntry
from src.key_evaluator import IKeyComparator
from src.concurrency_control import IIndexConcurrencyManager

class SplitCoordinator:
    def coordinate_split(self, parent: InternalNode, child: BTreeNode) -> bool:
        raise NotImplementedError("TDD Stub")

class MergeRedistributeManager:
    def coordinate_merge_or_redistribute(self, parent: InternalNode, child: BTreeNode) -> bool:
        raise NotImplementedError("TDD Stub")

class BTreeEngine:
    def __init__(self, 
                 split_coordinator: SplitCoordinator, 
                 merge_coordinator: MergeRedistributeManager,
                 key_comparator: IKeyComparator,
                 concurrency_manager: IIndexConcurrencyManager):
        self._split_coordinator = split_coordinator
        self._merge_coordinator = merge_coordinator
        self._key_comparator = key_comparator
        self._concurrency_manager = concurrency_manager
        self.pages: Dict[int, BTreeNode] = {}
        self.next_page_id = 1
        self.max_capacity = 3
        self.min_capacity = 1
        self.root_override = -1

    def allocate_leaf(self) -> LeafNode:
        raise NotImplementedError("TDD Stub")

    def allocate_internal(self) -> InternalNode:
        raise NotImplementedError("TDD Stub")

    def _traverse(self, root_page_id: int, key: Any, latch_mode: LatchMode) -> BTreeNode:
        raise NotImplementedError("TDD Stub")

    def search(self, root_page_id: int, key: Any) -> LeafNode:
        raise NotImplementedError("TDD Stub")

    def search_optimistic(self, root_page_id: int, key: Any) -> int:
        raise NotImplementedError("TDD Stub")

    def insert(self, root_page_id: int, key: Any, rid: RecordID) -> bool:
        raise NotImplementedError("TDD Stub")

    def delete(self, root_page_id: int, key: Any, rid: RecordID) -> bool:
        raise NotImplementedError("TDD Stub")

    def bulk_load_build(self, entries: Iterable[IndexEntry]) -> int:
        raise NotImplementedError("TDD Stub")
