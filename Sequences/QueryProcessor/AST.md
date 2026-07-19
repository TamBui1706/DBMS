# Sequence Diagrams: AST

## 🆕 Added Properties & Methods for `AST`
To support the detailed sequence logic for unit testing, please update the `AST` class in your Class Diagram with the following properties and methods:

- **Property** added to `AST`: `rootNode`
- **Method** added to `AST`: `clone()`
- **Method** added to `AST`: `countNodes()`
- **Method** added to `AST`: `toSQL()`
- **Method** added to `AST`: `traverse()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **AST** class.

## 1. Init_SetsRootNode

```mermaid
sequenceDiagram
    actor TestRunner
    participant AST
    TestRunner->>AST: init()
    AST->>AST: apply SetsRootNode
    AST->>Dependency: invoke logic
    Dependency-->>AST: success
    AST-->>TestRunner: Success
```

## 2. Traverse_VisitsAllNodesInCorrectOrder

```mermaid
sequenceDiagram
    actor TestRunner
    participant AST
    TestRunner->>AST: traverse()
    AST->>AST: apply VisitsAllNodesInCorrectOrder
    AST->>Dependency: invoke logic
    Dependency-->>AST: success
    AST-->>TestRunner: Success
```

## 3. ToSQL_ReconstructsSQLStringFromTree

```mermaid
sequenceDiagram
    actor TestRunner
    participant AST
    TestRunner->>AST: toSQL()
    AST->>AST: apply ReconstructsSQLStringFromTree
    AST->>Dependency: invoke logic
    Dependency-->>AST: success
    AST-->>TestRunner: Success
```

## 4. Clone_CreatesDeepCopyOfTree

```mermaid
sequenceDiagram
    actor TestRunner
    participant AST
    TestRunner->>AST: clone()
    AST->>AST: apply CreatesDeepCopyOfTree
    AST->>Dependency: invoke logic
    Dependency-->>AST: success
    AST-->>TestRunner: Success
```

## 5. CountNodes_ReturnsTotalSizeOfTree

```mermaid
sequenceDiagram
    actor TestRunner
    participant AST
    TestRunner->>AST: countNodes()
    AST->>AST: apply ReturnsTotalSizeOfTree
    AST->>Dependency: invoke logic
    Dependency-->>AST: success
    AST-->>TestRunner: Success
```

