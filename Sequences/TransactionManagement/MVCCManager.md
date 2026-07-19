# Sequence Diagrams: MVCCManager

## 🆕 Added Properties & Methods for `MVCCManager`
To support the detailed sequence logic for unit testing, please update the `MVCCManager` class in your Class Diagram with the following properties and methods:

- **Property** added to `MVCCManager`: `versionChain (List)`
- **Method** added to `MVCCManager`: `createVersion()`
- **Method** added to `MVCCManager`: `detectWriteConflict()`
- **Method** added to `MVCCManager`: `garbageCollect()`
- **Method** added to `MVCCManager`: `readVersion()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **MVCCManager** class.

## 1. CreateVersion_AppendsNewRecordVersionToChain

```mermaid
sequenceDiagram
    actor TestRunner
    participant MVCCManager
    TestRunner->>MVCCManager: createVersion()
    MVCCManager->>MVCCManager: apply AppendsNewRecordVersionToChain
    MVCCManager->>Dependency: invoke logic
    Dependency-->>MVCCManager: success
    MVCCManager-->>TestRunner: Success
```

## 2. GarbageCollect_RemovesVersionsInvisibleToAllActiveTransactions

```mermaid
sequenceDiagram
    actor TestRunner
    participant MVCCManager
    TestRunner->>MVCCManager: garbageCollect()
    MVCCManager->>MVCCManager: apply RemovesVersionsInvisibleToAllActiveTransactions
    MVCCManager->>Dependency: invoke logic
    Dependency-->>MVCCManager: success
    MVCCManager-->>TestRunner: Success
```

## 3. ReadVersion_ReturnsCorrectDataBasedOnTxSnapshot

```mermaid
sequenceDiagram
    actor TestRunner
    participant MVCCManager
    TestRunner->>MVCCManager: readVersion()
    MVCCManager->>MVCCManager: apply ReturnsCorrectDataBasedOnTxSnapshot
    MVCCManager->>Dependency: invoke logic
    Dependency-->>MVCCManager: success
    MVCCManager-->>TestRunner: Success
```

## 4. DetectWriteConflict_WhenTwoTxUpdateSameRecord_ThrowsException

```mermaid
sequenceDiagram
    actor TestRunner
    participant MVCCManager
    TestRunner->>MVCCManager: detectWriteConflict()
    MVCCManager->>MVCCManager: check WhenTwoTxUpdateSameRecord
    MVCCManager-->>MVCCManager: condition failed
    MVCCManager-->>TestRunner: throws Exception
```

## 5. ReadVersion_WhenNoVisibleVersion_ReturnsNull

```mermaid
sequenceDiagram
    actor TestRunner
    participant MVCCManager
    TestRunner->>MVCCManager: readVersion()
    MVCCManager->>MVCCManager: validate WhenNoVisibleVersion
    MVCCManager->>MVCCManager: process ReadVersion
    MVCCManager-->>TestRunner: return Null
```

