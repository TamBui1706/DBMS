# Sequence Diagrams: LockTable

## 🆕 Added Properties & Methods for `LockTable`
To support the detailed sequence logic for unit testing, please update the `LockTable` class in your Class Diagram with the following properties and methods:

- **Property** added to `LockTable`: `locks (Dict)`
- **Method** added to `LockTable`: `addLock()`
- **Method** added to `LockTable`: `clear()`
- **Method** added to `LockTable`: `countLocks()`
- **Method** added to `LockTable`: `getLocks()`
- **Method** added to `LockTable`: `removeLock()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **LockTable** class.

## 1. GetLocks_ReturnsCurrentLockInformation

```mermaid
sequenceDiagram
    actor TestRunner
    participant LockTable
    TestRunner->>LockTable: getLocks()
    LockTable->>LockTable: apply ReturnsCurrentLockInformation
    LockTable->>Dependency: invoke logic
    Dependency-->>LockTable: success
    LockTable-->>TestRunner: Success
```

## 2. AddLock_RegistersNewLockForResource

```mermaid
sequenceDiagram
    actor TestRunner
    participant LockTable
    TestRunner->>LockTable: addLock()
    LockTable->>LockTable: apply RegistersNewLockForResource
    LockTable->>Dependency: invoke logic
    Dependency-->>LockTable: success
    LockTable-->>TestRunner: Success
```

## 3. RemoveLock_DeletesRegistration

```mermaid
sequenceDiagram
    actor TestRunner
    participant LockTable
    TestRunner->>LockTable: removeLock()
    LockTable->>LockTable: apply DeletesRegistration
    LockTable->>Dependency: invoke logic
    Dependency-->>LockTable: success
    LockTable-->>TestRunner: Success
```

## 4. Clear_RemovesAllLocksDuringSystemReset

```mermaid
sequenceDiagram
    actor TestRunner
    participant LockTable
    TestRunner->>LockTable: clear()
    LockTable->>LockTable: apply RemovesAllLocksDuringSystemReset
    LockTable->>Dependency: invoke logic
    Dependency-->>LockTable: success
    LockTable-->>TestRunner: Success
```

## 5. CountLocks_ForSpecificTransactionId

```mermaid
sequenceDiagram
    actor TestRunner
    participant LockTable
    TestRunner->>LockTable: countLocks()
    LockTable->>LockTable: apply ForSpecificTransactionId
    LockTable->>Dependency: invoke logic
    Dependency-->>LockTable: success
    LockTable-->>TestRunner: Success
```

