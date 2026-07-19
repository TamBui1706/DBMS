# Sequence Diagrams: LogicalOperator

## 🆕 Added Properties & Methods for `LogicalOperator`
To support the detailed sequence logic for unit testing, please update the `LogicalOperator` class in your Class Diagram with the following properties and methods:

- *(No major new structural properties required, logic handled internally)*

---

This file contains the detailed sequence diagrams for all 1 unit tests of the **LogicalOperator** class.

## 1. Instantiation_OfAbstractClass_FailsWithTypeError

```mermaid
sequenceDiagram
    actor TestRunner
    participant LogicalOperator
    TestRunner->>LogicalOperator: instantiation()
    LogicalOperator->>LogicalOperator: check OfAbstractClass
    LogicalOperator-->>LogicalOperator: condition failed
    LogicalOperator-->>TestRunner: throws FailsWithTypeError
```

