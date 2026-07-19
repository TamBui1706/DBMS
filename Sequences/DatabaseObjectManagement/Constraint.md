# Sequence Diagrams: Constraint

## 🆕 Added Properties & Methods for `Constraint`
To support the detailed sequence logic for unit testing, please update the `Constraint` class in your Class Diagram with the following properties and methods:

- *(No major new structural properties required, logic handled internally)*

---

This file contains the detailed sequence diagrams for all 1 unit tests of the **Constraint** class.

## 1. Instantiation_OfAbstractClass_FailsWithTypeError

```mermaid
sequenceDiagram
    actor TestRunner
    participant Constraint
    TestRunner->>Constraint: instantiation()
    Constraint->>Constraint: check OfAbstractClass
    Constraint-->>Constraint: condition failed
    Constraint-->>TestRunner: throws FailsWithTypeError
```

