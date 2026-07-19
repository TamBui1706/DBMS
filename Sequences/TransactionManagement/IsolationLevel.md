# Sequence Diagrams: IsolationLevel

## 🆕 Added Properties & Methods for `IsolationLevel`
To support the detailed sequence logic for unit testing, please update the `IsolationLevel` class in your Class Diagram with the following properties and methods:

- *(No major new structural properties required, logic handled internally)*

---

This file contains the detailed sequence diagrams for all 1 unit tests of the **IsolationLevel** class.

## 1. EnumValues_IncludeReadCommittedAndSerializable

```mermaid
sequenceDiagram
    actor TestRunner
    participant IsolationLevel
    TestRunner->>IsolationLevel: enumValues()
    IsolationLevel->>IsolationLevel: apply IncludeReadCommittedAndSerializable
    IsolationLevel->>Dependency: invoke logic
    Dependency-->>IsolationLevel: success
    IsolationLevel-->>TestRunner: Success
```

