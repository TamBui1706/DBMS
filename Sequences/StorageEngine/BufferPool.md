# Sequence Diagrams: BufferPool

## 🆕 Added Properties & Methods for `BufferPool`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `BufferPool` class in your Class Diagram with these:**

- **Property** added to `BufferPool`: `pages` (Dictionary of cached pages)
- **Property** added to `BufferPool`: `replacementAlgorithm` (Reference to PageReplacementAlgorithm)
- **Method** added to `BufferPool`: `evictPage()` (Finds a victim page and removes it)

---

This file contains the detailed sequence diagrams for all unit tests of the **BufferPool** class in the Storage Engine subsystem.

## 1. PinPage_IncrementsPinCountAndPreventsEviction

```mermaid
sequenceDiagram
    actor Test
    participant BufferPool
    participant Page

    Test->>BufferPool: pinPage(pageId)
    BufferPool->>BufferPool: get page from pages dict
    BufferPool->>Page: increment pinCount
    Page-->>BufferPool: success
    BufferPool-->>Test: success
```

## 2. UnpinPage_DecrementsPinCount

```mermaid
sequenceDiagram
    actor Test
    participant BufferPool
    participant Page

    Test->>BufferPool: unpinPage(pageId)
    BufferPool->>BufferPool: get page from pages dict
    BufferPool->>Page: decrement pinCount
    Page-->>BufferPool: success
    BufferPool-->>Test: success
```

## 3. FlushPage_ForcesDirtyPageToDisk

```mermaid
sequenceDiagram
    actor Test
    participant BufferPool
    participant StorageEngine

    Test->>BufferPool: flushPage(pageId)
    BufferPool->>StorageEngine: writePage(pageId)
    StorageEngine-->>BufferPool: success
    BufferPool-->>Test: success
```

## 4. FetchPage_WhenPoolFull_EvictsUnpinnedPage

```mermaid
sequenceDiagram
    actor Test
    participant BufferPool
    participant PageReplacementAlgorithm
    participant StorageEngine

    Test->>BufferPool: fetchPage(newPageId)
    BufferPool->>BufferPool: check pool is full
    BufferPool->>PageReplacementAlgorithm: findVictim()
    PageReplacementAlgorithm-->>BufferPool: victimPageId
    BufferPool->>StorageEngine: writePage(victimPageId) (if dirty)
    StorageEngine-->>BufferPool: success
    BufferPool->>BufferPool: remove victimPageId, insert newPageId
    BufferPool-->>Test: return new Page
```

