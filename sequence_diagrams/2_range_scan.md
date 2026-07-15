# Index Management Subsystem - Range Scan Flow

The Range Scan flow allows users to scan and retrieve all records falling within a key range `[start_key, end_key]` in either forward or backward direction.

---

## 1. Scenario A: Forward Scan - Multiple Leaves

* **Description:** The scan process moves from `start_key` to `end_key` in the forward direction (`direction = FORWARD`). When finishing scanning the current page, it gets the `next_page_id`, acquires the read latch on the next leaf page first before releasing the read latch on the current leaf page (Lock Crabbing on leaf pages) to prevent losing the link due to another write thread.

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
    participant Comp as IKeyComparator
    participant Iter as RangeIterator

    Client->>AM: range_scan(start_key, end_key, ScanDirection.FORWARD)
    activate AM
    
    AM->>MD: get root_page_id
    activate MD
    MD-->>AM: root_page_id
    deactivate MD

    AM->>BE: search(root_page_id, start_key)
    activate BE
    note over BE: Traverse down to the leaf containing start_key and read-latch it
    BE-->>AM: starting_leaf_node (Read Latched)
    deactivate BE

    AM->>Iter: create(starting_leaf, start_key, end_key, FORWARD)
    activate Iter
    Iter-->>AM: iterator_instance
    deactivate Iter
    
    AM-->>Client: Iterator[IndexEntry]
    deactivate AM

    %% Client pulls elements
    Client->>Iter: next()
    activate Iter
    Iter->>Leaf: lookup values inside leaf
    activate Leaf
    Leaf-->>Iter: IndexEntry(key, rid)
    deactivate Leaf
    Iter-->>Client: IndexEntry(key, rid)
    deactivate Iter

    %% Sibling movement
    Client->>Iter: next() (Current leaf has run out of keys)
    activate Iter
    Iter->>Leaf: get next_page_id
    activate Leaf
    Leaf-->>Iter: next_page_id
    deactivate Leaf
    
    Iter->>LCM: acquire_latch(sibling_leaf, LatchMode.READ)
    activate LCM
    LCM-->>Iter: success
    deactivate LCM
    
    Iter->>LCM: release_latch(current_leaf)
    activate LCM
    LCM-->>Iter: success
    deactivate LCM
    
    Iter->>Iter: Update current_leaf = sibling_leaf
    
    Iter->>Sibling: Read first key from the new leaf page
    activate Sibling
    Sibling-->>Iter: key, rid
    deactivate Sibling
    
    Iter-->>Client: IndexEntry(key, rid)
    deactivate Iter

    %% Close iterator
    Client->>Iter: close()
    activate Iter
    Iter->>LCM: release_all_latches()
    activate LCM
    LCM-->>Iter: success
    deactivate LCM
    Iter-->>Client: closed
    deactivate Iter
```

---

## 2. Scenario B: Backward Scan

* **Description:** The backward scan process goes from `start_key` to `end_key` (`direction = BACKWARD`). It traverses in the reverse direction using the previous page link pointer `prev_page_id`.

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
    participant Iter as RangeIterator

    Client->>AM: range_scan(start_key, end_key, ScanDirection.BACKWARD)
    activate AM
    
    AM->>MD: get root_page_id
    activate MD
    MD-->>AM: root_page_id
    deactivate MD

    AM->>BE: search(root_page_id, start_key)
    activate BE
    note over BE: Traverse down to the leaf containing start_key and read-latch it
    BE-->>AM: starting_leaf_node (Read Latched)
    deactivate BE

    AM->>Iter: create(starting_leaf, start_key, end_key, BACKWARD)
    activate Iter
    Iter-->>AM: iterator_instance
    deactivate Iter
    
    AM-->>Client: Iterator[IndexEntry]
    deactivate AM

    %% Client pulls elements
    Client->>Iter: next()
    activate Iter
    Iter->>Leaf: lookup values inside leaf
    activate Leaf
    Leaf-->>Iter: IndexEntry(key, rid)
    deactivate Leaf
    Iter-->>Client: IndexEntry(key, rid)
    deactivate Iter

    %% Sibling movement
    Client->>Iter: next() (Current leaf has run out of keys in reverse direction)
    activate Iter
    Iter->>Leaf: get prev_page_id
    activate Leaf
    Leaf-->>Iter: prev_page_id
    deactivate Leaf
    
    Iter->>LCM: acquire_latch(sibling_leaf, LatchMode.READ)
    activate LCM
    LCM-->>Iter: success
    deactivate LCM
    
    Iter->>LCM: release_latch(current_leaf)
    activate LCM
    LCM-->>Iter: success
    deactivate LCM
    
    Iter->>Iter: Update current_leaf = sibling_leaf
    
    Iter->>Sibling: Read first key from the new leaf page
    activate Sibling
    Sibling-->>Iter: key, rid
    deactivate Sibling
    
    Iter-->>Client: IndexEntry(key, rid)
    deactivate Iter

    %% Close iterator
    Client->>Iter: close()
    activate Iter
    Iter->>LCM: release_all_latches()
    activate LCM
    LCM-->>Iter: success
    deactivate LCM
    Iter-->>Client: closed
    deactivate Iter
```

---

## 3. Scenario C: Empty Range

* **Description:** No key falls within the scan range or the start_key is completely out of bounds of the index tree. The iterator terminates immediately with a `StopIteration` error.

### Sequence Diagram:
```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant AM as BTreeAccessMethod
    participant MD as IndexMetadata
    participant BE as BTreeEngine
    participant Leaf as LeafNode
    participant Comp as IKeyComparator
    participant Iter as RangeIterator

    Client->>AM: range_scan(start_key, end_key, ScanDirection.FORWARD)
    activate AM
    
    AM->>MD: get root_page_id
    activate MD
    MD-->>AM: root_page_id
    deactivate MD

    AM->>BE: search(root_page_id, start_key)
    activate BE
    BE-->>AM: starting_leaf_node (Read Latched)
    deactivate BE

    AM->>Iter: create(starting_leaf, start_key, end_key, FORWARD)
    activate Iter
    Iter-->>AM: iterator_instance
    deactivate Iter
    
    AM-->>Client: Iterator[IndexEntry]
    deactivate AM

    Client->>Iter: next()
    activate Iter
    
    Iter->>Leaf: get keys
    activate Leaf
    Leaf-->>Iter: keys
    deactivate Leaf
    
    Iter->>Comp: compare key with end_key
    activate Comp
    Comp-->>Iter: key_is_greater_than_end_key
    deactivate Comp
    
    note over Iter: The first key is out of bounds of end_key, terminate the scan range
    Iter-->>Client: StopIteration
    deactivate Iter
```
