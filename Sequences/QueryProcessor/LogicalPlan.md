# Sequence Diagrams: LogicalPlan

## 🆕 Added Properties & Methods for `LogicalPlan`
To support the detailed sequence logic for unit testing, please update the `LogicalPlan` class in your Class Diagram with the following properties and methods:

- **Property** added to `LogicalPlan`: `operators (List)`
- **Method** added to `LogicalPlan`: `addOperator()`
- **Method** added to `LogicalPlan`: `getLeaves()`
- **Method** added to `LogicalPlan`: `printTree()`
- **Method** added to `LogicalPlan`: `validate()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **LogicalPlan** class.

## 1. Init_CreatesEmptyOperatorTree

```mermaid
sequenceDiagram
    actor TestRunner
    participant LogicalPlan
    TestRunner->>LogicalPlan: init()
    LogicalPlan->>LogicalPlan: apply CreatesEmptyOperatorTree
    LogicalPlan->>Dependency: invoke logic
    Dependency-->>LogicalPlan: success
    LogicalPlan-->>TestRunner: Success
```

## 2. AddOperator_AppendsToPlan

```mermaid
sequenceDiagram
    actor TestRunner
    participant LogicalPlan
    TestRunner->>LogicalPlan: addOperator()
    LogicalPlan->>LogicalPlan: apply AppendsToPlan
    LogicalPlan->>Dependency: invoke logic
    Dependency-->>LogicalPlan: success
    LogicalPlan-->>TestRunner: Success
```

## 3. Validate_EnsuresReferencesExistInCatalog

```mermaid
sequenceDiagram
    actor TestRunner
    participant LogicalPlan
    TestRunner->>LogicalPlan: validate()
    LogicalPlan->>LogicalPlan: apply EnsuresReferencesExistInCatalog
    LogicalPlan->>Dependency: invoke logic
    Dependency-->>LogicalPlan: success
    LogicalPlan-->>TestRunner: Success
```

## 4. PrintTree_OutputsFormattedStringForDebugging

```mermaid
sequenceDiagram
    actor TestRunner
    participant LogicalPlan
    TestRunner->>LogicalPlan: printTree()
    LogicalPlan->>LogicalPlan: apply OutputsFormattedStringForDebugging
    LogicalPlan->>Dependency: invoke logic
    Dependency-->>LogicalPlan: success
    LogicalPlan-->>TestRunner: Success
```

## 5. GetLeaves_ReturnsBaseTableScans

```mermaid
sequenceDiagram
    actor TestRunner
    participant LogicalPlan
    TestRunner->>LogicalPlan: getLeaves()
    LogicalPlan->>LogicalPlan: apply ReturnsBaseTableScans
    LogicalPlan->>Dependency: invoke logic
    Dependency-->>LogicalPlan: success
    LogicalPlan-->>TestRunner: Success
```

