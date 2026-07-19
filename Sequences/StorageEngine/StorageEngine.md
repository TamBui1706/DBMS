# Sequence Diagrams: StorageEngine

## 🆕 Added Properties & Methods for `StorageEngine`
To support the detailed sequence logic for unit testing, please update the `StorageEngine` class in your Class Diagram with the following properties and methods:

- **Method** added to `StorageEngine`: `allocatePage()`
- **Method** added to `StorageEngine`: `deallocatePage()`
- **Method** added to `StorageEngine`: `formatDrive()`
- **Method** added to `StorageEngine`: `readPage()`
- **Method** added to `StorageEngine`: `sync()`
- **Method** added to `StorageEngine`: `writePage()`

---

This file contains the detailed sequence diagrams for all 6 unit tests of the **StorageEngine** class.

## 1. ReadPage_WhenPageNotInBuffer_LoadsFromDisk

```mermaid
sequenceDiagram
    actor TestRunner
    participant StorageEngine
    TestRunner->>StorageEngine: readPage()
    StorageEngine->>StorageEngine: apply WhenPageNotInBuffer
    StorageEngine->>Dependency: invoke logic
    Dependency-->>StorageEngine: success
    StorageEngine-->>TestRunner: LoadsFromDisk
```

## 2. WritePage_WhenPageIsDirty_FlushesToDisk

```mermaid
sequenceDiagram
    actor TestRunner
    participant StorageEngine
    TestRunner->>StorageEngine: writePage()
    StorageEngine->>StorageEngine: apply WhenPageIsDirty
    StorageEngine->>Dependency: invoke logic
    Dependency-->>StorageEngine: success
    StorageEngine-->>TestRunner: FlushesToDisk
```

## 3. AllocatePage_CreatesNewPageAndReturnsId

```mermaid
sequenceDiagram
    actor TestRunner
    participant StorageEngine
    TestRunner->>StorageEngine: allocatePage()
    StorageEngine->>StorageEngine: apply CreatesNewPageAndReturnsId
    StorageEngine->>Dependency: invoke logic
    Dependency-->>StorageEngine: success
    StorageEngine-->>TestRunner: Success
```

## 4. DeallocatePage_FreesPageSpace

```mermaid
sequenceDiagram
    actor TestRunner
    participant StorageEngine
    TestRunner->>StorageEngine: deallocatePage()
    StorageEngine->>StorageEngine: apply FreesPageSpace
    StorageEngine->>Dependency: invoke logic
    Dependency-->>StorageEngine: success
    StorageEngine-->>TestRunner: Success
```

## 5. Sync_ForcesAllDirtyPagesToDisk

```mermaid
sequenceDiagram
    actor TestRunner
    participant StorageEngine
    TestRunner->>StorageEngine: sync()
    StorageEngine->>StorageEngine: apply ForcesAllDirtyPagesToDisk
    StorageEngine->>Dependency: invoke logic
    Dependency-->>StorageEngine: success
    StorageEngine-->>TestRunner: Success
```

## 6. FormatDrive_InitializesDataDirectoryStructure

```mermaid
sequenceDiagram
    actor TestRunner
    participant StorageEngine
    TestRunner->>StorageEngine: formatDrive()
    StorageEngine->>StorageEngine: apply InitializesDataDirectoryStructure
    StorageEngine->>Dependency: invoke logic
    Dependency-->>StorageEngine: success
    StorageEngine-->>TestRunner: Success
```

