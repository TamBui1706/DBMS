# Sequence Diagrams: TransactionState

## 🆕 Added Properties & Methods for `TransactionState`
To support the detailed sequence logic for unit testing, please update the `TransactionState` class in your Class Diagram with the following properties and methods:

- *(No major new structural properties required, logic handled internally)*

---

This file contains the detailed sequence diagrams for all 1 unit tests of the **TransactionState** class.

## 1. EnumValues_IncludeActiveCommittedAborted

```mermaid
sequenceDiagram
    actor TestRunner
    participant TransactionState
    TestRunner->>TransactionState: enumValues()
    TransactionState->>TransactionState: apply IncludeActiveCommittedAborted
    TransactionState->>Dependency: invoke logic
    Dependency-->>TransactionState: success
    TransactionState-->>TestRunner: Success
```

