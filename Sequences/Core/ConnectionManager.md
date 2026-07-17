# Sequence Diagrams: ConnectionManager

## 🆕 Added Properties & Methods for `ConnectionManager`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `ConnectionManager` class in your Class Diagram with these:**

- **Property** added to `ConnectionManager`: `activeConnections` (List or Counter of currently active sessions)
- **Property** added to `ConnectionManager`: `MAX_LIMIT` (Integer constant defining maximum concurrent connections)
- **Method** added to `ConnectionManager`: `getActiveSessions(dbName)` (Returns active sessions for a specific database, used by DatabaseManager)
- **Method** added to `ConnectionManager`: `checkServerState()` (Checks if the server is PAUSED or DISCONNECTED)

---

This file contains the detailed sequence diagrams for all unit tests of the **ConnectionManager** class in the Core Server & Connections subsystem.

## 1. AcceptConnection_WhenUnderMaxLimit_CreatesClientSession

```mermaid
sequenceDiagram
    actor Test
    participant ConnectionManager
    participant ClientSession

    Test->>ConnectionManager: acceptConnection(clientInfo)
    ConnectionManager->>ConnectionManager: check activeConnections.size() < MAX_LIMIT
    ConnectionManager->>ClientSession: new ClientSession(clientInfo)
    ClientSession-->>ConnectionManager: sessionInstance
    ConnectionManager->>ConnectionManager: activeConnections.append(sessionInstance)
    ConnectionManager-->>Test: return sessionInstance
```

## 2. AcceptConnection_WhenAtMaxLimit_RejectsConnection

```mermaid
sequenceDiagram
    actor Test
    participant ConnectionManager

    Test->>ConnectionManager: acceptConnection(clientInfo)
    ConnectionManager->>ConnectionManager: check activeConnections.size() >= MAX_LIMIT
    ConnectionManager-->>Test: throws MaxConnectionsReachedException
```

## 3. AcceptConnection_WhenServerPaused_QueuesOrRejects

```mermaid
sequenceDiagram
    actor Test
    participant ConnectionManager

    Test->>ConnectionManager: acceptConnection(clientInfo)
    ConnectionManager->>ConnectionManager: checkServerState()
    ConnectionManager-->>ConnectionManager: PAUSED
    ConnectionManager-->>Test: throws ServerPausedException
```

## 4. CloseConnection_WhenValidSession_ReleasesResources

```mermaid
sequenceDiagram
    actor Test
    participant ConnectionManager
    participant ClientSession

    Test->>ConnectionManager: closeConnection(sessionId)
    ConnectionManager->>ConnectionManager: find session in activeConnections
    ConnectionManager->>ClientSession: close()
    ClientSession-->>ConnectionManager: success
    ConnectionManager->>ConnectionManager: activeConnections.remove(session)
    ConnectionManager-->>Test: return success
```

## 5. CloseConnection_WhenInvalidSession_ThrowsException

```mermaid
sequenceDiagram
    actor Test
    participant ConnectionManager

    Test->>ConnectionManager: closeConnection(invalidSessionId)
    ConnectionManager->>ConnectionManager: find session in activeConnections
    ConnectionManager-->>ConnectionManager: not found
    ConnectionManager-->>Test: throws SessionNotFoundException
```

