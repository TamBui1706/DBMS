# Sequence Diagrams: FileManager

## 🆕 Added Properties & Methods for `FileManager`
To support the detailed sequence logic for unit testing, please update the `FileManager` class in your Class Diagram with the following properties and methods:

- **Property** added to `FileManager`: `freeBlocks (List)`
- **Method** added to `FileManager`: `allocateSpace()`
- **Method** added to `FileManager`: `checkSpace()`
- **Method** added to `FileManager`: `closeAll()`
- **Method** added to `FileManager`: `deallocateSpace()`
- **Method** added to `FileManager`: `extendFile()`
- **Method** added to `FileManager`: `getFileSize()`

---

This file contains the detailed sequence diagrams for all 6 unit tests of the **FileManager** class.

## 1. AllocateSpace_CreatesNewBlockAndReturnsId

```mermaid
sequenceDiagram
    actor TestRunner
    participant FileManager
    TestRunner->>FileManager: allocateSpace()
    FileManager->>FileManager: apply CreatesNewBlockAndReturnsId
    FileManager->>Dependency: invoke logic
    Dependency-->>FileManager: success
    FileManager-->>TestRunner: Success
```

## 2. DeallocateSpace_MarksBlockAsFree

```mermaid
sequenceDiagram
    actor TestRunner
    participant FileManager
    TestRunner->>FileManager: deallocateSpace()
    FileManager->>FileManager: apply MarksBlockAsFree
    FileManager->>Dependency: invoke logic
    Dependency-->>FileManager: success
    FileManager-->>TestRunner: Success
```

## 3. ExtendFile_IncreasesFileSizeWhenFull

```mermaid
sequenceDiagram
    actor TestRunner
    participant FileManager
    TestRunner->>FileManager: extendFile()
    FileManager->>FileManager: apply IncreasesFileSizeWhenFull
    FileManager->>Dependency: invoke logic
    Dependency-->>FileManager: success
    FileManager-->>TestRunner: Success
```

## 4. CloseAll_ReleasesFileHandles

```mermaid
sequenceDiagram
    actor TestRunner
    participant FileManager
    TestRunner->>FileManager: closeAll()
    FileManager->>FileManager: apply ReleasesFileHandles
    FileManager->>Dependency: invoke logic
    Dependency-->>FileManager: success
    FileManager-->>TestRunner: Success
```

## 5. GetFileSize_ReturnsSizeInBytes

```mermaid
sequenceDiagram
    actor TestRunner
    participant FileManager
    TestRunner->>FileManager: getFileSize()
    FileManager->>FileManager: apply ReturnsSizeInBytes
    FileManager->>Dependency: invoke logic
    Dependency-->>FileManager: success
    FileManager-->>TestRunner: Success
```

## 6. CheckSpace_ReturnsAvailableBlocks

```mermaid
sequenceDiagram
    actor TestRunner
    participant FileManager
    TestRunner->>FileManager: checkSpace()
    FileManager->>FileManager: apply ReturnsAvailableBlocks
    FileManager->>Dependency: invoke logic
    Dependency-->>FileManager: success
    FileManager-->>TestRunner: Success
```

