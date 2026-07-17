# Sequence Diagrams: Table

## 🆕 Added Properties & Methods for `Table`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `Table` class in your Class Diagram with these:**

- **Property** added to `Table`: `rows` (List or collection of Row objects)
- **Property** added to `Table`: `columns` (List of Column definitions)
- **Method** added to `Table`: `validateConstraints(row)` (Checks constraints like Primary Key before insert)

---

This file contains the detailed sequence diagrams for all unit tests of the **Table** class in the Database Object Management subsystem.

## 1. Insert_WhenValidRowAndConstraintsMet_AppendsRow

```mermaid
sequenceDiagram
    actor Test
    participant Table
    participant PrimaryKey

    Test->>Table: insert(Row)
    Table->>Table: validateConstraints(Row)
    Table->>PrimaryKey: validate(Row)
    PrimaryKey-->>Table: valid
    Table->>Table: rows.append(Row)
    Table-->>Test: success
```

## 2. Insert_WhenPrimaryKeyViolated_ThrowsConstraintException

```mermaid
sequenceDiagram
    actor Test
    participant Table
    participant PrimaryKey

    Test->>Table: insert(Row)
    Table->>Table: validateConstraints(Row)
    Table->>PrimaryKey: validate(Row)
    PrimaryKey-->>Table: throws ConstraintViolationException
    Table-->>Test: throws ConstraintViolationException
```

## 3. Update_WhenRowExists_ModifiesValues

```mermaid
sequenceDiagram
    actor Test
    participant Table
    participant Row

    Test->>Table: update(rowId, newValues)
    Table->>Table: find Row by rowId
    Table-->>Table: Row found
    Table->>Row: updateValues(newValues)
    Row-->>Table: success
    Table-->>Test: success
```

## 4. Update_WhenRowNotExists_ReturnsZeroAffectedRows

```mermaid
sequenceDiagram
    actor Test
    participant Table

    Test->>Table: update(invalidRowId, newValues)
    Table->>Table: find Row by rowId
    Table-->>Table: not found
    Table-->>Test: return 0 (rows affected)
```

## 5. Delete_WhenRowExists_RemovesRow

```mermaid
sequenceDiagram
    actor Test
    participant Table

    Test->>Table: delete(rowId)
    Table->>Table: find Row by rowId
    Table-->>Table: Row found
    Table->>Table: rows.remove(Row)
    Table-->>Test: success
```

