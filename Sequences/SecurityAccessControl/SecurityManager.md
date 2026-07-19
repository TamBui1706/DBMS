# Sequence Diagrams: SecurityManager

## 🆕 Added Properties & Methods for `SecurityManager`
To support the detailed sequence logic for unit testing, please update the `SecurityManager` class in your Class Diagram with the following properties and methods:

- **Property** added to `SecurityManager`: `usersDict (Dict)`
- **Property** added to `SecurityManager`: `activeTokens (Set)`
- **Method** added to `SecurityManager`: `authenticate()`
- **Method** added to `SecurityManager`: `authorize()`
- **Method** added to `SecurityManager`: `cleanupTokens()`
- **Method** added to `SecurityManager`: `hashPassword()`
- **Method** added to `SecurityManager`: `revokeToken()`

---

This file contains the detailed sequence diagrams for all 8 unit tests of the **SecurityManager** class.

## 1. Authenticate_WhenValidCredentials_ReturnsSessionToken

```mermaid
sequenceDiagram
    actor TestRunner
    participant SecurityManager
    TestRunner->>SecurityManager: authenticate()
    SecurityManager->>SecurityManager: validate WhenValidCredentials
    SecurityManager->>SecurityManager: process Authenticate
    SecurityManager-->>TestRunner: return SessionToken
```

## 2. Authenticate_WhenInvalidCredentials_ThrowsAuthException

```mermaid
sequenceDiagram
    actor TestRunner
    participant SecurityManager
    TestRunner->>SecurityManager: authenticate()
    SecurityManager->>SecurityManager: check WhenInvalidCredentials
    SecurityManager-->>SecurityManager: condition failed
    SecurityManager-->>TestRunner: throws AuthException
```

## 3. Authorize_WhenUserHasRequiredRole_Succeeds

```mermaid
sequenceDiagram
    actor TestRunner
    participant SecurityManager
    TestRunner->>SecurityManager: authorize()
    SecurityManager->>SecurityManager: validate WhenUserHasRequiredRole
    SecurityManager->>SecurityManager: process Authorize
    SecurityManager-->>TestRunner: return Succeeds
```

## 4. Authorize_WhenUserLacksPermission_ThrowsAccessException

```mermaid
sequenceDiagram
    actor TestRunner
    participant SecurityManager
    TestRunner->>SecurityManager: authorize()
    SecurityManager->>SecurityManager: check WhenUserLacksPermission
    SecurityManager-->>SecurityManager: condition failed
    SecurityManager-->>TestRunner: throws AccessException
```

## 5. RevokeToken_InvalidatesSessionImmediately

```mermaid
sequenceDiagram
    actor TestRunner
    participant SecurityManager
    TestRunner->>SecurityManager: revokeToken()
    SecurityManager->>SecurityManager: apply InvalidatesSessionImmediately
    SecurityManager->>Dependency: invoke logic
    Dependency-->>SecurityManager: success
    SecurityManager-->>TestRunner: Success
```

## 6. HashPassword_UsesStrongCryptography

```mermaid
sequenceDiagram
    actor TestRunner
    participant SecurityManager
    TestRunner->>SecurityManager: hashPassword()
    SecurityManager->>SecurityManager: apply UsesStrongCryptography
    SecurityManager->>Dependency: invoke logic
    Dependency-->>SecurityManager: success
    SecurityManager-->>TestRunner: Success
```

## 7. Authenticate_WhenAccountLocked_ThrowsLockedException

```mermaid
sequenceDiagram
    actor TestRunner
    participant SecurityManager
    TestRunner->>SecurityManager: authenticate()
    SecurityManager->>SecurityManager: check WhenAccountLocked
    SecurityManager-->>SecurityManager: condition failed
    SecurityManager-->>TestRunner: throws LockedException
```

## 8. CleanupTokens_RemovesExpiredSessions

```mermaid
sequenceDiagram
    actor TestRunner
    participant SecurityManager
    TestRunner->>SecurityManager: cleanupTokens()
    SecurityManager->>SecurityManager: apply RemovesExpiredSessions
    SecurityManager->>Dependency: invoke logic
    Dependency-->>SecurityManager: success
    SecurityManager-->>TestRunner: Success
```

