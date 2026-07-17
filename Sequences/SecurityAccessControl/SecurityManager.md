# Sequence Diagrams: SecurityManager

## 🆕 Added Properties & Methods for `SecurityManager`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `SecurityManager` class in your Class Diagram with these:**

- **Property** added to `SecurityManager`: `usersDict` (Maps username to User object)
- **Property** added to `SecurityManager`: `activeTokens` (Tracks authenticated sessions)

---

This file contains the detailed sequence diagrams for all unit tests of the **SecurityManager** class in the Security & Access Control subsystem.

## 1. Authenticate_WhenValidCredentials_ReturnsSessionToken

```mermaid
sequenceDiagram
    actor Test
    participant SecurityManager
    participant User

    Test->>SecurityManager: authenticate(username, password)
    SecurityManager->>SecurityManager: user = usersDict.get(username)
    SecurityManager->>User: verifyPassword(password)
    User-->>SecurityManager: true
    SecurityManager->>SecurityManager: generate token
    SecurityManager->>SecurityManager: activeTokens.add(token)
    SecurityManager-->>Test: return token
```

## 2. Authenticate_WhenInvalidCredentials_ThrowsAuthException

```mermaid
sequenceDiagram
    actor Test
    participant SecurityManager
    participant User

    Test->>SecurityManager: authenticate(username, wrongPassword)
    SecurityManager->>SecurityManager: user = usersDict.get(username)
    SecurityManager->>User: verifyPassword(wrongPassword)
    User-->>SecurityManager: false
    SecurityManager-->>Test: throws AuthenticationException
```

## 3. Authorize_WhenUserHasRequiredRole_Succeeds

```mermaid
sequenceDiagram
    actor Test
    participant SecurityManager
    participant User
    participant Role

    Test->>SecurityManager: authorize(token, resource, action)
    SecurityManager->>SecurityManager: user = activeTokens.getUser(token)
    SecurityManager->>User: checkRoles(resource, action)
    User->>Role: hasPermission(resource, action)
    Role-->>User: true
    User-->>SecurityManager: true
    SecurityManager-->>Test: success
```

## 4. Authorize_WhenUserLacksPermission_ThrowsAccessException

```mermaid
sequenceDiagram
    actor Test
    participant SecurityManager
    participant User
    participant Role

    Test->>SecurityManager: authorize(token, resource, action)
    SecurityManager->>SecurityManager: user = activeTokens.getUser(token)
    SecurityManager->>User: checkRoles(resource, action)
    User->>Role: hasPermission(resource, action)
    Role-->>User: false
    User-->>SecurityManager: false
    SecurityManager-->>Test: throws AccessDeniedException
```

