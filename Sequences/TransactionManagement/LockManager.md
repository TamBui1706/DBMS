# Sequence Diagrams: LockManager

## 🆕 Added Properties & Methods for `LockManager`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `LockManager` class in your Class Diagram with these:**

- **Property** added to `LockManager`: `lockTable` (Reference to the LockTable object)
- **Property** added to `LockManager`: `deadlockDetector` (Reference to the DeadlockDetector)
- **Method** added to `LockManager`: `checkConflict(resource)` (Checks if lock can be granted immediately)

---

This file contains the detailed sequence diagrams for all unit tests of the **LockManager** class in the Transaction Management subsystem.

## 1. AcquireLock_WhenResourceFree_GrantsLockInstantly

```mermaid
sequenceDiagram
    actor Test
    participant LockManager
    participant LockTable

    Test->>LockManager: acquireLock(resource, txId)
    LockManager->>LockManager: checkConflict(resource)
    LockManager-->>LockManager: no conflict
    LockManager->>LockTable: addLock(resource, txId)
    LockTable-->>LockManager: success
    LockManager-->>Test: success
```

## 2. AcquireLock_WhenResourceLocked_BlocksOrThrowsTimeout

```mermaid
sequenceDiagram
    actor Test
    participant LockManager
    participant DeadlockDetector

    Test->>LockManager: acquireLock(resource, txId2)
    LockManager->>LockManager: checkConflict(resource)
    LockManager-->>LockManager: conflict (held by txId1)
    LockManager->>DeadlockDetector: addEdge(txId2, txId1)
    LockManager->>LockManager: wait(TIMEOUT)
    LockManager-->>Test: throws TimeoutException (or blocks)
```

## 3. ReleaseLock_WhenHoldingLock_FreesResourceAndWakesWaiters

```mermaid
sequenceDiagram
    actor Test
    participant LockManager
    participant LockTable

    Test->>LockManager: releaseLock(resource, txId)
    LockManager->>LockTable: removeLock(resource, txId)
    LockTable-->>LockManager: success
    LockManager->>LockManager: notify waiting transactions
    LockManager-->>Test: success
```

