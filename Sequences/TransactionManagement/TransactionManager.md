# Sequence Diagrams: TransactionManager

## 🆕 Added Properties & Methods for `TransactionManager`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `TransactionManager` class in your Class Diagram with these:**

- **Property** added to `TransactionManager`: `activeTransactions` (Dictionary mapping TxId to Transaction)
- **Property** added to `TransactionManager`: `walManager` (Reference to Write-Ahead Log manager)
- **Method** added to `TransactionManager`: `validateTransaction(txId)` (Checks constraints before commit)

---

This file contains the detailed sequence diagrams for all unit tests of the **TransactionManager** class in the Transaction Management subsystem.

## 1. BeginTransaction_CreatesAndRegistersNewActiveTransaction

```mermaid
sequenceDiagram
    actor Test
    participant TransactionManager
    participant Transaction

    Test->>TransactionManager: beginTransaction()
    TransactionManager->>Transaction: new Transaction()
    Transaction-->>TransactionManager: txInstance (state=ACTIVE)
    TransactionManager->>TransactionManager: activeTransactions.put(txInstance.id, txInstance)
    TransactionManager-->>Test: return txInstance
```

## 2. Commit_WhenSuccessful_WritesToLogAndChangesState

```mermaid
sequenceDiagram
    actor Test
    participant TransactionManager
    participant WALManager

    Test->>TransactionManager: commit(txId)
    TransactionManager->>TransactionManager: validateTransaction(txId)
    TransactionManager-->>TransactionManager: valid
    TransactionManager->>WALManager: flushLog(txId)
    WALManager-->>TransactionManager: success
    TransactionManager->>TransactionManager: update tx.state = COMMITTED
    TransactionManager->>TransactionManager: activeTransactions.remove(txId)
    TransactionManager-->>Test: success
```

## 3. Rollback_WhenCalled_RevertsAllModifications

```mermaid
sequenceDiagram
    actor Test
    participant TransactionManager
    participant WALManager

    Test->>TransactionManager: rollback(txId)
    TransactionManager->>WALManager: undoLogs(txId)
    WALManager-->>TransactionManager: success
    TransactionManager->>TransactionManager: update tx.state = ABORTED
    TransactionManager->>TransactionManager: activeTransactions.remove(txId)
    TransactionManager-->>Test: success
```

## 4. Commit_WhenValidationFails_ForcesRollback

```mermaid
sequenceDiagram
    actor Test
    participant TransactionManager
    participant WALManager

    Test->>TransactionManager: commit(txId)
    TransactionManager->>TransactionManager: validateTransaction(txId)
    TransactionManager-->>TransactionManager: conflict detected
    TransactionManager->>WALManager: undoLogs(txId)
    WALManager-->>TransactionManager: success
    TransactionManager->>TransactionManager: update tx.state = ABORTED
    TransactionManager-->>Test: throws ValidationFailedException (forced rollback)
```

