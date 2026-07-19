# Sequence Diagrams: Role

## 🆕 Added Properties & Methods for `Role`
To support the detailed sequence logic for unit testing, please update the `Role` class in your Class Diagram with the following properties and methods:

- **Property** added to `Role`: `permissions (List)`
- **Method** added to `Role`: `addPermission()`
- **Method** added to `Role`: `getAllPermissions()`
- **Method** added to `Role`: `hasPermission()`
- **Method** added to `Role`: `inheritRole()`
- **Method** added to `Role`: `removePermission()`

---

This file contains the detailed sequence diagrams for all 6 unit tests of the **Role** class.

## 1. Init_SetsRoleName

```mermaid
sequenceDiagram
    actor TestRunner
    participant Role
    TestRunner->>Role: init()
    Role->>Role: apply SetsRoleName
    Role->>Dependency: invoke logic
    Dependency-->>Role: success
    Role-->>TestRunner: Success
```

## 2. AddPermission_GrantsPermissionToRole

```mermaid
sequenceDiagram
    actor TestRunner
    participant Role
    TestRunner->>Role: addPermission()
    Role->>Role: apply GrantsPermissionToRole
    Role->>Dependency: invoke logic
    Dependency-->>Role: success
    Role-->>TestRunner: Success
```

## 3. RemovePermission_RevokesAccess

```mermaid
sequenceDiagram
    actor TestRunner
    participant Role
    TestRunner->>Role: removePermission()
    Role->>Role: apply RevokesAccess
    Role->>Dependency: invoke logic
    Dependency-->>Role: success
    Role-->>TestRunner: Success
```

## 4. HasPermission_ReturnsTrueIfMatchFound

```mermaid
sequenceDiagram
    actor TestRunner
    participant Role
    TestRunner->>Role: hasPermission()
    Role->>Role: apply ReturnsTrueIfMatchFound
    Role->>Dependency: invoke logic
    Dependency-->>Role: success
    Role-->>TestRunner: Success
```

## 5. GetAllPermissions_ReturnsCombinedList

```mermaid
sequenceDiagram
    actor TestRunner
    participant Role
    TestRunner->>Role: getAllPermissions()
    Role->>Role: apply ReturnsCombinedList
    Role->>Dependency: invoke logic
    Dependency-->>Role: success
    Role-->>TestRunner: Success
```

## 6. InheritRole_AppliesParentPermissionsToChildRole

```mermaid
sequenceDiagram
    actor TestRunner
    participant Role
    TestRunner->>Role: inheritRole()
    Role->>Role: apply AppliesParentPermissionsToChildRole
    Role->>Dependency: invoke logic
    Dependency-->>Role: success
    Role-->>TestRunner: Success
```

