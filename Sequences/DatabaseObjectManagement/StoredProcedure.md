# Sequence Diagrams: StoredProcedure

## 🆕 Added Properties & Methods for `StoredProcedure`
To support the detailed sequence logic for unit testing, please update the `StoredProcedure` class in your Class Diagram with the following properties and methods:

- **Property** added to `StoredProcedure`: `parameters (List)`
- **Method** added to `StoredProcedure`: `compile()`
- **Method** added to `StoredProcedure`: `drop()`
- **Method** added to `StoredProcedure`: `execute()`

---

This file contains the detailed sequence diagrams for all 6 unit tests of the **StoredProcedure** class.

## 1. Execute_WhenValidParametersProvided_RunsLogic

```mermaid
sequenceDiagram
    actor TestRunner
    participant StoredProcedure
    TestRunner->>StoredProcedure: execute()
    StoredProcedure->>StoredProcedure: apply WhenValidParametersProvided
    StoredProcedure->>Dependency: invoke logic
    Dependency-->>StoredProcedure: success
    StoredProcedure-->>TestRunner: RunsLogic
```

## 2. Execute_WhenTypeMismatchInParams_ThrowsException

```mermaid
sequenceDiagram
    actor TestRunner
    participant StoredProcedure
    TestRunner->>StoredProcedure: execute()
    StoredProcedure->>StoredProcedure: check WhenTypeMismatchInParams
    StoredProcedure-->>StoredProcedure: condition failed
    StoredProcedure-->>TestRunner: throws Exception
```

## 3. Execute_WhenMissingParameters_ThrowsArgumentException

```mermaid
sequenceDiagram
    actor TestRunner
    participant StoredProcedure
    TestRunner->>StoredProcedure: execute()
    StoredProcedure->>StoredProcedure: check WhenMissingParameters
    StoredProcedure-->>StoredProcedure: condition failed
    StoredProcedure-->>TestRunner: throws ArgumentException
```

## 4. Compile_ValidatesSyntaxAndDependencies

```mermaid
sequenceDiagram
    actor TestRunner
    participant StoredProcedure
    TestRunner->>StoredProcedure: compile()
    StoredProcedure->>StoredProcedure: apply ValidatesSyntaxAndDependencies
    StoredProcedure->>Dependency: invoke logic
    Dependency-->>StoredProcedure: success
    StoredProcedure-->>TestRunner: Success
```

## 5. Drop_RemovesProcedureFromCatalog

```mermaid
sequenceDiagram
    actor TestRunner
    participant StoredProcedure
    TestRunner->>StoredProcedure: drop()
    StoredProcedure->>StoredProcedure: apply RemovesProcedureFromCatalog
    StoredProcedure->>Dependency: invoke logic
    Dependency-->>StoredProcedure: success
    StoredProcedure-->>TestRunner: Success
```

## 6. Execute_WhenProcedureTimesOut_KillsExecution

```mermaid
sequenceDiagram
    actor TestRunner
    participant StoredProcedure
    TestRunner->>StoredProcedure: execute()
    StoredProcedure->>StoredProcedure: apply WhenProcedureTimesOut
    StoredProcedure->>Dependency: invoke logic
    Dependency-->>StoredProcedure: success
    StoredProcedure-->>TestRunner: KillsExecution
```

