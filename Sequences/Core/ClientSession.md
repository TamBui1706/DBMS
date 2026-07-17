# Sequence Diagrams: ClientSession

## 🆕 Added Properties & Methods for `ClientSession`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `ClientSession` class in your Class Diagram with these:**

- **Property** added to `ClientSession`: `TIMEOUT` (Constant for session expiration)
- **Method** added to `ClientSession`: `close()` (Releases session resources, called by ConnectionManager)
- **Method** added to `ClientSession`: `validateSession()` (Checks session expiration against `connectTime`)

---

This file contains the detailed sequence diagrams for all unit tests of the **ClientSession** class in the Core Server & Connections subsystem.

## 1. Init_SetsSessionIdAndTimestamp

```mermaid
sequenceDiagram
    actor Test
    participant ClientSession

    Test->>ClientSession: new ClientSession()
    ClientSession->>ClientSession: generate sessionId
    ClientSession->>ClientSession: connectTime = now()
    ClientSession-->>Test: return instance
```

## 2. Execute_WhenValidQuery_ReturnsExecutionResult

```mermaid
sequenceDiagram
    actor Test
    participant ClientSession
    participant QueryProcessor

    Test->>ClientSession: execute(sqlQuery)
    ClientSession->>ClientSession: validateSession()
    ClientSession-->>ClientSession: active
    ClientSession->>QueryProcessor: processQuery(sqlQuery)
    QueryProcessor-->>ClientSession: resultData
    ClientSession-->>Test: return resultData
```

## 3. Execute_WhenSessionExpired_ThrowsTimeoutException

```mermaid
sequenceDiagram
    actor Test
    participant ClientSession

    Test->>ClientSession: execute(sqlQuery)
    ClientSession->>ClientSession: validateSession()
    ClientSession->>ClientSession: check (now() - connectTime) > TIMEOUT
    ClientSession-->>Test: throws SessionExpiredException
```

## 4. Execute_WhenConnectionLost_FailsGracefully

```mermaid
sequenceDiagram
    actor Test
    participant ClientSession
    participant ConnectionManager

    Test->>ClientSession: execute(sqlQuery)
    ClientSession->>ConnectionManager: checkServerState()
    ConnectionManager-->>ClientSession: DISCONNECTED
    ClientSession-->>Test: throws ConnectionLostException
```

