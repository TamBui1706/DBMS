# Sequence Diagrams: Transaction

## 🆕 Added Properties & Methods for `Transaction`
To support the detailed sequence logic for unit testing, please update the `Transaction` class in your Class Diagram with the following properties and methods:

- **Property** added to `Transaction`: `transactionId`
- **Property** added to `Transaction`: `isolationLevel`
- **Property** added to `Transaction`: `state`
- **Property** added to `Transaction`: `savepoints (List)`
- **Property** added to `Transaction`: `heldLocks (List)`
- **Method** added to `Transaction`: `addLock()`
- **Method** added to `Transaction`: `releaseAllLocks()`
- **Method** added to `Transaction`: `rollbackToSavepoint()`
- **Method** added to `Transaction`: `setIsolationLevel()`
- **Method** added to `Transaction`: `setSavepoint()`

---

This file contains the detailed sequence diagrams for all 6 unit tests of the **Transaction** class.

## 1. Init_GeneratesUniqueTransactionId

```mermaid
sequenceDiagram
    actor TestRunner
    participant Transaction
    TestRunner->>Transaction: init()
    Transaction->>Transaction: apply GeneratesUniqueTransactionId
    Transaction->>Dependency: invoke logic
    Dependency-->>Transaction: success
    Transaction-->>TestRunner: Success
```

## 2. SetIsolationLevel_UpdatesTransactionProperties

```mermaid
sequenceDiagram
    actor TestRunner
    participant Transaction
    TestRunner->>Transaction: setIsolationLevel()
    Transaction->>Transaction: apply UpdatesTransactionProperties
    Transaction->>Dependency: invoke logic
    Dependency-->>Transaction: success
    Transaction-->>TestRunner: Success
```

## 3. AddLock_TracksLocksHeldByThisTransaction

```mermaid
sequenceDiagram
    actor TestRunner
    participant Transaction
    TestRunner->>Transaction: addLock()
    Transaction->>Transaction: apply TracksLocksHeldByThisTransaction
    Transaction->>Dependency: invoke logic
    Dependency-->>Transaction: success
    Transaction-->>TestRunner: Success
```

## 4. ReleaseAllLocks_CalledDuringCommitOrRollback

```mermaid
sequenceDiagram
    actor TestRunner
    participant Transaction
    TestRunner->>Transaction: releaseAllLocks()
    Transaction->>Transaction: apply CalledDuringCommitOrRollback
    Transaction->>Dependency: invoke logic
    Dependency-->>Transaction: success
    Transaction-->>TestRunner: Success
```

## 5. SetSavepoint_CreatesPartialRollbackMarker

```mermaid
sequenceDiagram
    actor TestRunner
    participant Transaction
    TestRunner->>Transaction: setSavepoint()
    Transaction->>Transaction: apply CreatesPartialRollbackMarker
    Transaction->>Dependency: invoke logic
    Dependency-->>Transaction: success
    Transaction-->>TestRunner: Success
```

## 6. RollbackToSavepoint_RevertsChangesAfterMarker

```mermaid
sequenceDiagram
    actor TestRunner
    participant Transaction
    TestRunner->>Transaction: rollbackToSavepoint()
    Transaction->>Transaction: apply RevertsChangesAfterMarker
    Transaction->>Dependency: invoke logic
    Dependency-->>Transaction: success
    Transaction-->>TestRunner: Success
```

