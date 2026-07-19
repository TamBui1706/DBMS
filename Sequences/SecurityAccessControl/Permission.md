# Sequence Diagrams: Permission

## 🆕 Added Properties & Methods for `Permission`
To support the detailed sequence logic for unit testing, please update the `Permission` class in your Class Diagram with the following properties and methods:

- **Property** added to `Permission`: `resource`
- **Property** added to `Permission`: `actionType`
- **Method** added to `Permission`: `matches()`
- **Method** added to `Permission`: `toString()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **Permission** class.

## 1. Init_SetsResourceAndActionType

```mermaid
sequenceDiagram
    actor TestRunner
    participant Permission
    TestRunner->>Permission: init()
    Permission->>Permission: apply SetsResourceAndActionType
    Permission->>Dependency: invoke logic
    Dependency-->>Permission: success
    Permission-->>TestRunner: Success
```

## 2. Matches_WhenActionAndResourceAlign_ReturnsTrue

```mermaid
sequenceDiagram
    actor TestRunner
    participant Permission
    TestRunner->>Permission: matches()
    Permission->>Permission: validate WhenActionAndResourceAlign
    Permission->>Permission: process Matches
    Permission-->>TestRunner: return True
```

## 3. Matches_WhenWildcardResource_ReturnsTrueForAll

```mermaid
sequenceDiagram
    actor TestRunner
    participant Permission
    TestRunner->>Permission: matches()
    Permission->>Permission: validate WhenWildcardResource
    Permission->>Permission: process Matches
    Permission-->>TestRunner: return TrueForAll
```

## 4. ToString_FormatsPermissionForLogging

```mermaid
sequenceDiagram
    actor TestRunner
    participant Permission
    TestRunner->>Permission: toString()
    Permission->>Permission: apply FormatsPermissionForLogging
    Permission->>Dependency: invoke logic
    Dependency-->>Permission: success
    Permission-->>TestRunner: Success
```

## 5. Matches_WhenActionIsDeny_OverridesGrant

```mermaid
sequenceDiagram
    actor TestRunner
    participant Permission
    TestRunner->>Permission: matches()
    Permission->>Permission: apply WhenActionIsDeny
    Permission->>Dependency: invoke logic
    Dependency-->>Permission: success
    Permission-->>TestRunner: OverridesGrant
```

