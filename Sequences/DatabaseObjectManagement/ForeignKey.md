# Sequence Diagrams: ForeignKey

## 🆕 Added Properties & Methods for `ForeignKey`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `ForeignKey` class in your Class Diagram with these:**

- **Property** added to `ForeignKey`: `referenceTable`, `referenceColumn`
- **Method** added to `ForeignKey`: `checkReferenceExists(value)` (Looks up reference table)

---

This file contains the detailed sequence diagrams for all unit tests of the **ForeignKey** class in the Database Object Management subsystem.

## 1. Validate_WhenReferencedRowExists_Succeeds

```mermaid
sequenceDiagram
    actor Test
    participant ForeignKey
    participant ReferenceTable

    Test->>ForeignKey: validate(value)
    ForeignKey->>ReferenceTable: checkReferenceExists(value)
    ReferenceTable-->>ForeignKey: true
    ForeignKey-->>Test: success
```

## 2. Validate_WhenReferencedRowDoesNotExist_ThrowsForeignKeyException

```mermaid
sequenceDiagram
    actor Test
    participant ForeignKey
    participant ReferenceTable

    Test->>ForeignKey: validate(value)
    ForeignKey->>ReferenceTable: checkReferenceExists(value)
    ReferenceTable-->>ForeignKey: false
    ForeignKey-->>Test: throws ForeignKeyException
```

## 3. Init_SetsReferenceTableCorrectly

```mermaid
sequenceDiagram
    actor Test
    participant ForeignKey

    Test->>ForeignKey: new ForeignKey(refTable, refCol)
    ForeignKey->>ForeignKey: self.referenceTable = refTable
    ForeignKey-->>Test: return instance
```

