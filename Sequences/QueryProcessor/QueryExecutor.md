# Sequence Diagrams: QueryExecutor

## 🆕 Added Properties & Methods for `QueryExecutor`
To support the detailed sequence logic for unit testing, please update the `QueryExecutor` class in your Class Diagram with the following properties and methods:

- **Property** added to `QueryExecutor`: `memoryLimit (Int)`
- **Method** added to `QueryExecutor`: `close()`
- **Method** added to `QueryExecutor`: `executePlan()`
- **Method** added to `QueryExecutor`: `initialize()`
- **Method** added to `QueryExecutor`: `streamResults()`

---

This file contains the detailed sequence diagrams for all 6 unit tests of the **QueryExecutor** class.

## 1. ExecutePlan_WhenValidPhysicalPlan_IteratesAndYieldsResults

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryExecutor
    TestRunner->>QueryExecutor: executePlan()
    QueryExecutor->>QueryExecutor: apply WhenValidPhysicalPlan
    QueryExecutor->>Dependency: invoke logic
    Dependency-->>QueryExecutor: success
    QueryExecutor-->>TestRunner: IteratesAndYieldsResults
```

## 2. ExecutePlan_WhenMemoryExceeded_SpillsToDiskOrThrows

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryExecutor
    TestRunner->>QueryExecutor: executePlan()
    QueryExecutor->>QueryExecutor: check WhenMemoryExceeded
    QueryExecutor-->>QueryExecutor: condition failed
    QueryExecutor-->>TestRunner: throws SpillsToDiskOr
```

## 3. ExecutePlan_WhenCanceledByUser_AbortsImmediately

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryExecutor
    TestRunner->>QueryExecutor: executePlan()
    QueryExecutor->>QueryExecutor: apply WhenCanceledByUser
    QueryExecutor->>Dependency: invoke logic
    Dependency-->>QueryExecutor: success
    QueryExecutor-->>TestRunner: AbortsImmediately
```

## 4. StreamResults_YieldsBatchesInsteadOfLoadingAllIntoMemory

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryExecutor
    TestRunner->>QueryExecutor: streamResults()
    QueryExecutor->>QueryExecutor: apply YieldsBatchesInsteadOfLoadingAllIntoMemory
    QueryExecutor->>Dependency: invoke logic
    Dependency-->>QueryExecutor: success
    QueryExecutor-->>TestRunner: Success
```

## 5. Initialize_AllocatesRequiredTempSpace

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryExecutor
    TestRunner->>QueryExecutor: initialize()
    QueryExecutor->>QueryExecutor: apply AllocatesRequiredTempSpace
    QueryExecutor->>Dependency: invoke logic
    Dependency-->>QueryExecutor: success
    QueryExecutor-->>TestRunner: Success
```

## 6. Close_ReleasesAllInternalIterators

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryExecutor
    TestRunner->>QueryExecutor: close()
    QueryExecutor->>QueryExecutor: apply ReleasesAllInternalIterators
    QueryExecutor->>Dependency: invoke logic
    Dependency-->>QueryExecutor: success
    QueryExecutor-->>TestRunner: Success
```

