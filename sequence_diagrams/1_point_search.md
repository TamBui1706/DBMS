# Index Management Subsystem - Point Search Flow

The Point Search flow performs a search for a specific key in the B+ Tree index to return the corresponding list of `RecordID`s. Below is a detailed description of the scenarios for this flow.

---

## 1. Scenario A: Key Found - Happy Path

* **Description:** The key exists in the index. The traversal process succeeds from the root node down to the leaf node, applying **Read Lock Crabbing**, finds the key at the leaf page, and returns a valid list of `RecordID`s.

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
    participant Internal as InternalNode
    participant Comp as IKeyComparator

    Client->>AM: point_search(key)
    activate AM
    
    AM->>MD: get root_page_id & state
    activate MD
    MD-->>AM: root_page_id, state=VALID
    deactivate MD

    AM->>BE: search(root_page_id, key)
    activate BE
    
    BE->>BE: _traverse(root_page_id, key, LatchMode.READ)
    activate BE
    
    BE->>LCM: acquire_latch(root_node, LatchMode.READ)
    activate LCM
    LCM-->>BE: success
    deactivate LCM
    
    loop Traverse from parent node to child node (InternalNode -> ChildNode)
        BE->>Internal: get children page pointers
        activate Internal
        Internal-->>BE: children_page_ids
        deactivate Internal
        
        BE->>Internal: lookup(key, comparator)
        activate Internal
        Internal->>Comp: compare(key, node_keys)
        activate Comp
        Comp-->>Internal: index_position
        deactivate Comp
        Internal-->>BE: child_page_id
        deactivate Internal
        
        BE->>LCM: acquire_latch(child_node, LatchMode.READ)
        activate LCM
        LCM-->>BE: success
        deactivate LCM
        
        BE->>LCM: release_latch(parent_node)
        activate LCM
        LCM-->>BE: success
        deactivate LCM
    end
    deactivate BE
    
    BE-->>AM: leaf_node (holds Read latch)
    deactivate BE

    AM->>Leaf: lookup(key, comparator)
    activate Leaf
    Leaf->>Comp: compare(key, leaf_keys)
    activate Comp
    Comp-->>Leaf: matching_positions
    deactivate Comp
    Leaf-->>AM: List[RecordID]
    deactivate Leaf

    AM->>LCM: release_all_latches()
    activate LCM
    LCM-->>AM: success
    deactivate LCM

    AM-->>Client: List[RecordID]
    deactivate AM
```

---

## 2. Scenario B: Key Not Found

* **Description:** The key does not exist in the index. The tree traversal process proceeds normally down to the leaf node, but when performing the binary search on the leaf node, there is no matching key. The system returns an empty list (`[]`).

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
    participant Internal as InternalNode
    participant Comp as IKeyComparator

    Client->>AM: point_search(key)
    activate AM
    
    AM->>MD: get root_page_id & state
    activate MD
    MD-->>AM: root_page_id, state=VALID
    deactivate MD

    AM->>BE: search(root_page_id, key)
    activate BE
    
    BE->>BE: _traverse(root_page_id, key, LatchMode.READ)
    activate BE
    
    BE->>LCM: acquire_latch(root_node, LatchMode.READ)
    activate LCM
    LCM-->>BE: success
    deactivate LCM
    
    loop Traverse from parent node to child node (InternalNode -> ChildNode)
        BE->>Internal: get children page pointers
        activate Internal
        Internal-->>BE: children_page_ids
        deactivate Internal
        
        BE->>Internal: lookup(key, comparator)
        activate Internal
        Internal->>Comp: compare(key, node_keys)
        activate Comp
        Comp-->>Internal: index_position
        deactivate Comp
        Internal-->>BE: child_page_id
        deactivate Internal
        
        BE->>LCM: acquire_latch(child_node, LatchMode.READ)
        activate LCM
        LCM-->>BE: success
        deactivate LCM
        
        BE->>LCM: release_latch(parent_node)
        activate LCM
        LCM-->>BE: success
        deactivate LCM
    end
    deactivate BE
    
    BE-->>AM: leaf_node (holds Read latch)
    deactivate BE

    AM->>Leaf: lookup(key, comparator)
    activate Leaf
    Leaf->>Comp: compare(key, leaf_keys)
    activate Comp
    Comp-->>Leaf: not_found_index
    deactivate Comp
    Leaf-->>AM: Empty List []
    deactivate Leaf

    AM->>LCM: release_all_latches()
    activate LCM
    LCM-->>AM: success
    deactivate LCM

    AM-->>Client: Empty List []
    deactivate AM
```

---

## 3. Scenario C: Invalid Index - Early Failure

* **Description:** The client requests a search on an index that is corrupted or currently being built (`state != VALID`). The system checks the metadata, detects the invalid state, and aborts the process early, throwing an error.

### Sequence Diagram:
```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant AM as BTreeAccessMethod
    participant MD as IndexMetadata

    Client->>AM: point_search(key)
    activate AM
    
    AM->>MD: get root_page_id & state
    activate MD
    MD-->>AM: root_page_id, state=BUILDING
    deactivate MD

    note over AM: Check indicates state == BUILDING or INVALID
    AM-->>Client: raise IndexUnusableException("Index is invalid or building")
    deactivate AM
```
