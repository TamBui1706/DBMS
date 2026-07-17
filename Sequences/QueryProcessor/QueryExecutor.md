# Sequence Diagrams: QueryExecutor

## 🆕 Added Properties & Methods for `QueryExecutor`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `QueryExecutor` class in your Class Diagram with these:**

- **Property** added to `QueryExecutor`: `memoryLimit` (Threshold for memory usage)
- **Method** added to `QueryExecutor`: `executePipeline(physicalPlan)` (Runs operators)
- **Method** added to `QueryExecutor`: `spillToDisk()` (Called when memory exceeded)

---

This file contains the detailed sequence diagrams for all unit tests of the **QueryExecutor** class in the Query Processor subsystem.

## 1. ExecutePlan_WhenValidPhysicalPlan_IteratesAndYieldsResults

```mermaid
sequenceDiagram
    actor Test
    participant QueryExecutor
    participant PhysicalPlan

    Test->>QueryExecutor: executePlan(physicalPlan)
    QueryExecutor->>QueryExecutor: executePipeline(physicalPlan)
    QueryExecutor->>PhysicalPlan: getRootOperator()
    PhysicalPlan-->>QueryExecutor: rootOp
    QueryExecutor->>QueryExecutor: execute tree
    QueryExecutor-->>Test: return ResultData
```

## 2. ExecutePlan_WhenMemoryExceeded_SpillsToDiskOrThrows

```mermaid
sequenceDiagram
    actor Test
    participant QueryExecutor
    participant StorageEngine

    Test->>QueryExecutor: executePlan(heavyPhysicalPlan)
    QueryExecutor->>QueryExecutor: monitorMemoryUsage()
    QueryExecutor->>QueryExecutor: check usage > self.memoryLimit
    QueryExecutor-->>QueryExecutor: true
    QueryExecutor->>QueryExecutor: spillToDisk()
    QueryExecutor->>StorageEngine: writeTempFile(buffer)
    StorageEngine-->>QueryExecutor: success
    QueryExecutor-->>Test: return ResultData (or throws OutOfMemoryException)
```

