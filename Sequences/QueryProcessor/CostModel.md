# Sequence Diagrams: CostModel

## 🆕 Added Properties & Methods for `CostModel`
To support the detailed sequence logic for unit testing, please update the `CostModel` class in your Class Diagram with the following properties and methods:

- **Method** added to `CostModel`: `estimateCost()`
- **Method** added to `CostModel`: `estimateMemoryUsage()`
- **Method** added to `CostModel`: `updateStatistics()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **CostModel** class.

## 1. EstimateCost_CalculatesIOAndCPUCost

```mermaid
sequenceDiagram
    actor TestRunner
    participant CostModel
    TestRunner->>CostModel: estimateCost()
    CostModel->>CostModel: apply CalculatesIOAndCPUCost
    CostModel->>Dependency: invoke logic
    Dependency-->>CostModel: success
    CostModel-->>TestRunner: Success
```

## 2. EstimateCost_WhenUsingIndex_ReturnsLowerCostThanSeqScan

```mermaid
sequenceDiagram
    actor TestRunner
    participant CostModel
    TestRunner->>CostModel: estimateCost()
    CostModel->>CostModel: validate WhenUsingIndex
    CostModel->>CostModel: process EstimateCost
    CostModel-->>TestRunner: return LowerCostThanSeqScan
```

## 3. EstimateCost_ForNestedLoopJoin_IsHigherThanHashJoinForLargeTables

```mermaid
sequenceDiagram
    actor TestRunner
    participant CostModel
    TestRunner->>CostModel: estimateCost()
    CostModel->>CostModel: apply ForNestedLoopJoin
    CostModel->>Dependency: invoke logic
    Dependency-->>CostModel: success
    CostModel-->>TestRunner: IsHigherThanHashJoinForLargeTables
```

## 4. UpdateStatistics_AdjustsInternalWeightsBasedOnFeedback

```mermaid
sequenceDiagram
    actor TestRunner
    participant CostModel
    TestRunner->>CostModel: updateStatistics()
    CostModel->>CostModel: apply AdjustsInternalWeightsBasedOnFeedback
    CostModel->>Dependency: invoke logic
    Dependency-->>CostModel: success
    CostModel-->>TestRunner: Success
```

## 5. EstimateMemoryUsage_ForSortOperator_ReturnsExpectedBytes

```mermaid
sequenceDiagram
    actor TestRunner
    participant CostModel
    TestRunner->>CostModel: estimateMemoryUsage()
    CostModel->>CostModel: validate ForSortOperator
    CostModel->>CostModel: process EstimateMemoryUsage
    CostModel-->>TestRunner: return ExpectedBytes
```

