# Sequence Diagrams: DataFile

## 🆕 Added Properties & Methods for `DataFile`
To support the detailed sequence logic for unit testing, please update the `DataFile` class in your Class Diagram with the following properties and methods:

- **Property** added to `DataFile`: `fileStream`
- **Method** added to `DataFile`: `deleteFile()`
- **Method** added to `DataFile`: `readBlock()`
- **Method** added to `DataFile`: `writeBlock()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **DataFile** class.

## 1. Init_OpensFileStreamForDataBlocks

```mermaid
sequenceDiagram
    actor TestRunner
    participant DataFile
    TestRunner->>DataFile: init()
    DataFile->>DataFile: apply OpensFileStreamForDataBlocks
    DataFile->>Dependency: invoke logic
    Dependency-->>DataFile: success
    DataFile-->>TestRunner: Success
```

## 2. ReadBlock_LoadsBytesFromDisk

```mermaid
sequenceDiagram
    actor TestRunner
    participant DataFile
    TestRunner->>DataFile: readBlock()
    DataFile->>DataFile: apply LoadsBytesFromDisk
    DataFile->>Dependency: invoke logic
    Dependency-->>DataFile: success
    DataFile-->>TestRunner: Success
```

## 3. WriteBlock_SavesBytesToDisk

```mermaid
sequenceDiagram
    actor TestRunner
    participant DataFile
    TestRunner->>DataFile: writeBlock()
    DataFile->>DataFile: apply SavesBytesToDisk
    DataFile->>Dependency: invoke logic
    Dependency-->>DataFile: success
    DataFile-->>TestRunner: Success
```

## 4. DeleteFile_RemovesFromOS

```mermaid
sequenceDiagram
    actor TestRunner
    participant DataFile
    TestRunner->>DataFile: deleteFile()
    DataFile->>DataFile: apply RemovesFromOS
    DataFile->>Dependency: invoke logic
    Dependency-->>DataFile: success
    DataFile-->>TestRunner: Success
```

## 5. Init_WhenFileLockedByOS_ThrowsIOException

```mermaid
sequenceDiagram
    actor TestRunner
    participant DataFile
    TestRunner->>DataFile: init()
    DataFile->>DataFile: check WhenFileLockedByOS
    DataFile-->>DataFile: condition failed
    DataFile-->>TestRunner: throws IOException
```

