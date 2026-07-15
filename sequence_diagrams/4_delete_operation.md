# Index Management Subsystem - Delete Flow (Delete Key & Merge/Redistribute)

The flow to delete a key from the B+ Tree performs locating the leaf page containing the key, removing the key, and coordinating tree restructuring if the leaf page falls into an underflow state.

---

## 1. Scenario A: Leaf Safe After Delete (Leaf Safe) - Happy Path

* **Description:** The key is deleted from the leaf page. The number of remaining keys on the leaf page still satisfies the minimum capacity requirement (`key_count >= min_capacity`). The tree structure is preserved.

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

    Client->>AM: delete(key, rid)
    activate AM
    
    AM->>MD: get root_page_id
    activate MD
    MD-->>AM: root_page_id
    deactivate MD

    AM->>BE: delete(root_page_id, key, rid)
    activate BE

    BE->>BE: _traverse(root_page_id, key, LatchMode.WRITE)
    activate BE
    note over BE: Write Latch Crabbing: Only retain latch on the leaf node if the leaf node is safe
    BE-->>BE: leaf_node (Write Latched)
    deactivate BE

    BE->>Leaf: delete(key, rid, comparator)
    activate Leaf
    Leaf-->>BE: True (deleted)
    deactivate Leaf

    note over BE: LeafNode remains safe (key_count >= min_capacity)
    BE->>LCM: release_all_latches()
    activate LCM
    LCM-->>BE: success
    deactivate LCM
    
    BE-->>AM: True
    deactivate BE
    AM-->>Client: True (success)
    deactivate AM
```

---

## 2. Scenario B: Key Underflow & Borrowing from Sibling (Redistribution)

* **Description:** After deletion, the leaf page suffers from underflow (`key_count < min_capacity`). The adjacent sibling (sibling page under the same parent) has surplus keys. The system borrows 1 key from the sibling page and moves it to the underflowing leaf page, and simultaneously updates the separating key in the parent node.

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
    participant MC as MergeCoordinator
    participant Parent as InternalNode

    Client->>AM: delete(key, rid)
    activate AM
    
    AM->>MD: get root_page_id
    activate MD
    MD-->>AM: root_page_id
    deactivate MD

    AM->>BE: delete(root_page_id, key, rid)
    activate BE

    BE->>BE: _traverse(root_page_id, key, LatchMode.WRITE)
    activate BE
    note over BE: Hold Write latches on Parent and LeafNode because LeafNode is likely to underflow
    BE-->>BE: parent_node (Write Latched), leaf_node (Write Latched)
    deactivate BE

    BE->>Leaf: delete(key, rid, comparator)
    activate Leaf
    Leaf-->>BE: True (deleted, underflow detected)
    deactivate Leaf

    BE->>MC: coordinate_merge_or_redistribute(parent_node, leaf_node)
    activate MC
    
    MC->>LCM: acquire_latch(sibling_node, LatchMode.WRITE)
    activate LCM
    LCM-->>MC: success
    deactivate LCM

    note over MC: Detect that Sibling has surplus keys (key_count > min_capacity)
    MC->>MC: Move 1 element from Sibling to LeafNode
    MC->>Parent: Update new Separating Key at the parent node
    
    MC-->>BE: redistribution_completed
    deactivate MC
    
    BE->>LCM: release_all_latches()
    activate LCM
    LCM-->>BE: success
    deactivate LCM
    
    BE-->>AM: True
    deactivate BE
    AM-->>Client: True (success)
    deactivate AM
```

---

## 3. Scenario C: Key Underflow & Node Merging (Merge)

