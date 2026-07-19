# Sequence Diagrams: ConnectionManager

## 🆕 Added Properties & Methods for `ConnectionManager`
To support the detailed sequence logic for unit testing, please update the `ConnectionManager` class in your Class Diagram with the following properties and methods:

- **Property** added to `ConnectionManager`: `activeConnections (List)`
- **Property** added to `ConnectionManager`: `MAX_LIMIT (Int)`
- **Property** added to `ConnectionManager`: `isPaused (Bool)`
- **Method** added to `ConnectionManager`: `acceptConnection()`
- **Method** added to `ConnectionManager`: `broadcastMessage()`
- **Method** added to `ConnectionManager`: `cleanup()`
- **Method** added to `ConnectionManager`: `closeConnection()`
- **Method** added to `ConnectionManager`: `getActiveSessions()`
- **Method** added to `ConnectionManager`: `killSession()`

---

This file contains the detailed sequence diagrams for all 10 unit tests of the **ConnectionManager** class.

## 1. AcceptConnection_WhenUnderMaxLimit_CreatesClientSession

```mermaid
sequenceDiagram
    actor TestRunner
    participant ConnectionManager
    TestRunner->>ConnectionManager: acceptConnection()
    ConnectionManager->>ConnectionManager: validate WhenUnderMaxLimit
    ConnectionManager->>ConnectionManager: process AcceptConnection
    ConnectionManager-->>TestRunner: return CreatesClientSession
```

## 2. AcceptConnection_WhenAtMaxLimit_RejectsConnection

```mermaid
sequenceDiagram
    actor TestRunner
    participant ConnectionManager
    TestRunner->>ConnectionManager: acceptConnection()
    ConnectionManager->>ConnectionManager: apply WhenAtMaxLimit
    ConnectionManager->>Dependency: invoke logic
    Dependency-->>ConnectionManager: success
    ConnectionManager-->>TestRunner: RejectsConnection
```

## 3. AcceptConnection_WhenServerPaused_QueuesOrRejects

```mermaid
sequenceDiagram
    actor TestRunner
    participant ConnectionManager
    TestRunner->>ConnectionManager: acceptConnection()
    ConnectionManager->>ConnectionManager: apply WhenServerPaused
    ConnectionManager->>Dependency: invoke logic
    Dependency-->>ConnectionManager: success
    ConnectionManager-->>TestRunner: QueuesOrRejects
```

## 4. CloseConnection_WhenValidSession_ReleasesResources

```mermaid
sequenceDiagram
    actor TestRunner
    participant ConnectionManager
    TestRunner->>ConnectionManager: closeConnection()
    ConnectionManager->>ConnectionManager: apply WhenValidSession
    ConnectionManager->>Dependency: invoke logic
    Dependency-->>ConnectionManager: success
    ConnectionManager-->>TestRunner: ReleasesResources
```

## 5. CloseConnection_WhenInvalidSession_ThrowsException

```mermaid
sequenceDiagram
    actor TestRunner
    participant ConnectionManager
    TestRunner->>ConnectionManager: closeConnection()
    ConnectionManager->>ConnectionManager: check WhenInvalidSession
    ConnectionManager-->>ConnectionManager: condition failed
    ConnectionManager-->>TestRunner: throws Exception
```

## 6. GetActiveSessions_ReturnsSnapshotOfConnectedClients

```mermaid
sequenceDiagram
    actor TestRunner
    participant ConnectionManager
    TestRunner->>ConnectionManager: getActiveSessions()
    ConnectionManager->>ConnectionManager: apply ReturnsSnapshotOfConnectedClients
    ConnectionManager->>Dependency: invoke logic
    Dependency-->>ConnectionManager: success
    ConnectionManager-->>TestRunner: Success
```

## 7. BroadcastMessage_SendsToAllActiveSessions

```mermaid
sequenceDiagram
    actor TestRunner
    participant ConnectionManager
    TestRunner->>ConnectionManager: broadcastMessage()
    ConnectionManager->>ConnectionManager: apply SendsToAllActiveSessions
    ConnectionManager->>Dependency: invoke logic
    Dependency-->>ConnectionManager: success
    ConnectionManager-->>TestRunner: Success
```

## 8. KillSession_ForcefullyTerminatesConnection

```mermaid
sequenceDiagram
    actor TestRunner
    participant ConnectionManager
    TestRunner->>ConnectionManager: killSession()
    ConnectionManager->>ConnectionManager: apply ForcefullyTerminatesConnection
    ConnectionManager->>Dependency: invoke logic
    Dependency-->>ConnectionManager: success
    ConnectionManager-->>TestRunner: Success
```

## 9. Cleanup_RemovesIdleConnectionsAutomatically

```mermaid
sequenceDiagram
    actor TestRunner
    participant ConnectionManager
    TestRunner->>ConnectionManager: cleanup()
    ConnectionManager->>ConnectionManager: apply RemovesIdleConnectionsAutomatically
    ConnectionManager->>Dependency: invoke logic
    Dependency-->>ConnectionManager: success
    ConnectionManager-->>TestRunner: Success
```

## 10. AcceptConnection_WhenClientBlacklisted_RejectsImmediately

```mermaid
sequenceDiagram
    actor TestRunner
    participant ConnectionManager
    TestRunner->>ConnectionManager: acceptConnection()
    ConnectionManager->>ConnectionManager: apply WhenClientBlacklisted
    ConnectionManager->>Dependency: invoke logic
    Dependency-->>ConnectionManager: success
    ConnectionManager-->>TestRunner: RejectsImmediately
```

