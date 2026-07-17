# Sequence Diagrams: StoredProcedure

## 🆕 Added Properties & Methods for `StoredProcedure`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `StoredProcedure` class in your Class Diagram with these:**

- **Property** added to `StoredProcedure`: `parameters` (List of expected parameter types)
- **Method** added to `StoredProcedure`: `validateParams(args)` (Validates types before execution)

---

This file contains the detailed sequence diagrams for all unit tests of the **StoredProcedure** class in the Database Object Management subsystem.

## 1. Execute_WhenValidParametersProvided_RunsLogic

```mermaid
sequenceDiagram
    actor Test
    participant StoredProcedure
    participant QueryProcessor

    Test->>StoredProcedure: execute(args)
    StoredProcedure->>StoredProcedure: validateParams(args)
    StoredProcedure-->>StoredProcedure: valid
    StoredProcedure->>QueryProcessor: runLogic(args)
    QueryProcessor-->>StoredProcedure: result
    StoredProcedure-->>Test: return result
```

## 2. Execute_WhenTypeMismatchInParams_ThrowsException

```mermaid
sequenceDiagram
    actor Test
    participant StoredProcedure

    Test->>StoredProcedure: execute(invalidArgs)
    StoredProcedure->>StoredProcedure: validateParams(invalidArgs)
    StoredProcedure-->>StoredProcedure: type mismatch
    StoredProcedure-->>Test: throws TypeMismatchException
```

