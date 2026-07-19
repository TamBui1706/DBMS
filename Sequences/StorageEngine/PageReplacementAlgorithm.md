# Sequence Diagrams: PageReplacementAlgorithm

## 🆕 Added Properties & Methods for `PageReplacementAlgorithm`
To support the detailed sequence logic for unit testing, please update the `PageReplacementAlgorithm` class in your Class Diagram with the following properties and methods:

- *(No major new structural properties required, logic handled internally)*

---

This file contains the detailed sequence diagrams for all 1 unit tests of the **PageReplacementAlgorithm** class.

## 1. Instantiation_OfInterface_FailsWithTypeError

```mermaid
sequenceDiagram
    actor TestRunner
    participant PageReplacementAlgorithm
    TestRunner->>PageReplacementAlgorithm: instantiation()
    PageReplacementAlgorithm->>PageReplacementAlgorithm: check OfInterface
    PageReplacementAlgorithm-->>PageReplacementAlgorithm: condition failed
    PageReplacementAlgorithm-->>TestRunner: throws FailsWithTypeError
```

