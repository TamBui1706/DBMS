# Sequence Diagrams: PhysicalPlan

## 🆕 Added Properties & Methods for `PhysicalPlan`
To support the detailed sequence logic for unit testing, please update the `PhysicalPlan` class in your Class Diagram with the following properties and methods:

- **Property** added to `PhysicalPlan`: `operators (List)`
- **Method** added to `PhysicalPlan`: `clone()`
- **Method** added to `PhysicalPlan`: `estimateTotalCost()`
- **Method** added to `PhysicalPlan`: `getRoot()`
- **Method** added to `PhysicalPlan`: `validatePipeline()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **PhysicalPlan** class.

## 1. Init_CreatesEmptyOperatorTree

```mermaid
sequenceDiagram
    actor TestRunner
    participant PhysicalPlan
    TestRunner->>PhysicalPlan: init()
    PhysicalPlan->>PhysicalPlan: apply CreatesEmptyOperatorTree
    PhysicalPlan->>Dependency: invoke logic
    Dependency-->>PhysicalPlan: success
    PhysicalPlan-->>TestRunner: Success
```

## 2. ValidatePipeline_EnsuresOperatorCompatibility

```mermaid
sequenceDiagram
    actor TestRunner
    participant PhysicalPlan
    TestRunner->>PhysicalPlan: validatePipeline()
    PhysicalPlan->>PhysicalPlan: apply EnsuresOperatorCompatibility
    PhysicalPlan->>Dependency: invoke logic
    Dependency-->>PhysicalPlan: success
    PhysicalPlan-->>TestRunner: Success
```

## 3. EstimateTotalCost_SumsCostOfAllOperators

```mermaid
sequenceDiagram
    actor TestRunner
    participant PhysicalPlan
    TestRunner->>PhysicalPlan: estimateTotalCost()
    PhysicalPlan->>PhysicalPlan: apply SumsCostOfAllOperators
    PhysicalPlan->>Dependency: invoke logic
    Dependency-->>PhysicalPlan: success
    PhysicalPlan-->>TestRunner: Success
```

## 4. GetRoot_ReturnsTopOperator

```mermaid
sequenceDiagram
    actor TestRunner
    participant PhysicalPlan
    TestRunner->>PhysicalPlan: getRoot()
    PhysicalPlan->>PhysicalPlan: apply ReturnsTopOperator
    PhysicalPlan->>Dependency: invoke logic
    Dependency-->>PhysicalPlan: success
    PhysicalPlan-->>TestRunner: Success
```

## 5. Clone_CreatesIsolatedExecutionInstance

```mermaid
sequenceDiagram
    actor TestRunner
    participant PhysicalPlan
    TestRunner->>PhysicalPlan: clone()
    PhysicalPlan->>PhysicalPlan: apply CreatesIsolatedExecutionInstance
    PhysicalPlan->>Dependency: invoke logic
    Dependency-->>PhysicalPlan: success
    PhysicalPlan-->>TestRunner: Success
```

