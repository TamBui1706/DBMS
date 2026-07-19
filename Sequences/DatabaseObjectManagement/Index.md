# Sequence Diagrams: Index

## 🆕 Added Properties & Methods for `Index`
To support the detailed sequence logic for unit testing, please update the `Index` class in your Class Diagram with the following properties and methods:

- *(No major new structural properties required, logic handled internally)*

---

This file contains the detailed sequence diagrams for all 1 unit tests of the **Index** class.

## 1. Instantiation_OfAbstractClass_FailsWithTypeError

```mermaid
sequenceDiagram
    actor TestRunner
    participant Index
    TestRunner->>Index: instantiation()
    Index->>Index: check OfAbstractClass
    Index-->>Index: condition failed
    Index-->>TestRunner: throws FailsWithTypeError
```

