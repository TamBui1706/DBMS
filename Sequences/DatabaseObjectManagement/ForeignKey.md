# Sequence Diagrams: ForeignKey

## 🆕 Added Properties & Methods for `ForeignKey`
To support the detailed sequence logic for unit testing, please update the `ForeignKey` class in your Class Diagram with the following properties and methods:

- **Property** added to `ForeignKey`: `referenceTable`
- **Property** added to `ForeignKey`: `referenceColumn`
- **Property** added to `ForeignKey`: `onDeleteAction`
- **Method** added to `ForeignKey`: `onDeleteCascade()`
- **Method** added to `ForeignKey`: `onDeleteRestrict()`
- **Method** added to `ForeignKey`: `onUpdateCascade()`
- **Method** added to `ForeignKey`: `validate()`

---

This file contains the detailed sequence diagrams for all 6 unit tests of the **ForeignKey** class.

## 1. Validate_WhenReferencedRowExists_Succeeds

```mermaid
sequenceDiagram
    actor TestRunner
    participant ForeignKey
    TestRunner->>ForeignKey: validate()
    ForeignKey->>ForeignKey: validate WhenReferencedRowExists
    ForeignKey->>ForeignKey: process Validate
    ForeignKey-->>TestRunner: return Succeeds
```

## 2. Validate_WhenReferencedRowDoesNotExist_ThrowsForeignKeyException

```mermaid
sequenceDiagram
    actor TestRunner
    participant ForeignKey
    TestRunner->>ForeignKey: validate()
    ForeignKey->>ForeignKey: check WhenReferencedRowDoesNotExist
    ForeignKey-->>ForeignKey: condition failed
    ForeignKey-->>TestRunner: throws ForeignKeyException
```

## 3. Init_SetsReferenceTableCorrectly

```mermaid
sequenceDiagram
    actor TestRunner
    participant ForeignKey
    TestRunner->>ForeignKey: init()
    ForeignKey->>ForeignKey: apply SetsReferenceTableCorrectly
    ForeignKey->>Dependency: invoke logic
    Dependency-->>ForeignKey: success
    ForeignKey-->>TestRunner: Success
```

## 4. OnDeleteCascade_RemovesChildRowsWhenParentDeleted

```mermaid
sequenceDiagram
    actor TestRunner
    participant ForeignKey
    TestRunner->>ForeignKey: onDeleteCascade()
    ForeignKey->>ForeignKey: apply RemovesChildRowsWhenParentDeleted
    ForeignKey->>Dependency: invoke logic
    Dependency-->>ForeignKey: success
    ForeignKey-->>TestRunner: Success
```

## 5. OnDeleteRestrict_ThrowsExceptionWhenParentDeleted

```mermaid
sequenceDiagram
    actor TestRunner
    participant ForeignKey
    TestRunner->>ForeignKey: onDeleteRestrict()
    ForeignKey->>ForeignKey: apply ThrowsExceptionWhenParentDeleted
    ForeignKey->>Dependency: invoke logic
    Dependency-->>ForeignKey: success
    ForeignKey-->>TestRunner: Success
```

## 6. OnUpdateCascade_ModifiesChildRowsWhenParentKeyChanges

```mermaid
sequenceDiagram
    actor TestRunner
    participant ForeignKey
    TestRunner->>ForeignKey: onUpdateCascade()
    ForeignKey->>ForeignKey: apply ModifiesChildRowsWhenParentKeyChanges
    ForeignKey->>Dependency: invoke logic
    Dependency-->>ForeignKey: success
    ForeignKey-->>TestRunner: Success
```

