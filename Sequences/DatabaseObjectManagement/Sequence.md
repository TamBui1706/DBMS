# Sequence Diagrams: Sequence

## 🆕 Added Properties & Methods for `Sequence`
To support the detailed sequence logic for unit testing, please update the `Sequence` class in your Class Diagram with the following properties and methods:

- **Property** added to `Sequence`: `currentValue (Int)`
- **Property** added to `Sequence`: `step (Int)`
- **Property** added to `Sequence`: `maxValue (Int)`
- **Method** added to `Sequence`: `currentValue()`
- **Method** added to `Sequence`: `nextValue()`
- **Method** added to `Sequence`: `reset()`

---

This file contains the detailed sequence diagrams for all 6 unit tests of the **Sequence** class.

## 1. NextValue_IncrementsByStepAndReturnsValue

```mermaid
sequenceDiagram
    actor TestRunner
    participant Sequence
    TestRunner->>Sequence: nextValue()
    Sequence->>Sequence: apply IncrementsByStepAndReturnsValue
    Sequence->>Dependency: invoke logic
    Dependency-->>Sequence: success
    Sequence-->>TestRunner: Success
```

## 2. NextValue_WhenMaxLimitReached_ThrowsOverflowException

```mermaid
sequenceDiagram
    actor TestRunner
    participant Sequence
    TestRunner->>Sequence: nextValue()
    Sequence->>Sequence: check WhenMaxLimitReached
    Sequence-->>Sequence: condition failed
    Sequence-->>TestRunner: throws OverflowException
```

## 3. Reset_SetsValueBackToStart

```mermaid
sequenceDiagram
    actor TestRunner
    participant Sequence
    TestRunner->>Sequence: reset()
    Sequence->>Sequence: apply SetsValueBackToStart
    Sequence->>Dependency: invoke logic
    Dependency-->>Sequence: success
    Sequence-->>TestRunner: Success
```

## 4. Init_SetsStartStepAndMaxLimit

```mermaid
sequenceDiagram
    actor TestRunner
    participant Sequence
    TestRunner->>Sequence: init()
    Sequence->>Sequence: apply SetsStartStepAndMaxLimit
    Sequence->>Dependency: invoke logic
    Dependency-->>Sequence: success
    Sequence-->>TestRunner: Success
```

## 5. CurrentValue_ReturnsCurrentWithoutIncrementing

```mermaid
sequenceDiagram
    actor TestRunner
    participant Sequence
    TestRunner->>Sequence: currentValue()
    Sequence->>Sequence: apply ReturnsCurrentWithoutIncrementing
    Sequence->>Dependency: invoke logic
    Dependency-->>Sequence: success
    Sequence-->>TestRunner: Success
```

## 6. NextValue_WhenStepIsNegative_DecrementsCorrectly

```mermaid
sequenceDiagram
    actor TestRunner
    participant Sequence
    TestRunner->>Sequence: nextValue()
    Sequence->>Sequence: apply WhenStepIsNegative
    Sequence->>Dependency: invoke logic
    Dependency-->>Sequence: success
    Sequence-->>TestRunner: DecrementsCorrectly
```

