# Index Management Subsystem - Bulk Loading Flow

Bulk Loading is an extremely high-performance optimization method used to build a new B+ Tree index from a large existing dataset using a bottom-up build algorithm.

---

## 1. Scenario A: Bulk Load Success

* **Description:** The input dataset contains multiple valid records. The process first sorts the entire data by key, then sequentially allocates the records into leaf pages from left to right. When a page fills up, the separating key is pushed directly to the immediate parent nodes (InternalNode) without recursively traversing from the root node.

### Sequence Diagram:
```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant LM as BTreeLifecycleManager
    participant BE as BTreeEngine
    participant MD as IndexMetadata
    participant Leaf as LeafNode
    participant Parent as InternalNode

    Client->>LM: bulk_load(index_id, sorted_entries)
    activate LM

    note over LM: Perform ascending sort on raw data by key using KeyComparator
    LM->>LM: sort(raw_entries)
    
    LM->>BE: bulk_load_build(sorted_entries)
    activate BE

    loop For each Entry in the sorted list
        alt Current leaf page is not full
            BE->>Leaf: Write entry directly to the current LeafNode
        else Current leaf page is full
            BE->>Leaf: Set next_page_id pointing to the new page
            BE->>BE: Initialize a new leaf page (NewLeafNode)
            BE->>Leaf: Write entry to the new leaf page
            BE->>Parent: Push the separating key and leaf page address to the parent node (Level 1 InternalNode)
            
            opt Parent node (InternalNode) is also full
                BE->>Parent: Create a new parent node and push the key to a higher-level InternalNode
            end
        end
    end

    BE-->>LM: new_root_page_id
    deactivate BE

    LM->>MD: Update new root_page_id, state=VALID, tree_height, node_count, key_count
    activate MD
    MD-->>LM: success
    deactivate MD

    LM-->>Client: success (Index build completed)
    deactivate LM
```

---

## 2. Scenario B: Empty Dataset

* **Description:** The input dataset contains no elements. The process creates a standard empty index tree: consisting of only a single empty leaf page acting as the root node. The index state is set to `VALID`.

### Sequence Diagram:
```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant LM as BTreeLifecycleManager
    participant BE as BTreeEngine
    participant MD as IndexMetadata

    Client->>LM: bulk_load(index_id, empty_entries)
    activate LM

    LM->>BE: allocate_empty_tree()
    activate BE
    BE-->>LM: empty_root_page_id
    deactivate BE
    
    LM->>MD: Update root_page_id, state=VALID, height=1
    activate MD
    MD-->>LM: success
    deactivate MD
    
    LM-->>Client: success (Empty Index Initialized)
    deactivate LM
```
