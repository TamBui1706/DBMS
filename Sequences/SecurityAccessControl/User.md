# Sequence Diagrams: User

## 🆕 Added Properties & Methods for `User`
To support the detailed sequence logic for unit testing, please update the `User` class in your Class Diagram with the following properties and methods:

- **Property** added to `User`: `roles (List)`
- **Property** added to `User`: `isLocked (Bool)`
- **Method** added to `User`: `addRole()`
- **Method** added to `User`: `hasRole()`
- **Method** added to `User`: `isLocked()`
- **Method** added to `User`: `lockAccount()`
- **Method** added to `User`: `removeRole()`
- **Method** added to `User`: `updatePassword()`

---

This file contains the detailed sequence diagrams for all 7 unit tests of the **User** class.

## 1. Init_SetsUsernameAndHashedPassword

```mermaid
sequenceDiagram
    actor TestRunner
    participant User
    TestRunner->>User: init()
    User->>User: apply SetsUsernameAndHashedPassword
    User->>Dependency: invoke logic
    Dependency-->>User: success
    User-->>TestRunner: Success
```

## 2. AddRole_AssignsNewRoleToUser

```mermaid
sequenceDiagram
    actor TestRunner
    participant User
    TestRunner->>User: addRole()
    User->>User: apply AssignsNewRoleToUser
    User->>Dependency: invoke logic
    Dependency-->>User: success
    User-->>TestRunner: Success
```

## 3. RemoveRole_TakesAwayPermissions

```mermaid
sequenceDiagram
    actor TestRunner
    participant User
    TestRunner->>User: removeRole()
    User->>User: apply TakesAwayPermissions
    User->>Dependency: invoke logic
    Dependency-->>User: success
    User-->>TestRunner: Success
```

## 4. UpdatePassword_HashesAndSavesNewPassword

```mermaid
sequenceDiagram
    actor TestRunner
    participant User
    TestRunner->>User: updatePassword()
    User->>User: apply HashesAndSavesNewPassword
    User->>Dependency: invoke logic
    Dependency-->>User: success
    User-->>TestRunner: Success
```

## 5. LockAccount_PreventsLoginAfterFailedAttempts

```mermaid
sequenceDiagram
    actor TestRunner
    participant User
    TestRunner->>User: lockAccount()
    User->>User: apply PreventsLoginAfterFailedAttempts
    User->>Dependency: invoke logic
    Dependency-->>User: success
    User-->>TestRunner: Success
```

## 6. IsLocked_ReturnsStatus

```mermaid
sequenceDiagram
    actor TestRunner
    participant User
    TestRunner->>User: isLocked()
    User->>User: apply ReturnsStatus
    User->>Dependency: invoke logic
    Dependency-->>User: success
    User-->>TestRunner: Success
```

## 7. HasRole_ReturnsTrueIfAssigned

```mermaid
sequenceDiagram
    actor TestRunner
    participant User
    TestRunner->>User: hasRole()
    User->>User: apply ReturnsTrueIfAssigned
    User->>Dependency: invoke logic
    Dependency-->>User: success
    User-->>TestRunner: Success
```

