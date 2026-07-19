# Sequence Diagrams: Database

## 🆕 Added Properties & Methods for `Database`
To support the detailed sequence logic for unit testing, please update the `Database` class in your Class Diagram with the following properties and methods:

- **Property** added to `Database`: `schemaDict (Dict)`
- **Property** added to `Database`: `contextData`
- **Method** added to `Database`: `close()`
- **Method** added to `Database`: `createSchema()`
- **Method** added to `Database`: `getSchema()`
- **Method** added to `Database`: `open()`

---

This file contains the detailed sequence diagrams for all 8 unit tests of the **Database** class.

## 1. Init_SetsDatabaseNameCorrectly

```mermaid
sequenceDiagram
    actor TestRunner
    participant Database
    TestRunner->>Database: init()
    Database->>Database: apply SetsDatabaseNameCorrectly
    Database->>Dependency: invoke logic
    Dependency-->>Database: success
    Database-->>TestRunner: Success
```

## 2. Open_WhenValidMetadata_LoadsDatabaseContext

```mermaid
sequenceDiagram
    actor TestRunner
    participant Database
    TestRunner->>Database: open()
    Database->>Database: apply WhenValidMetadata
    Database->>Dependency: invoke logic
    Dependency-->>Database: success
    Database-->>TestRunner: LoadsDatabaseContext
```

## 3. Open_WhenCorruptedMetadata_ThrowsCorruptionException

```mermaid
sequenceDiagram
    actor TestRunner
    participant Database
    TestRunner->>Database: open()
    Database->>Database: check WhenCorruptedMetadata
    Database-->>Database: condition failed
    Database-->>TestRunner: throws CorruptionException
```

## 4. Close_FlushesUnsavedChangesAndReleasesLocks

```mermaid
sequenceDiagram
    actor TestRunner
    participant Database
    TestRunner->>Database: close()
    Database->>Database: apply FlushesUnsavedChangesAndReleasesLocks
    Database->>Dependency: invoke logic
    Dependency-->>Database: success
    Database-->>TestRunner: Success
```

## 5. GetSchema_WhenSchemaExists_ReturnsSchema

```mermaid
sequenceDiagram
    actor TestRunner
    participant Database
    TestRunner->>Database: getSchema()
    Database->>Database: validate WhenSchemaExists
    Database->>Database: process GetSchema
    Database-->>TestRunner: return Schema
```

## 6. CreateSchema_WhenNameValid_AddsToDatabase

```mermaid
sequenceDiagram
    actor TestRunner
    participant Database
    TestRunner->>Database: createSchema()
    Database->>Database: apply WhenNameValid
    Database->>Dependency: invoke logic
    Dependency-->>Database: success
    Database-->>TestRunner: AddsToDatabase
```

## 7. Close_WhenAlreadyClosed_DoesNothing

```mermaid
sequenceDiagram
    actor TestRunner
    participant Database
    TestRunner->>Database: close()
    Database->>Database: apply WhenAlreadyClosed
    Database->>Dependency: invoke logic
    Dependency-->>Database: success
    Database-->>TestRunner: DoesNothing
```

## 8. Open_WhenMissingDataFiles_ThrowsFileNotFoundException

```mermaid
sequenceDiagram
    actor TestRunner
    participant Database
    TestRunner->>Database: open()
    Database->>Database: check WhenMissingDataFiles
    Database-->>Database: condition failed
    Database-->>TestRunner: throws FileNotFoundException
```

