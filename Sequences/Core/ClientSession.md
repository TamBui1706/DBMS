# Sequence Diagrams: ClientSession

## 🆕 Added Properties & Methods for `ClientSession`
To support the detailed sequence logic for unit testing, please update the `ClientSession` class in your Class Diagram with the following properties and methods:

- **Property** added to `ClientSession`: `TIMEOUT (Int)`
- **Property** added to `ClientSession`: `connectTime (DateTime)`
- **Property** added to `ClientSession`: `sessionVariables (Dict)`
- **Method** added to `ClientSession`: `execute()`
- **Method** added to `ClientSession`: `getSessionVariable()`
- **Method** added to `ClientSession`: `ping()`
- **Method** added to `ClientSession`: `setSessionVariable()`

---

This file contains the detailed sequence diagrams for all 9 unit tests of the **ClientSession** class.

## 1. Init_SetsSessionIdAndTimestamp

```mermaid
sequenceDiagram
    actor TestRunner
    participant ClientSession
    TestRunner->>ClientSession: init()
    ClientSession->>ClientSession: apply SetsSessionIdAndTimestamp
    ClientSession->>Dependency: invoke logic
    Dependency-->>ClientSession: success
    ClientSession-->>TestRunner: Success
```

## 2. Execute_WhenValidQuery_ReturnsExecutionResult

```mermaid
sequenceDiagram
    actor TestRunner
    participant ClientSession
    TestRunner->>ClientSession: execute()
    ClientSession->>ClientSession: validate WhenValidQuery
    ClientSession->>ClientSession: process Execute
    ClientSession-->>TestRunner: return ExecutionResult
```

## 3. Execute_WhenSessionExpired_ThrowsTimeoutException

```mermaid
sequenceDiagram
    actor TestRunner
    participant ClientSession
    TestRunner->>ClientSession: execute()
    ClientSession->>ClientSession: check WhenSessionExpired
    ClientSession-->>ClientSession: condition failed
    ClientSession-->>TestRunner: throws TimeoutException
```

## 4. Execute_WhenConnectionLost_FailsGracefully

```mermaid
sequenceDiagram
    actor TestRunner
    participant ClientSession
    TestRunner->>ClientSession: execute()
    ClientSession->>ClientSession: check WhenConnectionLost
    ClientSession-->>ClientSession: condition failed
    ClientSession-->>TestRunner: throws FailsGracefully
```

## 5. SetSessionVariable_UpdatesInternalState

```mermaid
sequenceDiagram
    actor TestRunner
    participant ClientSession
    TestRunner->>ClientSession: setSessionVariable()
    ClientSession->>ClientSession: apply UpdatesInternalState
    ClientSession->>Dependency: invoke logic
    Dependency-->>ClientSession: success
    ClientSession-->>TestRunner: Success
```

## 6. GetSessionVariable_ReturnsSetValue

```mermaid
sequenceDiagram
    actor TestRunner
    participant ClientSession
    TestRunner->>ClientSession: getSessionVariable()
    ClientSession->>ClientSession: apply ReturnsSetValue
    ClientSession->>Dependency: invoke logic
    Dependency-->>ClientSession: success
    ClientSession-->>TestRunner: Success
```

## 7. Execute_WhenEmptyQuery_ReturnsEmptyResult

```mermaid
sequenceDiagram
    actor TestRunner
    participant ClientSession
    TestRunner->>ClientSession: execute()
    ClientSession->>ClientSession: validate WhenEmptyQuery
    ClientSession->>ClientSession: process Execute
    ClientSession-->>TestRunner: return EmptyResult
```

## 8. GetSessionVariable_WhenKeyNotExists_ReturnsNull

```mermaid
sequenceDiagram
    actor TestRunner
    participant ClientSession
    TestRunner->>ClientSession: getSessionVariable()
    ClientSession->>ClientSession: validate WhenKeyNotExists
    ClientSession->>ClientSession: process GetSessionVariable
    ClientSession-->>TestRunner: return Null
```

## 9. Ping_ResetsIdleTimer

```mermaid
sequenceDiagram
    actor TestRunner
    participant ClientSession
    TestRunner->>ClientSession: ping()
    ClientSession->>ClientSession: apply ResetsIdleTimer
    ClientSession->>Dependency: invoke logic
    Dependency-->>ClientSession: success
    ClientSession-->>TestRunner: Success
```

