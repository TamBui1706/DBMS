# Sequence Diagrams: TransactionManager

## 🆕 Added Properties & Methods for `TransactionManager`
To support the detailed sequence logic for unit testing, please update the `TransactionManager` class in your Class Diagram with the following properties and methods:

- **Property** added to `TransactionManager`: `activeTransactions (Dict)`
- **Property** added to `TransactionManager`: `walManager`
- **Method** added to `TransactionManager`: `beginTransaction()`
- **Method** added to `TransactionManager`: `commit()`
- **Method** added to `TransactionManager`: `forceRollbackAll()`
- **Method** added to `TransactionManager`: `getActiveTransactions()`
- **Method** added to `TransactionManager`: `resumeTransaction()`
- **Method** added to `TransactionManager`: `rollback()`
- **Method** added to `TransactionManager`: `suspendTransaction()`

---

This file contains the detailed sequence diagrams for all 8 unit tests of the **TransactionManager** class.

## 1. BeginTransaction_CreatesAndRegistersNewActiveTransaction

```mermaid
sequenceDiagram
    actor TestRunner
    participant TransactionManager
    TestRunner->>TransactionManager: beginTransaction()
    TransactionManager->>TransactionManager: apply CreatesAndRegistersNewActiveTransaction
    TransactionManager->>Dependency: invoke logic
    Dependency-->>TransactionManager: success
    TransactionManager-->>TestRunner: Success
```

## 2. Commit_WhenSuccessful_WritesToLogAndChangesState

```mermaid
sequenceDiagram
    actor TestRunner
    participant TransactionManager
    TestRunner->>TransactionManager: commit()
    TransactionManager->>TransactionManager: apply WhenSuccessful
    TransactionManager->>Dependency: invoke logic
    Dependency-->>TransactionManager: success
    TransactionManager-->>TestRunner: WritesToLogAndChangesState
```

## 3. Rollback_WhenCalled_RevertsAllModifications

```mermaid
sequenceDiagram
    actor TestRunner
    participant TransactionManager
    TestRunner->>TransactionManager: rollback()
    TransactionManager->>TransactionManager: apply WhenCalled
    TransactionManager->>Dependency: invoke logic
    Dependency-->>TransactionManager: success
    TransactionManager-->>TestRunner: RevertsAllModifications
```

## 4. Commit_WhenValidationFails_ForcesRollback

```mermaid
sequenceDiagram
    actor TestRunner
    participant TransactionManager
    TestRunner->>TransactionManager: commit()
    TransactionManager->>TransactionManager: apply WhenValidationFails
    TransactionManager->>Dependency: invoke logic
    Dependency-->>TransactionManager: success
    TransactionManager-->>TestRunner: ForcesRollback
```

## 5. GetActiveTransactions_ReturnsListOfCurrentlyRunningTx

```mermaid
sequenceDiagram
    actor TestRunner
    participant TransactionManager
    TestRunner->>TransactionManager: getActiveTransactions()
    TransactionManager->>TransactionManager: apply ReturnsListOfCurrentlyRunningTx
    TransactionManager->>Dependency: invoke logic
    Dependency-->>TransactionManager: success
    TransactionManager-->>TestRunner: Success
```

## 6. SuspendTransaction_TemporarilyHaltsExecution

```mermaid
sequenceDiagram
    actor TestRunner
    participant TransactionManager
    TestRunner->>TransactionManager: suspendTransaction()
    TransactionManager->>TransactionManager: apply TemporarilyHaltsExecution
    TransactionManager->>Dependency: invoke logic
    Dependency-->>TransactionManager: success
    TransactionManager-->>TestRunner: Success
```

## 7. ResumeTransaction_ContinuesSuspendedExecution

```mermaid
sequenceDiagram
    actor TestRunner
    participant TransactionManager
    TestRunner->>TransactionManager: resumeTransaction()
    TransactionManager->>TransactionManager: apply ContinuesSuspendedExecution
    TransactionManager->>Dependency: invoke logic
    Dependency-->>TransactionManager: success
    TransactionManager-->>TestRunner: Success
```

## 8. ForceRollbackAll_UsedDuringServerShutdown

```mermaid
sequenceDiagram
    actor TestRunner
    participant TransactionManager
    TestRunner->>TransactionManager: forceRollbackAll()
    TransactionManager->>TransactionManager: apply UsedDuringServerShutdown
    TransactionManager->>Dependency: invoke logic
    Dependency-->>TransactionManager: success
    TransactionManager-->>TestRunner: Success
```

