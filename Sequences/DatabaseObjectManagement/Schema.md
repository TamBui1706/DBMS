# Sequence Diagrams: Schema

## 🆕 Added Properties & Methods for `Schema`
To support the detailed sequence logic for unit testing, please update the `Schema` class in your Class Diagram with the following properties and methods:

- **Property** added to `Schema`: `tables (Dict)`
- **Method** added to `Schema`: `createTable()`
- **Method** added to `Schema`: `dropTable()`
- **Method** added to `Schema`: `getTable()`
- **Method** added to `Schema`: `listTables()`
- **Method** added to `Schema`: `validate()`

---

This file contains the detailed sequence diagrams for all 8 unit tests of the **Schema** class.

## 1. Init_SetsSchemaName

```mermaid
sequenceDiagram
    actor TestRunner
    participant Schema
    TestRunner->>Schema: init()
    Schema->>Schema: apply SetsSchemaName
    Schema->>Dependency: invoke logic
    Dependency-->>Schema: success
    Schema-->>TestRunner: Success
```

## 2. CreateTable_WhenValidTable_RegistersInSchema

```mermaid
sequenceDiagram
    actor TestRunner
    participant Schema
    TestRunner->>Schema: createTable()
    Schema->>Schema: apply WhenValidTable
    Schema->>Dependency: invoke logic
    Dependency-->>Schema: success
    Schema-->>TestRunner: RegistersInSchema
```

## 3. CreateTable_WhenTableNameExists_ThrowsException

```mermaid
sequenceDiagram
    actor TestRunner
    participant Schema
    TestRunner->>Schema: createTable()
    Schema->>Schema: check WhenTableNameExists
    Schema-->>Schema: condition failed
    Schema-->>TestRunner: throws Exception
```

## 4. DropTable_WhenExists_RemovesFromSchema

```mermaid
sequenceDiagram
    actor TestRunner
    participant Schema
    TestRunner->>Schema: dropTable()
    Schema->>Schema: apply WhenExists
    Schema->>Dependency: invoke logic
    Dependency-->>Schema: success
    Schema-->>TestRunner: RemovesFromSchema
```

## 5. DropTable_WhenNotExists_ThrowsException

```mermaid
sequenceDiagram
    actor TestRunner
    participant Schema
    TestRunner->>Schema: dropTable()
    Schema->>Schema: check WhenNotExists
    Schema-->>Schema: condition failed
    Schema-->>TestRunner: throws Exception
```

## 6. GetTable_WhenExists_ReturnsTable

```mermaid
sequenceDiagram
    actor TestRunner
    participant Schema
    TestRunner->>Schema: getTable()
    Schema->>Schema: validate WhenExists
    Schema->>Schema: process GetTable
    Schema-->>TestRunner: return Table
```

## 7. ListTables_ReturnsAllRegisteredTables

```mermaid
sequenceDiagram
    actor TestRunner
    participant Schema
    TestRunner->>Schema: listTables()
    Schema->>Schema: apply ReturnsAllRegisteredTables
    Schema->>Dependency: invoke logic
    Dependency-->>Schema: success
    Schema-->>TestRunner: Success
```

## 8. Validate_EnsuresSchemaNameIsAlphanumeric

```mermaid
sequenceDiagram
    actor TestRunner
    participant Schema
    TestRunner->>Schema: validate()
    Schema->>Schema: apply EnsuresSchemaNameIsAlphanumeric
    Schema->>Dependency: invoke logic
    Dependency-->>Schema: success
    Schema-->>TestRunner: Success
```

