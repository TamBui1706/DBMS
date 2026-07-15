# Index Management Subsystem - Optimistic Read Strategy Flow

The Optimistic Read strategy helps accelerate multi-threaded queries on the index by eliminating the need to continuously acquire Read Latches on the upper nodes of the B+ Tree.

---

## 1. Scenario A: Optimistic Success

* **Description:** A Reader traverses a node without any Writer modifying that node simultaneously. The Reader reads the version number before and after reading the node's data; if they match, the data is considered consistent. No latch needs to be acquired on that node.

### Sequence Diagram:
```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant BE as BTreeEngine
    participant Node as BTreeNode

    Client->>BE: search_optimistic(root_page_id, key)
    activate BE

    BE->>Node: Read the first version number (initial_version) from NodeHeader
    activate Node
    Node-->>BE: initial_version
    deactivate Node

    BE->>Node: Read keys data and child_page_id
    activate Node
    Node-->>BE: keys, child_page_id
    deactivate Node

    BE->>Node: Read the second version number (final_version)
    activate Node
    Node-->>BE: final_version
    deactivate Node

    note over BE: Validation: initial_version == final_version (Success)
    BE-->>Client: child_page_id (Safe read without latch)
    deactivate BE
```

---

## 2. Scenario B: Optimistic Failure & Fallback to Pessimistic Latch

* **Description:** While the Reader is reading the node's keys, a Writer thread concurrently performs an insert/delete operation on this node and alters the node's version number. Upon the second check, the Reader detects the version mismatch and considers the read data inconsistent. The system will automatically fall back to the standard Read Latch mode on that node to safely re-read the data.

### Sequence Diagram:
```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant BE as BTreeEngine
    participant Node as BTreeNode
    participant LCM as LockCrabbingManager

    Client->>BE: search_optimistic(root_page_id, key)
    activate BE

    BE->>Node: Read the first version number (initial_version) from NodeHeader
    activate Node
    Node-->>BE: initial_version
    deactivate Node

    BE->>Node: Read keys data and child_page_id
    activate Node
    Node-->>BE: keys, child_page_id
    deactivate Node

    BE->>Node: Read the second version number (final_version)
    activate Node
    Node-->>BE: final_version (Version Mismatch Detected!)
    deactivate Node

    note over BE: Validation failed: initial_version != final_version. Fallback to Pessimistic Latch
    
    BE->>LCM: acquire_latch(node, LatchMode.READ)
    activate LCM
    LCM-->>BE: success
    deactivate LCM
    
    BE->>Node: Re-read keys data and child_page_id (safe under read latch)
    activate Node
    Node-->>BE: keys, child_page_id
    deactivate Node
    
    BE->>LCM: release_latch(node)
    activate LCM
    LCM-->>BE: success
    deactivate LCM
    
    BE-->>Client: child_page_id
    deactivate BE
```
