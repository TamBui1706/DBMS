# Sequence Diagrams: DatabaseServer

## 🆕 Added Properties & Methods for `DatabaseServer`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `DatabaseServer` class in your Class Diagram with these:**

- **Property** added to `DatabaseServer`: `config` (Configuration object passed during start)
- **Property** added to `DatabaseServer`: `connectionManager`, `databaseManager`, `catalogManager` (References to subsystem instances)
- **Method** added to `DatabaseServer`: `getStatus()` (Returns the current operational status)

---

This file contains the detailed sequence diagrams for all unit tests of the **DatabaseServer** class in the Core Server & Connections subsystem.

## 1. Start_WhenConfigValid_InitializesAllSubsystems

```mermaid
sequenceDiagram
    actor Test
    participant DatabaseServer
    participant ConnectionManager
    participant DatabaseManager
    participant CatalogManager

    Test->>DatabaseServer: start()
    DatabaseServer->>ConnectionManager: initialize()
    ConnectionManager-->>DatabaseServer: success
    DatabaseServer->>DatabaseManager: initialize()
    DatabaseManager-->>DatabaseServer: success
    DatabaseServer->>CatalogManager: initialize()
    CatalogManager-->>DatabaseServer: success
    DatabaseServer->>DatabaseServer: status = RUNNING
    DatabaseServer-->>Test: success
```

## 2. Start_WhenAlreadyRunning_ThrowsIllegalStateException

```mermaid
sequenceDiagram
    actor Test
    participant DatabaseServer

    Test->>DatabaseServer: start()
    DatabaseServer->>DatabaseServer: getStatus()
    DatabaseServer-->>DatabaseServer: RUNNING
    DatabaseServer-->>Test: throws IllegalStateException
```

## 3. Stop_WhenRunning_ShutsDownGracefully

```mermaid
sequenceDiagram
    actor Test
    participant DatabaseServer
    participant ConnectionManager
    participant DatabaseManager
    participant CatalogManager

    Test->>DatabaseServer: stop()
    DatabaseServer->>ConnectionManager: shutdown()
    ConnectionManager-->>DatabaseServer: success
    DatabaseServer->>DatabaseManager: shutdown()
    DatabaseManager-->>DatabaseServer: success
    DatabaseServer->>CatalogManager: shutdown()
    CatalogManager-->>DatabaseServer: success
    DatabaseServer->>DatabaseServer: status = STOPPED
    DatabaseServer-->>Test: success
```

## 4. Stop_WhenAlreadyStopped_DoesNothing

```mermaid
sequenceDiagram
    actor Test
    participant DatabaseServer

    Test->>DatabaseServer: stop()
    DatabaseServer->>DatabaseServer: getStatus()
    DatabaseServer-->>DatabaseServer: STOPPED
    DatabaseServer-->>Test: return (does nothing)
```

## 5. Status_ReturnsCurrentOperationalState

```mermaid
sequenceDiagram
    actor Test
    participant DatabaseServer

    Test->>DatabaseServer: getStatus()
    DatabaseServer-->>Test: return status (RUNNING or STOPPED)
```

