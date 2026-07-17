# Sequence Diagrams: CheckConstraint

## 🆕 Added Properties & Methods for `CheckConstraint`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `CheckConstraint` class in your Class Diagram with these:**

- **Property** added to `CheckConstraint`: `expression` (The boolean logic to check)
- **Method** added to `CheckConstraint`: `evaluate(row)` (Evaluates expression against row data)

---

This file contains the detailed sequence diagrams for all unit tests of the **CheckConstraint** class in the Database Object Management subsystem.

## 1. Validate_WhenExpressionEvaluatesToTrue_Succeeds

```mermaid
sequenceDiagram
    actor Test
    participant CheckConstraint

    Test->>CheckConstraint: validate(row)
    CheckConstraint->>CheckConstraint: evaluate(self.expression, row)
    CheckConstraint-->>CheckConstraint: true
    CheckConstraint-->>Test: success
```

## 2. Validate_WhenExpressionEvaluatesToFalse_ThrowsCheckException

```mermaid
sequenceDiagram
    actor Test
    participant CheckConstraint

    Test->>CheckConstraint: validate(row)
    CheckConstraint->>CheckConstraint: evaluate(self.expression, row)
    CheckConstraint-->>CheckConstraint: false
    CheckConstraint-->>Test: throws CheckException
```

