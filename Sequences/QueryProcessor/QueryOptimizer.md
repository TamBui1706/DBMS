# Sequence Diagrams: QueryOptimizer

## 🆕 Added Properties & Methods for `QueryOptimizer`
To support the detailed sequence logic for unit testing, please update the `QueryOptimizer` class in your Class Diagram with the following properties and methods:

- **Method** added to `QueryOptimizer`: `optimize()`

---

This file contains the detailed sequence diagrams for all 7 unit tests of the **QueryOptimizer** class.

## 1. Optimize_WhenGivenLogicalPlan_TransformsToPhysicalPlan

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryOptimizer
    TestRunner->>QueryOptimizer: optimize()
    QueryOptimizer->>QueryOptimizer: apply WhenGivenLogicalPlan
    QueryOptimizer->>Dependency: invoke logic
    Dependency-->>QueryOptimizer: success
    QueryOptimizer-->>TestRunner: TransformsToPhysicalPlan
```

## 2. Optimize_AppliesFilterPushdownRule

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryOptimizer
    TestRunner->>QueryOptimizer: optimize()
    QueryOptimizer->>QueryOptimizer: apply AppliesFilterPushdownRule
    QueryOptimizer->>Dependency: invoke logic
    Dependency-->>QueryOptimizer: success
    QueryOptimizer-->>TestRunner: Success
```

## 3. Optimize_AppliesJoinReorderingForEfficiency

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryOptimizer
    TestRunner->>QueryOptimizer: optimize()
    QueryOptimizer->>QueryOptimizer: apply AppliesJoinReorderingForEfficiency
    QueryOptimizer->>Dependency: invoke logic
    Dependency-->>QueryOptimizer: success
    QueryOptimizer-->>TestRunner: Success
```

## 4. Optimize_ChoosesIndexScanOverSeqScanWhenSelective

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryOptimizer
    TestRunner->>QueryOptimizer: optimize()
    QueryOptimizer->>QueryOptimizer: apply ChoosesIndexScanOverSeqScanWhenSelective
    QueryOptimizer->>Dependency: invoke logic
    Dependency-->>QueryOptimizer: success
    QueryOptimizer-->>TestRunner: Success
```

## 5. Optimize_EliminatesDeadCodeOrAlwaysFalseConditions

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryOptimizer
    TestRunner->>QueryOptimizer: optimize()
    QueryOptimizer->>QueryOptimizer: apply EliminatesDeadCodeOrAlwaysFalseConditions
    QueryOptimizer->>Dependency: invoke logic
    Dependency-->>QueryOptimizer: success
    QueryOptimizer-->>TestRunner: Success
```

## 6. Optimize_FlattensUnnecessarySubqueries

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryOptimizer
    TestRunner->>QueryOptimizer: optimize()
    QueryOptimizer->>QueryOptimizer: apply FlattensUnnecessarySubqueries
    QueryOptimizer->>Dependency: invoke logic
    Dependency-->>QueryOptimizer: success
    QueryOptimizer-->>TestRunner: Success
```

## 7. Optimize_WhenStatsMissing_DefaultsToHeuristicRules

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryOptimizer
    TestRunner->>QueryOptimizer: optimize()
    QueryOptimizer->>QueryOptimizer: apply WhenStatsMissing
    QueryOptimizer->>Dependency: invoke logic
    Dependency-->>QueryOptimizer: success
    QueryOptimizer-->>TestRunner: DefaultsToHeuristicRules
```

