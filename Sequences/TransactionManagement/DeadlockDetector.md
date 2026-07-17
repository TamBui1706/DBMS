# Sequence Diagrams: DeadlockDetector

## 🆕 Added Properties & Methods for `DeadlockDetector`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `DeadlockDetector` class in your Class Diagram with these:**

- **Property** added to `DeadlockDetector`: `waitForGraph` (Internal graph of waiting transactions)
- **Method** added to `DeadlockDetector`: `detectCycles()` (Runs cycle detection algorithm)

---

This file contains the detailed sequence diagrams for all unit tests of the **DeadlockDetector** class in the Transaction Management subsystem.

## 1. DetectAndResolve_WhenCycleFound_AbortsVictimTransaction

```mermaid
sequenceDiagram
    actor Test
    participant DeadlockDetector
    participant TransactionManager

    Test->>DeadlockDetector: detectAndResolve()
    DeadlockDetector->>DeadlockDetector: build waitForGraph
    DeadlockDetector->>DeadlockDetector: detectCycles()
    DeadlockDetector-->>DeadlockDetector: cycle found (victim = txId)
    DeadlockDetector->>TransactionManager: rollback(txId)
    TransactionManager-->>DeadlockDetector: success
    DeadlockDetector-->>Test: true (deadlock resolved)
```

## 2. DetectAndResolve_WhenNoCycleFound_DoesNothing

```mermaid
sequenceDiagram
    actor Test
    participant DeadlockDetector

    Test->>DeadlockDetector: detectAndResolve()
    DeadlockDetector->>DeadlockDetector: build waitForGraph
    DeadlockDetector->>DeadlockDetector: detectCycles()
    DeadlockDetector-->>DeadlockDetector: no cycle found
    DeadlockDetector-->>Test: false (no deadlock)
```

