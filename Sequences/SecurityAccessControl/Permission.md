# Sequence Diagrams: Permission

## 🆕 Added Properties & Methods for `Permission`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `Permission` class in your Class Diagram with these:**

- **Property** added to `Permission`: `resource`, `actionType` (e.g. 'TABLE_A', 'SELECT')

---

This file contains the detailed sequence diagrams for all unit tests of the **Permission** class in the Security & Access Control subsystem.

## 1. Init_SetsResourceAndActionType

```mermaid
sequenceDiagram
    actor Test
    participant Permission

    Test->>Permission: new Permission(resource, actionType)
    Permission->>Permission: self.resource = resource
    Permission->>Permission: self.actionType = actionType
    Permission-->>Test: return instance
```

## 2. Matches_WhenActionAndResourceAlign_ReturnsTrue

```mermaid
sequenceDiagram
    actor Test
    participant Permission

    Test->>Permission: matches("TABLE_A", "READ")
    Permission->>Permission: check self.resource == "TABLE_A" and self.actionType == "READ"
    Permission-->>Test: return true
```

