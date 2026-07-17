# Sequence Diagrams: Schema

## 🆕 Added Properties & Methods for `Schema`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `Schema` class in your Class Diagram with these:**

- **Property** added to `Schema`: `tables` (Dictionary holding registered Table objects)
- **Method** added to `Schema`: `validateTable(table)` (Validates table name and structure before adding)

---

This file contains the detailed sequence diagrams for all unit tests of the **Schema** class in the Database Object Management subsystem.

## 1. Init_SetsSchemaName

```mermaid
sequenceDiagram
    actor Test
    participant Schema

    Test->>Schema: new Schema(name)
    Schema->>Schema: self.name = name
    Schema-->>Test: return instance
```

## 2. CreateTable_WhenValidTable_RegistersInSchema

```mermaid
sequenceDiagram
    actor Test
    participant Schema
    participant Table

    Test->>Schema: createTable(Table)
    Schema->>Schema: validateTable(Table)
    Schema->>Schema: check tables.containsKey(Table.name)
    Schema-->>Schema: false
    Schema->>Schema: tables.put(Table.name, Table)
    Schema-->>Test: success
```

## 3. CreateTable_WhenTableNameExists_ThrowsException

```mermaid
sequenceDiagram
    actor Test
    participant Schema
    participant Table

    Test->>Schema: createTable(Table)
    Schema->>Schema: validateTable(Table)
    Schema->>Schema: check tables.containsKey(Table.name)
    Schema-->>Schema: true
    Schema-->>Test: throws DuplicateTableException
```

## 4. DropTable_WhenExists_RemovesFromSchema

```mermaid
sequenceDiagram
    actor Test
    participant Schema

    Test->>Schema: dropTable(tableName)
    Schema->>Schema: check tables.containsKey(tableName)
    Schema-->>Schema: true
    Schema->>Schema: tables.remove(tableName)
    Schema-->>Test: success
```

