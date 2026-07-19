# Sequence Diagrams: IndexFile

## 🆕 Added Properties & Methods for `IndexFile`
To support the detailed sequence logic for unit testing, please update the `IndexFile` class in your Class Diagram with the following properties and methods:

- **Property** added to `IndexFile`: `fileStream`
- **Method** added to `IndexFile`: `readBlock()`
- **Method** added to `IndexFile`: `rebuild()`
- **Method** added to `IndexFile`: `verifyChecksum()`
- **Method** added to `IndexFile`: `writeBlock()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **IndexFile** class.

## 1. Init_OpensFileStreamForIndexBlocks

```mermaid
sequenceDiagram
    actor TestRunner
    participant IndexFile
    TestRunner->>IndexFile: init()
    IndexFile->>IndexFile: apply OpensFileStreamForIndexBlocks
    IndexFile->>Dependency: invoke logic
    Dependency-->>IndexFile: success
    IndexFile-->>TestRunner: Success
```

## 2. WriteBlock_SavesBytesToDisk

```mermaid
sequenceDiagram
    actor TestRunner
    participant IndexFile
    TestRunner->>IndexFile: writeBlock()
    IndexFile->>IndexFile: apply SavesBytesToDisk
    IndexFile->>Dependency: invoke logic
    Dependency-->>IndexFile: success
    IndexFile-->>TestRunner: Success
```

## 3. ReadBlock_LoadsBytesFromDisk

```mermaid
sequenceDiagram
    actor TestRunner
    participant IndexFile
    TestRunner->>IndexFile: readBlock()
    IndexFile->>IndexFile: apply LoadsBytesFromDisk
    IndexFile->>Dependency: invoke logic
    Dependency-->>IndexFile: success
    IndexFile-->>TestRunner: Success
```

## 4. Rebuild_CompactsIndexData

```mermaid
sequenceDiagram
    actor TestRunner
    participant IndexFile
    TestRunner->>IndexFile: rebuild()
    IndexFile->>IndexFile: apply CompactsIndexData
    IndexFile->>Dependency: invoke logic
    Dependency-->>IndexFile: success
    IndexFile-->>TestRunner: Success
```

## 5. VerifyChecksum_DetectsCorruption

```mermaid
sequenceDiagram
    actor TestRunner
    participant IndexFile
    TestRunner->>IndexFile: verifyChecksum()
    IndexFile->>IndexFile: apply DetectsCorruption
    IndexFile->>Dependency: invoke logic
    Dependency-->>IndexFile: success
    IndexFile-->>TestRunner: Success
```

