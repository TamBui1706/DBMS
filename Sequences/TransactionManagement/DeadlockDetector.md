# Sequence Diagrams: DeadlockDetector

## 🆕 Added Properties & Methods for `DeadlockDetector`
To support the detailed sequence logic for unit testing, please update the `DeadlockDetector` class in your Class Diagram with the following properties and methods:

- **Property** added to `DeadlockDetector`: `waitForGraph`
- **Property** added to `DeadlockDetector`: `timeout (Int)`
- **Method** added to `DeadlockDetector`: `buildWaitForGraph()`
- **Method** added to `DeadlockDetector`: `chooseVictim()`
- **Method** added to `DeadlockDetector`: `detectAndResolve()`
- **Method** added to `DeadlockDetector`: `setTimeout()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **DeadlockDetector** class.

## 1. DetectAndResolve_WhenCycleFound_AbortsVictimTransaction

```mermaid
sequenceDiagram
    actor TestRunner
    participant DeadlockDetector
    TestRunner->>DeadlockDetector: detectAndResolve()
    DeadlockDetector->>DeadlockDetector: apply WhenCycleFound
    DeadlockDetector->>Dependency: invoke logic
    Dependency-->>DeadlockDetector: success
    DeadlockDetector-->>TestRunner: AbortsVictimTransaction
```

## 2. DetectAndResolve_WhenNoCycleFound_DoesNothing

```mermaid
sequenceDiagram
    actor TestRunner
    participant DeadlockDetector
    TestRunner->>DeadlockDetector: detectAndResolve()
    DeadlockDetector->>DeadlockDetector: apply WhenNoCycleFound
    DeadlockDetector->>Dependency: invoke logic
    Dependency-->>DeadlockDetector: success
    DeadlockDetector-->>TestRunner: DoesNothing
```

## 3. BuildWaitForGraph_CorrectlyMapsDependencies

```mermaid
sequenceDiagram
    actor TestRunner
    participant DeadlockDetector
    TestRunner->>DeadlockDetector: buildWaitForGraph()
    DeadlockDetector->>DeadlockDetector: apply CorrectlyMapsDependencies
    DeadlockDetector->>Dependency: invoke logic
    Dependency-->>DeadlockDetector: success
    DeadlockDetector-->>TestRunner: Success
```

## 4. ChooseVictim_SelectsTransactionWithLeastWorkDone

```mermaid
sequenceDiagram
    actor TestRunner
    participant DeadlockDetector
    TestRunner->>DeadlockDetector: chooseVictim()
    DeadlockDetector->>DeadlockDetector: apply SelectsTransactionWithLeastWorkDone
    DeadlockDetector->>Dependency: invoke logic
    Dependency-->>DeadlockDetector: success
    DeadlockDetector-->>TestRunner: Success
```

## 5. SetTimeout_ControlsBackgroundDetectionInterval

```mermaid
sequenceDiagram
    actor TestRunner
    participant DeadlockDetector
    TestRunner->>DeadlockDetector: setTimeout()
    DeadlockDetector->>DeadlockDetector: apply ControlsBackgroundDetectionInterval
    DeadlockDetector->>Dependency: invoke logic
    Dependency-->>DeadlockDetector: success
    DeadlockDetector-->>TestRunner: Success
```

