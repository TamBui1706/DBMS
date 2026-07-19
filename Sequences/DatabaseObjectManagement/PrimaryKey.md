# Sequence Diagrams: PrimaryKey

## 🆕 Added Properties & Methods for `PrimaryKey`
To support the detailed sequence logic for unit testing, please update the `PrimaryKey` class in your Class Diagram with the following properties and methods:

- **Property** added to `PrimaryKey`: `columns (List)`
- **Method** added to `PrimaryKey`: `drop()`
- **Method** added to `PrimaryKey`: `validate()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **PrimaryKey** class.

## 1. Validate_WhenValueIsUniqueAndNotNull_Succeeds

```mermaid
sequenceDiagram
    actor TestRunner
    participant PrimaryKey
    TestRunner->>PrimaryKey: validate()
    PrimaryKey->>PrimaryKey: validate WhenValueIsUniqueAndNotNull
    PrimaryKey->>PrimaryKey: process Validate
    PrimaryKey-->>TestRunner: return Succeeds
```

## 2. Validate_WhenValueIsNull_ThrowsNullException

```mermaid
sequenceDiagram
    actor TestRunner
    participant PrimaryKey
    TestRunner->>PrimaryKey: validate()
    PrimaryKey->>PrimaryKey: check WhenValueIsNull
    PrimaryKey-->>PrimaryKey: condition failed
    PrimaryKey-->>TestRunner: throws NullException
```

## 3. Validate_WhenValueIsDuplicate_ThrowsDuplicateKeyException

```mermaid
sequenceDiagram
    actor TestRunner
    participant PrimaryKey
    TestRunner->>PrimaryKey: validate()
    PrimaryKey->>PrimaryKey: check WhenValueIsDuplicate
    PrimaryKey-->>PrimaryKey: condition failed
    PrimaryKey-->>TestRunner: throws DuplicateKeyException
```

## 4. Validate_WithCompositeKey_ChecksAllColumns

```mermaid
sequenceDiagram
    actor TestRunner
    participant PrimaryKey
    TestRunner->>PrimaryKey: validate()
    PrimaryKey->>PrimaryKey: apply WithCompositeKey
    PrimaryKey->>Dependency: invoke logic
    Dependency-->>PrimaryKey: success
    PrimaryKey-->>TestRunner: ChecksAllColumns
```

## 5. Drop_RemovesIndexFromStorage

```mermaid
sequenceDiagram
    actor TestRunner
    participant PrimaryKey
    TestRunner->>PrimaryKey: drop()
    PrimaryKey->>PrimaryKey: apply RemovesIndexFromStorage
    PrimaryKey->>Dependency: invoke logic
    Dependency-->>PrimaryKey: success
    PrimaryKey-->>TestRunner: Success
```

