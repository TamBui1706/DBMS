# Sequence Diagrams: LockManager

## 🆕 Added Properties & Methods for `LockManager`
To support the detailed sequence logic for unit testing, please update the `LockManager` class in your Class Diagram with the following properties and methods:

- **Property** added to `LockManager`: `lockTable`
- **Property** added to `LockManager`: `deadlockDetector`
- **Method** added to `LockManager`: `acquireLock()`
- **Method** added to `LockManager`: `downgradeLock()`
- **Method** added to `LockManager`: `releaseLock()`
- **Method** added to `LockManager`: `upgradeLock()`

---

This file contains the detailed sequence diagrams for all 8 unit tests of the **LockManager** class.

## 1. AcquireLock_WhenResourceFree_GrantsLockInstantly

```mermaid
sequenceDiagram
    actor TestRunner
    participant LockManager
    TestRunner->>LockManager: acquireLock()
    LockManager->>LockManager: apply WhenResourceFree
    LockManager->>Dependency: invoke logic
    Dependency-->>LockManager: success
    LockManager-->>TestRunner: GrantsLockInstantly
```

## 2. AcquireLock_WhenResourceLocked_BlocksOrThrowsTimeout

```mermaid
sequenceDiagram
    actor TestRunner
    participant LockManager
    TestRunner->>LockManager: acquireLock()
    LockManager->>LockManager: check WhenResourceLocked
    LockManager-->>LockManager: condition failed
    LockManager-->>TestRunner: throws BlocksOrTimeout
```

## 3. ReleaseLock_WhenHoldingLock_FreesResourceAndWakesWaiters

```mermaid
sequenceDiagram
    actor TestRunner
    participant LockManager
    TestRunner->>LockManager: releaseLock()
    LockManager->>LockManager: apply WhenHoldingLock
    LockManager->>Dependency: invoke logic
    Dependency-->>LockManager: success
    LockManager-->>TestRunner: FreesResourceAndWakesWaiters
```

## 4. AcquireLock_WhenSharedLockExists_GrantsAnotherSharedLock

```mermaid
sequenceDiagram
    actor TestRunner
    participant LockManager
    TestRunner->>LockManager: acquireLock()
    LockManager->>LockManager: apply WhenSharedLockExists
    LockManager->>Dependency: invoke logic
    Dependency-->>LockManager: success
    LockManager-->>TestRunner: GrantsAnotherSharedLock
```

## 5. AcquireLock_WhenSharedLockExists_BlocksExclusiveLock

```mermaid
sequenceDiagram
    actor TestRunner
    participant LockManager
    TestRunner->>LockManager: acquireLock()
    LockManager->>LockManager: apply WhenSharedLockExists
    LockManager->>Dependency: invoke logic
    Dependency-->>LockManager: success
    LockManager-->>TestRunner: BlocksExclusiveLock
```

## 6. UpgradeLock_ConvertsSharedToExclusiveIfPossible

```mermaid
sequenceDiagram
    actor TestRunner
    participant LockManager
    TestRunner->>LockManager: upgradeLock()
    LockManager->>LockManager: apply ConvertsSharedToExclusiveIfPossible
    LockManager->>Dependency: invoke logic
    Dependency-->>LockManager: success
    LockManager-->>TestRunner: Success
```

## 7. DowngradeLock_ConvertsExclusiveToShared

```mermaid
sequenceDiagram
    actor TestRunner
    participant LockManager
    TestRunner->>LockManager: downgradeLock()
    LockManager->>LockManager: apply ConvertsExclusiveToShared
    LockManager->>Dependency: invoke logic
    Dependency-->>LockManager: success
    LockManager-->>TestRunner: Success
```

## 8. ReleaseLock_WhenNotHoldingLock_ThrowsException

```mermaid
sequenceDiagram
    actor TestRunner
    participant LockManager
    TestRunner->>LockManager: releaseLock()
    LockManager->>LockManager: check WhenNotHoldingLock
    LockManager-->>LockManager: condition failed
    LockManager-->>TestRunner: throws Exception
```

