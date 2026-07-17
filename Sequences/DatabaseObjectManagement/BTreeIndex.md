# Sequence Diagrams: BTreeIndex

## 🆕 Added Properties & Methods for `BTreeIndex`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `BTreeIndex` class in your Class Diagram with these:**

- **Property** added to `BTreeIndex`: `rootNode` (Entry point for B-Tree)
- **Method** added to `BTreeIndex`: `balanceTree()` (Rebalances tree after insertion)

---

This file contains the detailed sequence diagrams for all unit tests of the **BTreeIndex** class in the Database Object Management subsystem.

## 1. InsertKey_WhenValid_AddsNodeToTreeBalancing

```mermaid
sequenceDiagram
    actor Test
    participant BTreeIndex

    Test->>BTreeIndex: insertKey(key, rowId)
    BTreeIndex->>BTreeIndex: find insertion point
    BTreeIndex->>BTreeIndex: insert(key, rowId)
    BTreeIndex->>BTreeIndex: balanceTree()
    BTreeIndex-->>Test: success
```

## 2. Search_WhenKeyExists_ReturnsCorrespondingRowID

```mermaid
sequenceDiagram
    actor Test
    participant BTreeIndex

    Test->>BTreeIndex: search(key)
    BTreeIndex->>BTreeIndex: traverse nodes
    BTreeIndex-->>BTreeIndex: key found
    BTreeIndex-->>Test: return rowId
```

## 3. Search_WhenKeyNotExists_ReturnsEmptyResult

```mermaid
sequenceDiagram
    actor Test
    participant BTreeIndex

    Test->>BTreeIndex: search(invalidKey)
    BTreeIndex->>BTreeIndex: traverse nodes
    BTreeIndex-->>BTreeIndex: not found
    BTreeIndex-->>Test: return null
```

