# Sequence Diagrams: DatabaseServer

## 🆕 Added Properties & Methods for `DatabaseServer`
To support the detailed sequence logic for unit testing, please update the `DatabaseServer` class in your Class Diagram with the following properties and methods:

- **Property** added to `DatabaseServer`: `config (Configuration)`
- **Property** added to `DatabaseServer`: `connectionManager`
- **Property** added to `DatabaseServer`: `databaseManager`
- **Property** added to `DatabaseServer`: `catalogManager`
- **Method** added to `DatabaseServer`: `healthCheck()`
- **Method** added to `DatabaseServer`: `restart()`
- **Method** added to `DatabaseServer`: `status()`

---

This file contains the detailed sequence diagrams for all 10 unit tests of the **DatabaseServer** class.

## 1. Start_WhenConfigValid_InitializesAllSubsystems

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseServer
    TestRunner->>DatabaseServer: start()
    DatabaseServer->>DatabaseServer: apply WhenConfigValid
    DatabaseServer->>Dependency: invoke logic
    Dependency-->>DatabaseServer: success
    DatabaseServer-->>TestRunner: InitializesAllSubsystems
```

## 2. Start_WhenAlreadyRunning_ThrowsIllegalStateException

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseServer
    TestRunner->>DatabaseServer: start()
    DatabaseServer->>DatabaseServer: check WhenAlreadyRunning
    DatabaseServer-->>DatabaseServer: condition failed
    DatabaseServer-->>TestRunner: throws IllegalStateException
```

## 3. Stop_WhenRunning_ShutsDownGracefully

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseServer
    TestRunner->>DatabaseServer: stop()
    DatabaseServer->>DatabaseServer: apply WhenRunning
    DatabaseServer->>Dependency: invoke logic
    Dependency-->>DatabaseServer: success
    DatabaseServer-->>TestRunner: ShutsDownGracefully
```

## 4. Stop_WhenAlreadyStopped_DoesNothing

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseServer
    TestRunner->>DatabaseServer: stop()
    DatabaseServer->>DatabaseServer: apply WhenAlreadyStopped
    DatabaseServer->>Dependency: invoke logic
    Dependency-->>DatabaseServer: success
    DatabaseServer-->>TestRunner: DoesNothing
```

## 5. Status_ReturnsCurrentOperationalState

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseServer
    TestRunner->>DatabaseServer: status()
    DatabaseServer->>DatabaseServer: apply ReturnsCurrentOperationalState
    DatabaseServer->>Dependency: invoke logic
    Dependency-->>DatabaseServer: success
    DatabaseServer-->>TestRunner: Success
```

## 6. Start_WhenPortAlreadyInUse_ThrowsBindException

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseServer
    TestRunner->>DatabaseServer: start()
    DatabaseServer->>DatabaseServer: check WhenPortAlreadyInUse
    DatabaseServer-->>DatabaseServer: condition failed
    DatabaseServer-->>TestRunner: throws BindException
```

## 7. Stop_WhenActiveTransactionsExist_WaitsForCompletionOrTimeout

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseServer
    TestRunner->>DatabaseServer: stop()
    DatabaseServer->>DatabaseServer: apply WhenActiveTransactionsExist
    DatabaseServer->>Dependency: invoke logic
    Dependency-->>DatabaseServer: success
    DatabaseServer-->>TestRunner: WaitsForCompletionOrTimeout
```

## 8. Restart_GracefullyStopsAndStartsSystem

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseServer
    TestRunner->>DatabaseServer: restart()
    DatabaseServer->>DatabaseServer: apply GracefullyStopsAndStartsSystem
    DatabaseServer->>Dependency: invoke logic
    Dependency-->>DatabaseServer: success
    DatabaseServer-->>TestRunner: Success
```

## 9. Init_WithMissingConfigFilePath_ThrowsConfigurationException

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseServer
    TestRunner->>DatabaseServer: init()
    DatabaseServer->>DatabaseServer: check WithMissingConfigFilePath
    DatabaseServer-->>DatabaseServer: condition failed
    DatabaseServer-->>TestRunner: throws ConfigurationException
```

## 10. HealthCheck_ReturnsTrueIfAllSubsystemsAreRunning

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseServer
    TestRunner->>DatabaseServer: healthCheck()
    DatabaseServer->>DatabaseServer: apply ReturnsTrueIfAllSubsystemsAreRunning
    DatabaseServer->>Dependency: invoke logic
    Dependency-->>DatabaseServer: success
    DatabaseServer-->>TestRunner: Success
```

