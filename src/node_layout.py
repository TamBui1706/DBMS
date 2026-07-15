from typing import Any, List, Tuple
from src.enums import NodeType
from src.key_evaluator import IKeyComparator

class RecordID:
    def __init__(self, page_id: int, slot_id: int):
        self.page_id = page_id
        self.slot_id = slot_id

    def __eq__(self, other: Any) -> bool:
        raise NotImplementedError("TDD Stub")

    def __repr__(self) -> str:
        raise NotImplementedError("TDD Stub")

class IndexEntry:
    def __init__(self, key: Any, rid: RecordID, is_deleted: bool = False):
        self.key = key
        self.rid = rid
        self.is_deleted = is_deleted

    def __repr__(self) -> str:
        raise NotImplementedError("TDD Stub")

class NodeHeader:
    def __init__(self, level: int = 0, key_count: int = 0, lsn: int = 0, free_space: int = 4096):
        self.level = level
        self.key_count = key_count
        self.lsn = lsn
        self.free_space = free_space
        self.version = 1

class BTreeNode:
    def __init__(self, page_id: int, node_type: NodeType, header: NodeHeader):
        self.page_id = page_id
        self.header = header
        self.node_type = node_type
        self.keys: List[Any] = []

    def is_leaf(self) -> bool:
        raise NotImplementedError("TDD Stub")

    def is_overflow(self, max_capacity: int) -> bool:
        raise NotImplementedError("TDD Stub")

    def is_underflow(self, min_capacity: int) -> bool:
        raise NotImplementedError("TDD Stub")

class InternalNode(BTreeNode):
    def __init__(self, page_id: int, header: NodeHeader):
        super().__init__(page_id, NodeType.INTERNAL, header)
        self.children_page_ids: List[int] = []

    def lookup(self, key: Any, comparator: IKeyComparator) -> int:
        raise NotImplementedError("TDD Stub")

    def insert(self, key: Any, child_page_id: int) -> None:
        raise NotImplementedError("TDD Stub")

    def split(self) -> Tuple[Any, BTreeNode]:
        raise NotImplementedError("TDD Stub")

class LeafNode(BTreeNode):
    def __init__(self, page_id: int, header: NodeHeader, next_page_id: int = -1, prev_page_id: int = -1):
        super().__init__(page_id, NodeType.LEAF, header)
        self.record_ids: List[RecordID] = []
        self.next_page_id = next_page_id
        self.prev_page_id = prev_page_id
        self.entries: List[IndexEntry] = []

    def lookup(self, key: Any, comparator: IKeyComparator) -> List[RecordID]:
        raise NotImplementedError("TDD Stub")

    def insert(self, key: Any, rid: RecordID, comparator: IKeyComparator) -> bool:
        raise NotImplementedError("TDD Stub")

    def delete(self, key: Any, rid: RecordID, comparator: IKeyComparator) -> bool:
        raise NotImplementedError("TDD Stub")

    def split(self) -> Tuple[Any, BTreeNode]:
        raise NotImplementedError("TDD Stub")
