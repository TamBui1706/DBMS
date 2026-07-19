# Sequence Diagrams: Trigger

## 🆕 Added Properties & Methods for `Trigger`
To support the detailed sequence logic for unit testing, please update the `Trigger` class in your Class Diagram with the following properties and methods:

- **Property** added to `Trigger`: `eventCondition`
- **Property** added to `Trigger`: `action`
- **Property** added to `Trigger`: `isActive (Bool)`
- **Method** added to `Trigger`: `disable()`
- **Method** added to `Trigger`: `enable()`
- **Method** added to `Trigger`: `fire()`
- **Method** added to `Trigger`: `validate()`

---

This file contains the detailed sequence diagrams for all 6 unit tests of the **Trigger** class.

## 1. Fire_OnEventConditionMet_ExecutesTriggerAction

```mermaid
sequenceDiagram
    actor TestRunner
    participant Trigger
    TestRunner->>Trigger: fire()
    Trigger->>Trigger: apply OnEventConditionMet
    Trigger->>Dependency: invoke logic
    Dependency-->>Trigger: success
    Trigger-->>TestRunner: ExecutesTriggerAction
```

## 2. Fire_OnEventConditionNotMet_SkipsExecution

```mermaid
sequenceDiagram
    actor TestRunner
    participant Trigger
    TestRunner->>Trigger: fire()
    Trigger->>Trigger: apply OnEventConditionNotMet
    Trigger->>Dependency: invoke logic
    Dependency-->>Trigger: success
    Trigger-->>TestRunner: SkipsExecution
```

## 3. Fire_WhenActionFails_RollsBackTransaction

```mermaid
sequenceDiagram
    actor TestRunner
    participant Trigger
    TestRunner->>Trigger: fire()
    Trigger->>Trigger: apply WhenActionFails
    Trigger->>Dependency: invoke logic
    Dependency-->>Trigger: success
    Trigger-->>TestRunner: RollsBackTransaction
```

## 4. Enable_ActivatesTrigger

```mermaid
sequenceDiagram
    actor TestRunner
    participant Trigger
    TestRunner->>Trigger: enable()
    Trigger->>Trigger: apply ActivatesTrigger
    Trigger->>Dependency: invoke logic
    Dependency-->>Trigger: success
    Trigger-->>TestRunner: Success
```

## 5. Disable_DeactivatesTrigger

```mermaid
sequenceDiagram
    actor TestRunner
    participant Trigger
    TestRunner->>Trigger: disable()
    Trigger->>Trigger: apply DeactivatesTrigger
    Trigger->>Dependency: invoke logic
    Dependency-->>Trigger: success
    Trigger-->>TestRunner: Success
```

## 6. Validate_EnsuresNoInfiniteTriggerLoops

```mermaid
sequenceDiagram
    actor TestRunner
    participant Trigger
    TestRunner->>Trigger: validate()
    Trigger->>Trigger: apply EnsuresNoInfiniteTriggerLoops
    Trigger->>Dependency: invoke logic
    Dependency-->>Trigger: success
    Trigger-->>TestRunner: Success
```

