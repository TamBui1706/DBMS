# Sequence Diagrams: PrimaryKey

## 🆕 Added Properties & Methods for `PrimaryKey`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `PrimaryKey` class in your Class Diagram with these:**

- **Property** added to `PrimaryKey`: `columns` (List of columns participating in PK)
- **Method** added to `PrimaryKey`: `checkUniqueness(value)` (Validates global uniqueness in Table)

---

This file contains the detailed sequence diagrams for all unit tests of the **PrimaryKey** class in the Database Object Management subsystem.

## 1. Validate_WhenValueIsUniqueAndNotNull_Succeeds

```mermaid
sequenceDiagram
    actor Test
    participant PrimaryKey

    Test->>PrimaryKey: validate(value)
    PrimaryKey->>PrimaryKey: check value != null
    PrimaryKey->>PrimaryKey: checkUniqueness(value)
    PrimaryKey-->>PrimaryKey: true
    PrimaryKey-->>Test: success
```

## 2. Validate_WhenValueIsNull_ThrowsNullException

```mermaid
sequenceDiagram
    actor Test
    participant PrimaryKey

    Test->>PrimaryKey: validate(null)
    PrimaryKey->>PrimaryKey: check value != null
    PrimaryKey-->>PrimaryKey: false
    PrimaryKey-->>Test: throws NullException
```

## 3. Validate_WhenValueIsDuplicate_ThrowsDuplicateKeyException

```mermaid
sequenceDiagram
    actor Test
    participant PrimaryKey

    Test->>PrimaryKey: validate(duplicateValue)
    PrimaryKey->>PrimaryKey: check value != null
    PrimaryKey->>PrimaryKey: checkUniqueness(duplicateValue)
    PrimaryKey-->>PrimaryKey: false
    PrimaryKey-->>Test: throws DuplicateKeyException
```

