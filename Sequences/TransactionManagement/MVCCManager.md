# Sequence Diagrams: MVCCManager

## 🆕 Added Properties & Methods for `MVCCManager`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `MVCCManager` class in your Class Diagram with these:**

- **Property** added to `MVCCManager`: `versionChain` (Stores multiversion records)
- **Method** added to `MVCCManager`: `findVisibleVersion(txId)` (Resolves the correct version based on IsolationLevel)

---

This file contains the detailed sequence diagrams for all unit tests of the **MVCCManager** class in the Transaction Management subsystem.

## 1. CreateVersion_AppendsNewRecordVersionToChain

```mermaid
sequenceDiagram
    actor Test
    participant MVCCManager

    Test->>MVCCManager: createVersion(recordId, txId, newData)
    MVCCManager->>MVCCManager: self.versionChain.append(newVersion)
    MVCCManager-->>Test: success
```

## 2. GarbageCollect_RemovesVersionsInvisibleToAllActiveTransactions

```mermaid
sequenceDiagram
    actor Test
    participant MVCCManager
    participant TransactionManager

    Test->>MVCCManager: garbageCollect()
    MVCCManager->>TransactionManager: getOldestActiveTxId()
    TransactionManager-->>MVCCManager: oldestTxId
    MVCCManager->>MVCCManager: remove versions committed before oldestTxId
    MVCCManager-->>Test: success (reclaimed space)
```

