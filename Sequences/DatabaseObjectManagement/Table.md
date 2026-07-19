# Sequence Diagrams: Table

## 🆕 Added Properties & Methods for `Table`
To support the detailed sequence logic for unit testing, please update the `Table` class in your Class Diagram with the following properties and methods:

- **Property** added to `Table`: `rows (List)`
- **Property** added to `Table`: `columns (List)`
- **Method** added to `Table`: `addColumn()`
- **Method** added to `Table`: `delete()`
- **Method** added to `Table`: `dropColumn()`
- **Method** added to `Table`: `getRowCount()`
- **Method** added to `Table`: `insert()`
- **Method** added to `Table`: `renameColumn()`
- **Method** added to `Table`: `truncate()`
- **Method** added to `Table`: `update()`

---

This file contains the detailed sequence diagrams for all 12 unit tests of the **Table** class.

## 1. Insert_WhenValidRowAndConstraintsMet_AppendsRow

```mermaid
sequenceDiagram
    actor TestRunner
    participant Table
    TestRunner->>Table: insert()
    Table->>Table: apply WhenValidRowAndConstraintsMet
    Table->>Dependency: invoke logic
    Dependency-->>Table: success
    Table-->>TestRunner: AppendsRow
```

## 2. Insert_WhenPrimaryKeyViolated_ThrowsConstraintException

```mermaid
sequenceDiagram
    actor TestRunner
    participant Table
    TestRunner->>Table: insert()
    Table->>Table: check WhenPrimaryKeyViolated
    Table-->>Table: condition failed
    Table-->>TestRunner: throws ConstraintException
```

## 3. Update_WhenRowExists_ModifiesValues

```mermaid
sequenceDiagram
    actor TestRunner
    participant Table
    TestRunner->>Table: update()
    Table->>Table: apply WhenRowExists
    Table->>Dependency: invoke logic
    Dependency-->>Table: success
    Table-->>TestRunner: ModifiesValues
```

## 4. Update_WhenRowNotExists_ReturnsZeroAffectedRows

```mermaid
sequenceDiagram
    actor TestRunner
    participant Table
    TestRunner->>Table: update()
    Table->>Table: validate WhenRowNotExists
    Table->>Table: process Update
    Table-->>TestRunner: return ZeroAffectedRows
```

## 5. Delete_WhenRowExists_RemovesRow

```mermaid
sequenceDiagram
    actor TestRunner
    participant Table
    TestRunner->>Table: delete()
    Table->>Table: apply WhenRowExists
    Table->>Dependency: invoke logic
    Dependency-->>Table: success
    Table-->>TestRunner: RemovesRow
```

## 6. Insert_WhenForeignKeyViolated_ThrowsException

```mermaid
sequenceDiagram
    actor TestRunner
    participant Table
    TestRunner->>Table: insert()
    Table->>Table: check WhenForeignKeyViolated
    Table-->>Table: condition failed
    Table-->>TestRunner: throws Exception
```

## 7. Insert_WhenCheckConstraintViolated_ThrowsException

```mermaid
sequenceDiagram
    actor TestRunner
    participant Table
    TestRunner->>Table: insert()
    Table->>Table: check WhenCheckConstraintViolated
    Table-->>Table: condition failed
    Table-->>TestRunner: throws Exception
```

## 8. Truncate_RemovesAllRowsRapidly

```mermaid
sequenceDiagram
    actor TestRunner
    participant Table
    TestRunner->>Table: truncate()
    Table->>Table: apply RemovesAllRowsRapidly
    Table->>Dependency: invoke logic
    Dependency-->>Table: success
    Table-->>TestRunner: Success
```

## 9. AddColumn_AppendsColumnDefinitionToSchema

```mermaid
sequenceDiagram
    actor TestRunner
    participant Table
    TestRunner->>Table: addColumn()
    Table->>Table: apply AppendsColumnDefinitionToSchema
    Table->>Dependency: invoke logic
    Dependency-->>Table: success
    Table-->>TestRunner: Success
```

## 10. DropColumn_RemovesColumnAndData

```mermaid
sequenceDiagram
    actor TestRunner
    participant Table
    TestRunner->>Table: dropColumn()
    Table->>Table: apply RemovesColumnAndData
    Table->>Dependency: invoke logic
    Dependency-->>Table: success
    Table-->>TestRunner: Success
```

## 11. GetRowCount_ReturnsAccurateCount

```mermaid
sequenceDiagram
    actor TestRunner
    participant Table
    TestRunner->>Table: getRowCount()
    Table->>Table: apply ReturnsAccurateCount
    Table->>Dependency: invoke logic
    Dependency-->>Table: success
    Table-->>TestRunner: Success
```

## 12. RenameColumn_WhenExists_UpdatesMetadataAndViews

```mermaid
sequenceDiagram
    actor TestRunner
    participant Table
    TestRunner->>Table: renameColumn()
    Table->>Table: validate WhenExists
    Table->>Table: process RenameColumn
    Table-->>TestRunner: return UpdatesMetadataAndViews
```

