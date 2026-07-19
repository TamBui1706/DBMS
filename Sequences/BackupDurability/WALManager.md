# Sequence Diagrams: WALManager

## 🆕 Added Properties & Methods for `WALManager`
To support the detailed sequence logic for unit testing, please update the `WALManager` class in your Class Diagram with the following properties and methods:

- **Property** added to `WALManager`: `logBuffer (List)`
- **Property** added to `WALManager`: `BUFFER_LIMIT (Int)`
- **Method** added to `WALManager`: `appendLog()`
- **Method** added to `WALManager`: `flush()`
- **Method** added to `WALManager`: `readLog()`
- **Method** added to `WALManager`: `switchLogFile()`
- **Method** added to `WALManager`: `truncateLog()`

---

This file contains the detailed sequence diagrams for all 7 unit tests of the **WALManager** class.

## 1. AppendLog_AddsRecordToMemoryBuffer

```mermaid
sequenceDiagram
    actor TestRunner
    participant WALManager
    TestRunner->>WALManager: appendLog()
    WALManager->>WALManager: apply AddsRecordToMemoryBuffer
    WALManager->>Dependency: invoke logic
    Dependency-->>WALManager: success
    WALManager-->>TestRunner: Success
```

## 2. Flush_WritesBufferToDiskSynchronously

```mermaid
sequenceDiagram
    actor TestRunner
    participant WALManager
    TestRunner->>WALManager: flush()
    WALManager->>WALManager: apply WritesBufferToDiskSynchronously
    WALManager->>Dependency: invoke logic
    Dependency-->>WALManager: success
    WALManager-->>TestRunner: Success
```

## 3. AppendLog_WhenBufferFull_TriggersAutomaticFlush

```mermaid
sequenceDiagram
    actor TestRunner
    participant WALManager
    TestRunner->>WALManager: appendLog()
    WALManager->>WALManager: apply WhenBufferFull
    WALManager->>Dependency: invoke logic
    Dependency-->>WALManager: success
    WALManager-->>TestRunner: TriggersAutomaticFlush
```

## 4. ReadLog_ReturnsRecordByLSN

```mermaid
sequenceDiagram
    actor TestRunner
    participant WALManager
    TestRunner->>WALManager: readLog()
    WALManager->>WALManager: apply ReturnsRecordByLSN
    WALManager->>Dependency: invoke logic
    Dependency-->>WALManager: success
    WALManager-->>TestRunner: Success
```

## 5. TruncateLog_DeletesLogsOlderThanCheckpoint

```mermaid
sequenceDiagram
    actor TestRunner
    participant WALManager
    TestRunner->>WALManager: truncateLog()
    WALManager->>WALManager: apply DeletesLogsOlderThanCheckpoint
    WALManager->>Dependency: invoke logic
    Dependency-->>WALManager: success
    WALManager-->>TestRunner: Success
```

## 6. Flush_WhenDiskFull_ThrowsStorageException

```mermaid
sequenceDiagram
    actor TestRunner
    participant WALManager
    TestRunner->>WALManager: flush()
    WALManager->>WALManager: check WhenDiskFull
    WALManager-->>WALManager: condition failed
    WALManager-->>TestRunner: throws StorageException
```

## 7. SwitchLogFile_CreatesNewSegmentWhenMaxFileSizeReached

```mermaid
sequenceDiagram
    actor TestRunner
    participant WALManager
    TestRunner->>WALManager: switchLogFile()
    WALManager->>WALManager: apply CreatesNewSegmentWhenMaxFileSizeReached
    WALManager->>Dependency: invoke logic
    Dependency-->>WALManager: success
    WALManager-->>TestRunner: Success
```

