# Sequence Diagrams: CheckpointManager

## 🆕 Added Properties & Methods for `CheckpointManager`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `CheckpointManager` class in your Class Diagram with these:**

- **Property** added to `CheckpointManager`: `bufferPool` (Reference to force flush dirty pages)

---

This file contains the detailed sequence diagrams for all unit tests of the **CheckpointManager** class in the Backup & Durability subsystem.

## 1. TakeCheckpoint_FlushesAllDirtyPages

```mermaid
sequenceDiagram
    actor Test
    participant CheckpointManager
    participant BufferPool

    Test->>CheckpointManager: takeCheckpoint()
    CheckpointManager->>BufferPool: flushAllDirtyPages()
    BufferPool-->>CheckpointManager: success
    CheckpointManager-->>Test: success
```

## 2. TakeCheckpoint_WritesCheckpointRecordToLog

```mermaid
sequenceDiagram
    actor Test
    participant CheckpointManager
    participant WALManager

    Test->>CheckpointManager: takeCheckpoint()
    CheckpointManager->>WALManager: appendLog(CheckpointRecord)
    WALManager-->>CheckpointManager: success
    CheckpointManager->>WALManager: flush()
    WALManager-->>CheckpointManager: success
    CheckpointManager-->>Test: success
```

