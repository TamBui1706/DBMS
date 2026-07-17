# Sequence Diagrams: AST

## 🆕 Added Properties & Methods for `AST`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `AST` class in your Class Diagram with these:**

- **Property** added to `AST`: `rootNode` (Entry point for abstract syntax tree)
- **Method** added to `AST`: `traverseNodes()` (Depth-first traversal)

---

This file contains the detailed sequence diagrams for all unit tests of the **AST** class in the Query Processor subsystem.

## 1. Init_SetsRootNode

```mermaid
sequenceDiagram
    actor Test
    participant AST

    Test->>AST: new AST(rootNode)
    AST->>AST: self.rootNode = rootNode
    AST-->>Test: return instance
```

## 2. Traverse_VisitsAllNodesInCorrectOrder

```mermaid
sequenceDiagram
    actor Test
    participant AST

    Test->>AST: traverse()
    AST->>AST: traverseNodes(self.rootNode)
    AST-->>Test: return list of visited nodes
```

