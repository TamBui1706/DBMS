# Sequence Diagrams: View

## 🆕 Added Properties & Methods for `View`
To support the detailed sequence logic for unit testing, please update the `View` class in your Class Diagram with the following properties and methods:

- **Property** added to `View`: `queryDefinition (String)`
- **Property** added to `View`: `materializedData (Cache)`
- **Method** added to `View`: `compileView()`
- **Method** added to `View`: `materialize()`
- **Method** added to `View`: `refresh()`

---

This file contains the detailed sequence diagrams for all 6 unit tests of the **View** class.

## 1. Init_SetsQueryDefinition

```mermaid
sequenceDiagram
    actor TestRunner
    participant View
    TestRunner->>View: init()
    View->>View: apply SetsQueryDefinition
    View->>Dependency: invoke logic
    Dependency-->>View: success
    View-->>TestRunner: Success
```

## 2. CompileView_WhenUnderlyingTablesExist_Succeeds

```mermaid
sequenceDiagram
    actor TestRunner
    participant View
    TestRunner->>View: compileView()
    View->>View: validate WhenUnderlyingTablesExist
    View->>View: process CompileView
    View-->>TestRunner: return Succeeds
```

## 3. CompileView_WhenTableDropped_ThrowsInvalidViewException

```mermaid
sequenceDiagram
    actor TestRunner
    participant View
    TestRunner->>View: compileView()
    View->>View: check WhenTableDropped
    View-->>View: condition failed
    View-->>TestRunner: throws InvalidViewException
```

## 4. Materialize_CachesResultSetToDisk

```mermaid
sequenceDiagram
    actor TestRunner
    participant View
    TestRunner->>View: materialize()
    View->>View: apply CachesResultSetToDisk
    View->>Dependency: invoke logic
    Dependency-->>View: success
    View-->>TestRunner: Success
```

## 5. Refresh_UpdatesMaterializedData

```mermaid
sequenceDiagram
    actor TestRunner
    participant View
    TestRunner->>View: refresh()
    View->>View: apply UpdatesMaterializedData
    View->>Dependency: invoke logic
    Dependency-->>View: success
    View-->>TestRunner: Success
```

## 6. CompileView_WhenCircularDependencyDetected_ThrowsException

```mermaid
sequenceDiagram
    actor TestRunner
    participant View
    TestRunner->>View: compileView()
    View->>View: check WhenCircularDependencyDetected
    View-->>View: condition failed
    View-->>TestRunner: throws Exception
```

