# Sequence Diagrams: BTreeIndex

## 🆕 Added Properties & Methods for `BTreeIndex`
To support the detailed sequence logic for unit testing, please update the `BTreeIndex` class in your Class Diagram with the following properties and methods:

- **Property** added to `BTreeIndex`: `rootNode`
- **Method** added to `BTreeIndex`: `bulkLoad()`
- **Method** added to `BTreeIndex`: `deleteKey()`
- **Method** added to `BTreeIndex`: `insertKey()`
- **Method** added to `BTreeIndex`: `mergeNodes()`
- **Method** added to `BTreeIndex`: `rangeSearch()`
- **Method** added to `BTreeIndex`: `search()`
- **Method** added to `BTreeIndex`: `splitNode()`

---

This file contains the detailed sequence diagrams for all 8 unit tests of the **BTreeIndex** class.

## 1. InsertKey_WhenValid_AddsNodeToTreeBalancing

```mermaid
sequenceDiagram
    actor TestRunner
    participant BTreeIndex
    TestRunner->>BTreeIndex: insertKey()
    BTreeIndex->>BTreeIndex: apply WhenValid
    BTreeIndex->>Dependency: invoke logic
    Dependency-->>BTreeIndex: success
    BTreeIndex-->>TestRunner: AddsNodeToTreeBalancing
```

## 2. Search_WhenKeyExists_ReturnsCorrespondingRowID

```mermaid
sequenceDiagram
    actor TestRunner
    participant BTreeIndex
    TestRunner->>BTreeIndex: search()
    BTreeIndex->>BTreeIndex: validate WhenKeyExists
    BTreeIndex->>BTreeIndex: process Search
    BTreeIndex-->>TestRunner: return CorrespondingRowID
```

## 3. Search_WhenKeyNotExists_ReturnsEmptyResult

```mermaid
sequenceDiagram
    actor TestRunner
    participant BTreeIndex
    TestRunner->>BTreeIndex: search()
    BTreeIndex->>BTreeIndex: validate WhenKeyNotExists
    BTreeIndex->>BTreeIndex: process Search
    BTreeIndex-->>TestRunner: return EmptyResult
```

## 4. DeleteKey_WhenExists_RemovesNodeAndRebalances

```mermaid
sequenceDiagram
    actor TestRunner
    participant BTreeIndex
    TestRunner->>BTreeIndex: deleteKey()
    BTreeIndex->>BTreeIndex: apply WhenExists
    BTreeIndex->>Dependency: invoke logic
    Dependency-->>BTreeIndex: success
    BTreeIndex-->>TestRunner: RemovesNodeAndRebalances
```

## 5. RangeSearch_ReturnsAllRowIDsInRange

```mermaid
sequenceDiagram
    actor TestRunner
    participant BTreeIndex
    TestRunner->>BTreeIndex: rangeSearch()
    BTreeIndex->>BTreeIndex: apply ReturnsAllRowIDsInRange
    BTreeIndex->>Dependency: invoke logic
    Dependency-->>BTreeIndex: success
    BTreeIndex-->>TestRunner: Success
```

## 6. BulkLoad_BuildsTreeEfficientlyFromSortedData

```mermaid
sequenceDiagram
    actor TestRunner
    participant BTreeIndex
    TestRunner->>BTreeIndex: bulkLoad()
    BTreeIndex->>BTreeIndex: apply BuildsTreeEfficientlyFromSortedData
    BTreeIndex->>Dependency: invoke logic
    Dependency-->>BTreeIndex: success
    BTreeIndex-->>TestRunner: Success
```

## 7. SplitNode_WhenFull_CreatesSibling

```mermaid
sequenceDiagram
    actor TestRunner
    participant BTreeIndex
    TestRunner->>BTreeIndex: splitNode()
    BTreeIndex->>BTreeIndex: validate WhenFull
    BTreeIndex->>BTreeIndex: process SplitNode
    BTreeIndex-->>TestRunner: return CreatesSibling
```

## 8. MergeNodes_WhenUnderfull_CombinesSiblings

```mermaid
sequenceDiagram
    actor TestRunner
    participant BTreeIndex
    TestRunner->>BTreeIndex: mergeNodes()
    BTreeIndex->>BTreeIndex: apply WhenUnderfull
    BTreeIndex->>Dependency: invoke logic
    Dependency-->>BTreeIndex: success
    BTreeIndex-->>TestRunner: CombinesSiblings
```

