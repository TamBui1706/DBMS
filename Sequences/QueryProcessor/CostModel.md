# Sequence Diagrams: CostModel

## 🆕 Added Properties & Methods for `CostModel`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `CostModel` class in your Class Diagram with these:**

- **Method** added to `CostModel`: `estimateIO(operator)`, `estimateCPU(operator)` (Internal cost heuristics)

---

This file contains the detailed sequence diagrams for all unit tests of the **CostModel** class in the Query Processor subsystem.

## 1. EstimateCost_CalculatesIOAndCPUCost

```mermaid
sequenceDiagram
    actor Test
    participant CostModel

    Test->>CostModel: estimateCost(operator)
    CostModel->>CostModel: estimateIO(operator)
    CostModel->>CostModel: estimateCPU(operator)
    CostModel->>CostModel: totalCost = IO + CPU
    CostModel-->>Test: return totalCost
```

## 2. EstimateCost_WhenUsingIndex_ReturnsLowerCostThanSeqScan

```mermaid
sequenceDiagram
    actor Test
    participant CostModel
    participant StatisticsManager

    Test->>CostModel: estimateCost(IndexScan)
    CostModel->>StatisticsManager: getStatistics(table)
    StatisticsManager-->>CostModel: stats
    CostModel->>CostModel: calc IndexCost
    Test->>CostModel: estimateCost(SeqScan)
    CostModel->>CostModel: calc SeqScanCost
    CostModel-->>Test: IndexCost < SeqScanCost (True)
```

