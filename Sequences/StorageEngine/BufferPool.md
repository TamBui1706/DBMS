# Sequence Diagrams: BufferPool

## 🆕 Added Properties & Methods for `BufferPool`
To support the detailed sequence logic for unit testing, please update the `BufferPool` class in your Class Diagram with the following properties and methods:

- **Property** added to `BufferPool`: `pages (Dict)`
- **Property** added to `BufferPool`: `replacementAlgorithm`
- **Property** added to `BufferPool`: `maxSize (Int)`
- **Method** added to `BufferPool`: `clear()`
- **Method** added to `BufferPool`: `fetchPage()`
- **Method** added to `BufferPool`: `flushPage()`
- **Method** added to `BufferPool`: `getHitRate()`
- **Method** added to `BufferPool`: `pinPage()`
- **Method** added to `BufferPool`: `unpinPage()`

---

This file contains the detailed sequence diagrams for all 8 unit tests of the **BufferPool** class.

## 1. PinPage_IncrementsPinCountAndPreventsEviction

```mermaid
sequenceDiagram
    actor TestRunner
    participant BufferPool
    TestRunner->>BufferPool: pinPage()
    BufferPool->>BufferPool: apply IncrementsPinCountAndPreventsEviction
    BufferPool->>Dependency: invoke logic
    Dependency-->>BufferPool: success
    BufferPool-->>TestRunner: Success
```

## 2. UnpinPage_DecrementsPinCount

```mermaid
sequenceDiagram
    actor TestRunner
    participant BufferPool
    TestRunner->>BufferPool: unpinPage()
    BufferPool->>BufferPool: apply DecrementsPinCount
    BufferPool->>Dependency: invoke logic
    Dependency-->>BufferPool: success
    BufferPool-->>TestRunner: Success
```

## 3. FlushPage_ForcesDirtyPageToDisk

```mermaid
sequenceDiagram
    actor TestRunner
    participant BufferPool
    TestRunner->>BufferPool: flushPage()
    BufferPool->>BufferPool: apply ForcesDirtyPageToDisk
    BufferPool->>Dependency: invoke logic
    Dependency-->>BufferPool: success
    BufferPool-->>TestRunner: Success
```

## 4. FetchPage_WhenPoolFull_EvictsUnpinnedPage

```mermaid
sequenceDiagram
    actor TestRunner
    participant BufferPool
    TestRunner->>BufferPool: fetchPage()
    BufferPool->>BufferPool: apply WhenPoolFull
    BufferPool->>Dependency: invoke logic
    Dependency-->>BufferPool: success
    BufferPool-->>TestRunner: EvictsUnpinnedPage
```

## 5. FetchPage_WhenAllPagesPinned_ThrowsBufferFullException

```mermaid
sequenceDiagram
    actor TestRunner
    participant BufferPool
    TestRunner->>BufferPool: fetchPage()
    BufferPool->>BufferPool: check WhenAllPagesPinned
    BufferPool-->>BufferPool: condition failed
    BufferPool-->>TestRunner: throws BufferFullException
```

## 6. GetHitRate_ReturnsCacheHitRatioMetrics

```mermaid
sequenceDiagram
    actor TestRunner
    participant BufferPool
    TestRunner->>BufferPool: getHitRate()
    BufferPool->>BufferPool: apply ReturnsCacheHitRatioMetrics
    BufferPool->>Dependency: invoke logic
    Dependency-->>BufferPool: success
    BufferPool-->>TestRunner: Success
```

## 7. Clear_EvictsAllUnpinnedPages

```mermaid
sequenceDiagram
    actor TestRunner
    participant BufferPool
    TestRunner->>BufferPool: clear()
    BufferPool->>BufferPool: apply EvictsAllUnpinnedPages
    BufferPool->>Dependency: invoke logic
    Dependency-->>BufferPool: success
    BufferPool-->>TestRunner: Success
```

## 8. UnpinPage_WhenCountIsZero_ThrowsException

```mermaid
sequenceDiagram
    actor TestRunner
    participant BufferPool
    TestRunner->>BufferPool: unpinPage()
    BufferPool->>BufferPool: check WhenCountIsZero
    BufferPool-->>BufferPool: condition failed
    BufferPool-->>TestRunner: throws Exception
```

