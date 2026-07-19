# Sequence Diagrams: CheckConstraint

## 🆕 Added Properties & Methods for `CheckConstraint`
To support the detailed sequence logic for unit testing, please update the `CheckConstraint` class in your Class Diagram with the following properties and methods:

- **Property** added to `CheckConstraint`: `expression (String)`
- **Method** added to `CheckConstraint`: `validate()`

---

This file contains the detailed sequence diagrams for all 3 unit tests of the **CheckConstraint** class.

## 1. Validate_WhenExpressionEvaluatesToTrue_Succeeds

```mermaid
sequenceDiagram
    actor TestRunner
    participant CheckConstraint
    TestRunner->>CheckConstraint: validate()
    CheckConstraint->>CheckConstraint: validate WhenExpressionEvaluatesToTrue
    CheckConstraint->>CheckConstraint: process Validate
    CheckConstraint-->>TestRunner: return Succeeds
```

## 2. Validate_WhenExpressionEvaluatesToFalse_ThrowsCheckException

```mermaid
sequenceDiagram
    actor TestRunner
    participant CheckConstraint
    TestRunner->>CheckConstraint: validate()
    CheckConstraint->>CheckConstraint: check WhenExpressionEvaluatesToFalse
    CheckConstraint-->>CheckConstraint: condition failed
    CheckConstraint-->>TestRunner: throws CheckException
```

## 3. Validate_WhenExpressionUsesInvalidColumn_ThrowsException

```mermaid
sequenceDiagram
    actor TestRunner
    participant CheckConstraint
    TestRunner->>CheckConstraint: validate()
    CheckConstraint->>CheckConstraint: check WhenExpressionUsesInvalidColumn
    CheckConstraint-->>CheckConstraint: condition failed
    CheckConstraint-->>TestRunner: throws Exception
```

