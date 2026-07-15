# Index Management Subsystem - Access Methods

This component provides the main API interface for the end-user or Query Optimizer to interact with the index, performing operations: Point Search, Range Scan, Insert, Delete, and Update.

---

## 1. Sub-Class Diagram

```mermaid
classDiagram
    %% --- ENUM ---
    class ScanDirection {
        <<enumeration>>
        FORWARD
        BACKWARD
    }

    %% --- ENTITIES ---
    class RecordID {
        +int page_id
        +int slot_id
    }

    class IndexEntry {
        +Any key
        +RecordID rid
        +bool is_deleted
    }

    class IndexMetadata {
        +int index_id
        +str name
        +int table_id
        +List~int~ column_ids
        +IndexType index_type
        +bool is_unique
        +int root_page_id
        +IndexState state
        +int tree_height
        +int node_count
        +int key_count
    }

    class LeafNode {
        +List~RecordID~ record_ids
        +int next_page_id
        +int prev_page_id
        +lookup(key: Any, comparator: IKeyComparator) List~RecordID~
        +insert(key: Any, rid: RecordID, comparator: IKeyComparator) bool
        +delete(key: Any, rid: RecordID, comparator: IKeyComparator) bool
        +split() Tuple~Any_BTreeNode~
    }

    %% --- INTERFACES ---
    class IIndexAccessMethod {
        <<interface>>
        +point_search(key: Any) List~RecordID~
        +range_scan(start_key: Any, end_key: Any, direction: ScanDirection) Iterator~IndexEntry~
        +insert(key: Any, rid: RecordID) bool
        +delete(key: Any, rid: RecordID) bool
        +update(old_key: Any, new_key: Any, rid: RecordID) bool
    }

    class IBTreeEngine {
        <<interface>>
        +search(root_page_id: int, key: Any) LeafNode
        +search_optimistic(root_page_id: int, key: Any) int
        +insert(root_page_id: int, key: Any, rid: RecordID) bool
        +delete(root_page_id: int, key: Any, rid: RecordID) bool
        +bulk_load_build(entries: Iterable~IndexEntry~) int
    }

    %% --- IMPLEMENTATIONS ---
    class BTreeAccessMethod {
        -IndexMetadata _metadata
        -IBTreeEngine _engine
        +point_search(key: Any) List~RecordID~
        +range_scan(start_key: Any, end_key: Any, direction: ScanDirection) Iterator~IndexEntry~
        +insert(key: Any, rid: RecordID) bool
        +delete(key: Any, rid: RecordID) bool
        +update(old_key: Any, new_key: Any, rid: RecordID) bool
    }

    class RangeIterator {
        -LeafNode _current_leaf
        -Any _start_key
        -Any _end_key
        -ScanDirection _direction
        -int _current_idx
        -IIndexConcurrencyManager _concurrency_manager
        -IKeyComparator _key_comparator
        +__next__() IndexEntry
        -_move_to_next_leaf() bool
    }

    %% --- RELATIONSHIPS ---
    IIndexAccessMethod <|.. BTreeAccessMethod : implements
    BTreeAccessMethod --> IBTreeEngine : uses
    BTreeAccessMethod --> IndexMetadata : uses
    BTreeAccessMethod ..> RangeIterator : creates
    RangeIterator --> ScanDirection : uses
    RangeIterator --> IndexEntry : yields
    RangeIterator --> LeafNode : references current
    IndexEntry --> RecordID : references
```

---

## 2. Python Skeleton Specification

```python
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Any, List, Iterator

class ScanDirection(Enum):
    FORWARD = auto()
    BACKWARD = auto()

class RecordID:
    def __init__(self, page_id: int, slot_id: int):
        self.page_id: int = page_id
        self.slot_id: int = slot_id

class IndexEntry:
    def __init__(self, key: Any, rid: RecordID, is_deleted: bool = False):
        self.key: Any = key
        self.rid: RecordID = rid
        self.is_deleted: bool = is_deleted

class IIndexAccessMethod(ABC):
    @abstractmethod
    def point_search(self, key: Any) -> List[RecordID]:
        """Search for a specific key, return the corresponding list of RecordIDs."""
        pass

    @abstractmethod
    def range_scan(self, start_key: Any, end_key: Any, direction: ScanDirection) -> Iterator[IndexEntry]:
        """Return an Iterator to scan through a range of data keys."""
        pass

    @abstractmethod
    def insert(self, key: Any, rid: RecordID) -> bool:
        """Insert a new index record (key -> RecordID)."""
        pass

    @abstractmethod
    def delete(self, key: Any, rid: RecordID) -> bool:
        """Delete an index record."""
        pass

    @abstractmethod
    def update(self, old_key: Any, new_key: Any, rid: RecordID) -> bool:
        """Update an index record (delete old_key, insert new_key)."""
        pass

class BTreeAccessMethod(IIndexAccessMethod):
    def __init__(self, metadata: 'IndexMetadata', engine: 'IBTreeEngine'):
        self._metadata = metadata
        self._engine = engine

    def point_search(self, key: Any) -> List[RecordID]:
        pass

    def range_scan(self, start_key: Any, end_key: Any, direction: ScanDirection) -> Iterator[IndexEntry]:
        pass

    def insert(self, key: Any, rid: RecordID) -> bool:
        pass

    def delete(self, key: Any, rid: RecordID) -> bool:
        pass

    def update(self, old_key: Any, new_key: Any, rid: RecordID) -> bool:
        pass

class RangeIterator(Iterator[IndexEntry]):
    def __init__(self, 
                 starting_leaf: 'LeafNode', 
                 start_key: Any, 
                 end_key: Any, 
                 direction: ScanDirection,
                 concurrency_manager: 'IIndexConcurrencyManager',
                 key_comparator: 'IKeyComparator'):
        self._current_leaf = starting_leaf
        self._start_key = start_key
        self._end_key = end_key
        self._direction = direction
        self._concurrency_manager = concurrency_manager
        self._key_comparator = key_comparator
        self._current_idx = 0

    def __next__(self) -> IndexEntry:
        pass

    def _move_to_next_leaf(self) -> bool:
        pass
```
