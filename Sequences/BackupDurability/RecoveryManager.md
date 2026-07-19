# Sequence Diagrams: RecoveryManager

## 🆕 Added Properties & Methods for `RecoveryManager`
To support the detailed sequence logic for unit testing, please update the `RecoveryManager` class in your Class Diagram with the following properties and methods:

- **Property** added to `RecoveryManager`: `walManager`
- **Method** added to `RecoveryManager`: `analyzePhase()`
- **Method** added to `RecoveryManager`: `recover()`
- **Method** added to `RecoveryManager`: `redoPhase()`
- **Method** added to `RecoveryManager`: `undoPhase()`

---

This file contains the detailed sequence diagrams for all 6 unit tests of the **RecoveryManager** class.

## 1. Recover_WhenSystemCrashes_ReplaysWALToRestoreState

```mermaid
sequenceDiagram
    actor TestRunner
    participant RecoveryManager
    TestRunner->>RecoveryManager: recover()
    RecoveryManager->>RecoveryManager: apply WhenSystemCrashes
    RecoveryManager->>Dependency: invoke logic
    Dependency-->>RecoveryManager: success
    RecoveryManager-->>TestRunner: ReplaysWALToRestoreState
```

## 2. Recover_WhenUndoNeeded_RollsBackUncommittedTransactions

```mermaid
sequenceDiagram
    actor TestRunner
    participant RecoveryManager
    TestRunner->>RecoveryManager: recover()
    RecoveryManager->>RecoveryManager: apply WhenUndoNeeded
    RecoveryManager->>Dependency: invoke logic
    Dependency-->>RecoveryManager: success
    RecoveryManager-->>TestRunner: RollsBackUncommittedTransactions
```

## 3. AnalyzePhase_IdentifiesDirtyPagesAndActiveTx

```mermaid
sequenceDiagram
    actor TestRunner
    participant RecoveryManager
    TestRunner->>RecoveryManager: analyzePhase()
    RecoveryManager->>RecoveryManager: apply IdentifiesDirtyPagesAndActiveTx
    RecoveryManager->>Dependency: invoke logic
    Dependency-->>RecoveryManager: success
    RecoveryManager-->>TestRunner: Success
```

## 4. RedoPhase_ReappliesChangesFromLog

```mermaid
sequenceDiagram
    actor TestRunner
    participant RecoveryManager
    TestRunner->>RecoveryManager: redoPhase()
    RecoveryManager->>RecoveryManager: apply ReappliesChangesFromLog
    RecoveryManager->>Dependency: invoke logic
    Dependency-->>RecoveryManager: success
    RecoveryManager-->>TestRunner: Success
```

## 5. UndoPhase_RevertsChangesOfAbortedTx

```mermaid
sequenceDiagram
    actor TestRunner
    participant RecoveryManager
    TestRunner->>RecoveryManager: undoPhase()
    RecoveryManager->>RecoveryManager: apply RevertsChangesOfAbortedTx
    RecoveryManager->>Dependency: invoke logic
    Dependency-->>RecoveryManager: success
    RecoveryManager-->>TestRunner: Success
```

## 6. Recover_WhenWALFileCorrupt_ThrowsFatalException

```mermaid
sequenceDiagram
    actor TestRunner
    participant RecoveryManager
    TestRunner->>RecoveryManager: recover()
    RecoveryManager->>RecoveryManager: check WhenWALFileCorrupt
    RecoveryManager-->>RecoveryManager: condition failed
    RecoveryManager-->>TestRunner: throws FatalException
```