* **Description:** The leaf page suffers from underflow, but the adjacent sibling page also only has the minimum number of keys (cannot lend). The system performs a merge of all keys from the leaf page and the sibling page into a single page. The separating key in the parent node is deleted.

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
    participant MC as MergeCoordinator
    participant Parent as InternalNode

    Client->>AM: delete(key, rid)
    activate AM
    
    AM->>MD: get root_page_id
    activate MD
    MD-->>AM: root_page_id
    deactivate MD

    AM->>BE: delete(root_page_id, key, rid)
    activate BE

    BE->>BE: _traverse(root_page_id, key, LatchMode.WRITE)
    activate BE
    BE-->>BE: parent_node (Write Latched), leaf_node (Write Latched)
    deactivate BE

    BE->>Leaf: delete(key, rid, comparator)
    activate Leaf
    Leaf-->>BE: True (deleted, underflow detected)
    deactivate Leaf

    BE->>MC: coordinate_merge_or_redistribute(parent_node, leaf_node)
    activate MC
    
    MC->>LCM: acquire_latch(sibling_node, LatchMode.WRITE)
    activate LCM
    LCM-->>MC: success
    deactivate LCM

    note over MC: Detect that Sibling is also at minimum level, proceed to merge
    MC->>MC: Merge all keys of LeafNode and Sibling into a single page
    MC->>Parent: Delete Separating Key and the empty page pointer in the parent node
    
    MC-->>BE: merge_completed
    deactivate MC
    
    BE->>LCM: release_all_latches()
    activate LCM
    LCM-->>BE: success
    deactivate LCM
    
    BE-->>AM: True
    deactivate BE
    AM-->>Client: True (success)
    deactivate AM
```

---

## 4. Scenario D: Recursive Merge to Root & Root Delete (Recursive Merge)

* **Description:** After merging the leaf node and deleting the key in the parent node, the parent node also suffers from underflow and must continue merging recursively up to the root. The old root node is left with only 1 child pointer, gets deleted, and promotes its child page to become the new root, decreasing the index tree height by 1.

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
    participant MC as MergeCoordinator
    participant Parent as InternalNode
    participant Root as InternalNode (Old Root)

    Client->>AM: delete(key, rid)
    activate AM
    
    AM->>MD: get root_page_id
    activate MD
    MD-->>AM: root_page_id
    deactivate MD

    AM->>BE: delete(root_page_id, key, rid)
    activate BE

    BE->>BE: _traverse(root_page_id, key, LatchMode.WRITE)
    activate BE
    note over BE: Hold Write latches on all levels from root down to leaf
    BE-->>BE: path_nodes (All Write Latched)
    deactivate BE

    BE->>Leaf: delete(key, rid, comparator)
    activate Leaf
    Leaf-->>BE: True (deleted, underflow detected)
    deactivate Leaf

    BE->>MC: coordinate_merge_or_redistribute(parent_node, leaf_node)
    activate MC
    
    MC->>MC: Merge leaf page and sibling
    MC->>Parent: Delete Separating Key
    
    note over MC: Parent node underflows, proceed to merge recursively upwards
    MC->>Parent: merge()
    activate Parent
    Parent-->>MC: parent_underflow_propagated
    deactivate Parent

    opt Recursion reaches the Root (Old Root only has 1 child pointer left)
        note over MC: Delete old root, promote child page to become the new Root
        MC->>MD: Update new root_page_id & tree_height -= 1
        activate MD
        MD-->>MC: success
        deactivate MD
    end

    MC-->>BE: merge_completed
    deactivate MC
    
    BE->>LCM: release_all_latches()
    activate LCM
    LCM-->>BE: success
    deactivate LCM
    
    BE-->>AM: True
    deactivate BE
    AM-->>Client: True (success)
    deactivate AM
```

---

## 5. Scenario E: Key to Delete Not Found

* **Description:** The system traverses the tree to the leaf node but detects that the key to be deleted does not exist in the index. The process stops and returns `False`.

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

    Client->>AM: delete(key, rid)
    activate AM
    
    AM->>MD: get root_page_id
    activate MD
    MD-->>AM: root_page_id
    deactivate MD

    AM->>BE: delete(root_page_id, key, rid)
    activate BE

    BE->>BE: _traverse(root_page_id, key, LatchMode.WRITE)
    activate BE
    BE-->>BE: leaf_node (Write Latched)
    deactivate BE

    BE->>Leaf: delete(key, rid, comparator)
    activate Leaf
    Leaf-->>BE: False (key_not_found)
    deactivate Leaf

    BE->>LCM: release_all_latches()
    activate LCM
    LCM-->>BE: success
    deactivate LCM
    
    BE-->>AM: False
    deactivate BE
    AM-->>Client: False (failure)
    deactivate AM
```
