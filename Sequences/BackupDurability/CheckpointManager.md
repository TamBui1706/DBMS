# Sequence Diagrams: CheckpointManager

## 🆕 Added Properties & Methods for `CheckpointManager`
To support the detailed sequence logic for unit testing, please update the `CheckpointManager` class in your Class Diagram with the following properties and methods:

- **Property** added to `CheckpointManager`: `bufferPool`
- **Method** added to `CheckpointManager`: `autoCheckpoint()`
- **Method** added to `CheckpointManager`: `getLastCheckpointLSN()`
- **Method** added to `CheckpointManager`: `takeCheckpoint()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **CheckpointManager** class.

## 1. TakeCheckpoint_FlushesAllDirtyPages

```mermaid
sequenceDiagram
    actor TestRunner
    participant CheckpointManager
    TestRunner->>CheckpointManager: takeCheckpoint()
    CheckpointManager->>CheckpointManager: apply FlushesAllDirtyPages
    CheckpointManager->>Dependency: invoke logic
    Dependency-->>CheckpointManager: success
    CheckpointManager-->>TestRunner: Success
```

## 2. TakeCheckpoint_WritesCheckpointRecordToLog

```mermaid
sequenceDiagram
    actor TestRunner
    participant CheckpointManager
    TestRunner->>CheckpointManager: takeCheckpoint()
    CheckpointManager->>CheckpointManager: apply WritesCheckpointRecordToLog
    CheckpointManager->>Dependency: invoke logic
    Dependency-->>CheckpointManager: success
    CheckpointManager-->>TestRunner: Success
```

## 3. AutoCheckpoint_TriggersWhenLogReachesSizeLimit

```mermaid
sequenceDiagram
    actor TestRunner
    participant CheckpointManager
    TestRunner->>CheckpointManager: autoCheckpoint()
    CheckpointManager->>CheckpointManager: apply TriggersWhenLogReachesSizeLimit
    CheckpointManager->>Dependency: invoke logic
    Dependency-->>CheckpointManager: success
    CheckpointManager-->>TestRunner: Success
```

## 4. AutoCheckpoint_TriggersWhenTimeIntervalElapsed

```mermaid
sequenceDiagram
    actor TestRunner
    participant CheckpointManager
    TestRunner->>CheckpointManager: autoCheckpoint()
    CheckpointManager->>CheckpointManager: apply TriggersWhenTimeIntervalElapsed
    CheckpointManager->>Dependency: invoke logic
    Dependency-->>CheckpointManager: success
    CheckpointManager-->>TestRunner: Success
```

## 5. GetLastCheckpointLSN_ReadsFromMasterRecord

```mermaid
sequenceDiagram
    actor TestRunner
    participant CheckpointManager
    TestRunner->>CheckpointManager: getLastCheckpointLSN()
    CheckpointManager->>CheckpointManager: apply ReadsFromMasterRecord
    CheckpointManager->>Dependency: invoke logic
    Dependency-->>CheckpointManager: success
    CheckpointManager-->>TestRunner: Success
```

