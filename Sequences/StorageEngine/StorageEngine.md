# Sequence Diagrams: StorageEngine

## 🆕 Added Properties & Methods for `StorageEngine`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `StorageEngine` class in your Class Diagram with these:**

- **Method** added to `StorageEngine`: `checkBuffer(pageId)` (Checks BufferPool before disk access)

---

This file contains the detailed sequence diagrams for all unit tests of the **StorageEngine** class in the Storage Engine subsystem.

## 1. ReadPage_WhenPageNotInBuffer_LoadsFromDisk

```mermaid
sequenceDiagram
    actor Test
    participant StorageEngine
    participant BufferPool
    participant FileManager

    Test->>StorageEngine: readPage(pageId)
    StorageEngine->>BufferPool: checkBuffer(pageId)
    BufferPool-->>StorageEngine: not found
    StorageEngine->>FileManager: readBlock(pageId)
    FileManager-->>StorageEngine: rawBytes
    StorageEngine->>BufferPool: addPage(rawBytes)
    BufferPool-->>StorageEngine: pageObject
    StorageEngine-->>Test: return pageObject
```

## 2. WritePage_WhenPageIsDirty_FlushesToDisk

```mermaid
sequenceDiagram
    actor Test
    participant StorageEngine
    participant BufferPool
    participant FileManager

    Test->>StorageEngine: writePage(pageId)
    StorageEngine->>BufferPool: checkBuffer(pageId)
    BufferPool-->>StorageEngine: page (isDirty=true)
    StorageEngine->>FileManager: writeBlock(pageId, page.data)
    FileManager-->>StorageEngine: success
    StorageEngine->>BufferPool: markClean(pageId)
    BufferPool-->>StorageEngine: success
    StorageEngine-->>Test: success
```

