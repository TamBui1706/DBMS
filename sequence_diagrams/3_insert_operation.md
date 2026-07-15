# Index Management Subsystem - Insert Flow (Insert Key & Node Split)

The flow to insert a new key into the B+ Tree requires locating the appropriate leaf page, verifying uniqueness (if it is a unique index), and handling recursive node splitting when the page overflows.

---

## 1. Scenario A: Leaf Node Has Free Space (No Split) - Happy Path

* **Description:** The target leaf node still has enough free space. The new key is inserted directly into the correct sorted position on the leaf page. No tree structure modification is needed.

### Sequence Diagram:
```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant AM as BTreeAccessMethod
    participant MD as IndexMetadata
    participant BE as BTreeEngine
    participant LCM as LockCrabbingManager
    participant Leaf as LeafNode

    Client->>AM: insert(key, rid)
    activate AM
    
    AM->>MD: get metadata info
    activate MD
    MD-->>AM: root_page_id, is_unique=False
    deactivate MD

    AM->>BE: insert(root_page_id, key, rid)
    activate BE

    BE->>BE: _traverse(root_page_id, key, LatchMode.WRITE)
    activate BE
    note over BE: Apply Write Lock Crabbing: Only release the parent node's latch if the child node is safe (not full)
    BE-->>BE: leaf_node (holds Write latch)
    deactivate BE

    BE->>Leaf: insert(key, rid, comparator)
    activate Leaf
    Leaf-->>BE: key_inserted
    deactivate Leaf

    note over BE: Leaf node does not overflow (has free space)
    BE->>LCM: release_all_latches()
    activate LCM
    LCM-->>BE: success
    deactivate LCM
    
    BE-->>AM: success
    deactivate BE
    AM-->>Client: success
    deactivate AM
```

---

## 2. Scenario B: Leaf Node Splits, Parent Safe (Leaf Split, Parent Safe)

* **Description:** The target leaf page is full (`key_count > max_capacity`). The system splits the leaf page into two (creates a new sibling leaf page, moves 50% of the keys to the new node, updates sibling links). The median key (`median_key`) is pushed up and inserted into the parent node (`InternalNode`). The parent node still has free space, so it accepts the new key without needing a further split.

### Sequence Diagram:
```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant AM as BTreeAccessMethod
    participant MD as IndexMetadata
    participant BE as BTreeEngine
    participant LCM as LockCrabbingManager
    participant Leaf as LeafNode
    participant Sibling as LeafNode (Sibling)
    participant SC as SplitCoordinator
    participant Parent as InternalNode

    Client->>AM: insert(key, rid)
    activate AM
    
    AM->>MD: get metadata info
    activate MD
    MD-->>AM: root_page_id, is_unique=False
    deactivate MD

    AM->>BE: insert(root_page_id, key, rid)
    activate BE

    BE->>BE: _traverse(root_page_id, key, LatchMode.WRITE)
    activate BE
    note over BE: Hold Write latches on parent node and leaf node since the leaf node may be full
    BE-->>BE: parent_node (Write Latched), leaf_node (Write Latched)
    deactivate BE

    BE->>Leaf: insert(key, rid, comparator)
    activate Leaf
    Leaf-->>BE: key_inserted (overflow detected)
    deactivate Leaf

    BE->>SC: coordinate_split(parent_node, leaf_node)
    activate SC
    
    SC->>Leaf: split()
    activate Leaf
    note over Leaf: Create SiblingLeaf, distribute 50% keys, link sibling pointers
    Leaf-->>SC: (median_key, sibling_leaf_node)
    deactivate Leaf
    
    SC->>Parent: insert(median_key, sibling_leaf_page_id)
    activate Parent
    note over Parent: Successfully insert the median key (Parent does not overflow)
    Parent-->>SC: success
    deactivate Parent
    
    SC-->>BE: split_completed
    deactivate SC
    
    BE->>LCM: release_all_latches()
    activate LCM
    LCM-->>BE: success
    deactivate LCM
    
    BE-->>AM: success
    deactivate BE
    AM-->>Client: success
    deactivate AM
```

---

## 3. Scenario C: Recursive Split to Root

* **Description:** The leaf node becomes full and splits, pushing the median key up to the parent node. The parent node also becomes full and must split and push further up. This process repeats until it reaches the root node. The root node splits, a new root node is created, and the index tree height increases by 1.

### Sequence Diagram:
```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant AM as BTreeAccessMethod
    participant MD as IndexMetadata
    participant BE as BTreeEngine
    participant LCM as LockCrabbingManager
    participant Leaf as LeafNode
    participant SC as SplitCoordinator
    participant Parent as InternalNode
    participant Root as InternalNode (Old Root)

    Client->>AM: insert(key, rid)
    activate AM
    
    AM->>MD: get metadata info
    activate MD
    MD-->>AM: root_page_id, is_unique=False
    deactivate MD

    AM->>BE: insert(root_page_id, key, rid)
    activate BE

    BE->>BE: _traverse(root_page_id, key, LatchMode.WRITE)
    activate BE
    note over BE: Hold write latch on all levels from root down to leaf because the entire path might split
    BE-->>BE: path_nodes (All Write Latched)
    deactivate BE

    BE->>Leaf: insert(key, rid, comparator)
    activate Leaf
    Leaf-->>BE: key_inserted (overflow detected)
    deactivate Leaf

    BE->>SC: coordinate_split(parent_node, leaf_node)
    activate SC
    
    SC->>Leaf: split()
    activate Leaf
    Leaf-->>SC: (median_key, sibling_leaf_node)
    deactivate Leaf
    
    SC->>Parent: insert(median_key, sibling_leaf_page_id)
    activate Parent
    note over Parent: Parent is full, proceed to split the parent node
    Parent-->>SC: parent_overflow_detected
    deactivate Parent

    SC->>Parent: split()
    activate Parent
    Parent-->>SC: (parent_median_key, sibling_parent)
    deactivate Parent

    note over SC: Recursive process reaches all the way to the Root Node
    SC->>Root: split()
    activate Root
    Root-->>SC: (root_median_key, sibling_root)
    deactivate Root

    note over SC: Create a new Root, increment tree_height by 1
    SC->>MD: Update new root_page_id & tree_height += 1
    activate MD
    MD-->>SC: success
    deactivate MD
    
    SC-->>BE: split_completed
    deactivate SC
    
    BE->>LCM: release_all_latches()
    activate LCM
    LCM-->>BE: success
    deactivate LCM
    
    BE-->>AM: success
    deactivate BE
    AM-->>Client: success
    deactivate AM
```

---

## 4. Scenario D: Duplicate Key on Unique Index

* **Description:** The index is configured as unique (`is_unique = True`). Before insertion, the system performs a search and detects that this key already exists in the index tree. The insertion process stops immediately and throws a duplicate key error.

### Sequence Diagram:
```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant AM as BTreeAccessMethod
    participant MD as IndexMetadata
    participant BE as BTreeEngine
    participant Leaf as LeafNode

    Client->>AM: insert(key, rid)
    activate AM
    
    AM->>MD: get metadata info
    activate MD
    MD-->>AM: root_page_id, is_unique=True
    deactivate MD

    AM->>BE: search(root_page_id, key)
    activate BE
    BE-->>AM: leaf_node
    deactivate BE

    AM->>Leaf: lookup(key)
    activate Leaf
    Leaf-->>AM: List[RecordID] (contains existing records)
    deactivate Leaf

    note over AM: Check indicates is_unique == True and key already exists
    AM-->>Client: raise DuplicateKeyException("Key already exists")
    deactivate AM
```
