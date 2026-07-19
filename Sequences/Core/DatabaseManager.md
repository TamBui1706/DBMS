# Sequence Diagrams: DatabaseManager

## 🆕 Added Properties & Methods for `DatabaseManager`
To support the detailed sequence logic for unit testing, please update the `DatabaseManager` class in your Class Diagram with the following properties and methods:

- **Method** added to `DatabaseManager`: `createDatabase()`
- **Method** added to `DatabaseManager`: `dropDatabase()`
- **Method** added to `DatabaseManager`: `getDatabase()`
- **Method** added to `DatabaseManager`: `listDatabases()`
- **Method** added to `DatabaseManager`: `renameDatabase()`

---

This file contains the detailed sequence diagrams for all 12 unit tests of the **DatabaseManager** class.

## 1. CreateDatabase_WhenNameIsValid_CreatesMetadataAndFiles

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseManager
    TestRunner->>DatabaseManager: createDatabase()
    DatabaseManager->>DatabaseManager: validate WhenNameIsValid
    DatabaseManager->>DatabaseManager: process CreateDatabase
    DatabaseManager-->>TestRunner: return CreatesMetadataAndFiles
```

## 2. CreateDatabase_WhenNameExists_ThrowsDuplicateDatabaseException

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseManager
    TestRunner->>DatabaseManager: createDatabase()
    DatabaseManager->>DatabaseManager: check WhenNameExists
    DatabaseManager-->>DatabaseManager: condition failed
    DatabaseManager-->>TestRunner: throws DuplicateDatabaseException
```

## 3. CreateDatabase_WhenInvalidCharacters_ThrowsValidationException

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseManager
    TestRunner->>DatabaseManager: createDatabase()
    DatabaseManager->>DatabaseManager: check WhenInvalidCharacters
    DatabaseManager-->>DatabaseManager: condition failed
    DatabaseManager-->>TestRunner: throws ValidationException
```

## 4. DropDatabase_WhenExists_RemovesAllAssociatedData

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseManager
    TestRunner->>DatabaseManager: dropDatabase()
    DatabaseManager->>DatabaseManager: apply WhenExists
    DatabaseManager->>Dependency: invoke logic
    Dependency-->>DatabaseManager: success
    DatabaseManager-->>TestRunner: RemovesAllAssociatedData
```

## 5. DropDatabase_WhenInUse_ThrowsConcurrencyException

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseManager
    TestRunner->>DatabaseManager: dropDatabase()
    DatabaseManager->>DatabaseManager: check WhenInUse
    DatabaseManager-->>DatabaseManager: condition failed
    DatabaseManager-->>TestRunner: throws ConcurrencyException
```

## 6. GetDatabase_WhenExists_ReturnsDatabaseInstance

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseManager
    TestRunner->>DatabaseManager: getDatabase()
    DatabaseManager->>DatabaseManager: validate WhenExists
    DatabaseManager->>DatabaseManager: process GetDatabase
    DatabaseManager-->>TestRunner: return DatabaseInstance
```

## 7. GetDatabase_WhenNotExists_ThrowsDatabaseNotFoundException

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseManager
    TestRunner->>DatabaseManager: getDatabase()
    DatabaseManager->>DatabaseManager: check WhenNotExists
    DatabaseManager-->>DatabaseManager: condition failed
    DatabaseManager-->>TestRunner: throws DatabaseNotFoundException
```

## 8. ListDatabases_ReturnsAllRegisteredDatabases

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseManager
    TestRunner->>DatabaseManager: listDatabases()
    DatabaseManager->>DatabaseManager: apply ReturnsAllRegisteredDatabases
    DatabaseManager->>Dependency: invoke logic
    Dependency-->>DatabaseManager: success
    DatabaseManager-->>TestRunner: Success
```

## 9. RenameDatabase_WhenNewNameValid_UpdatesMetadata

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseManager
    TestRunner->>DatabaseManager: renameDatabase()
    DatabaseManager->>DatabaseManager: validate WhenNewNameValid
    DatabaseManager->>DatabaseManager: process RenameDatabase
    DatabaseManager-->>TestRunner: return UpdatesMetadata
```

## 10. CreateDatabase_WhenDiskFull_ThrowsInsufficientStorageException

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseManager
    TestRunner->>DatabaseManager: createDatabase()
    DatabaseManager->>DatabaseManager: check WhenDiskFull
    DatabaseManager-->>DatabaseManager: condition failed
    DatabaseManager-->>TestRunner: throws InsufficientStorageException
```

## 11. CreateDatabase_WhenNameTooLong_ThrowsValidationException

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseManager
    TestRunner->>DatabaseManager: createDatabase()
    DatabaseManager->>DatabaseManager: check WhenNameTooLong
    DatabaseManager-->>DatabaseManager: condition failed
    DatabaseManager-->>TestRunner: throws ValidationException
```

## 12. DropDatabase_WhenPermissionDenied_ThrowsSecurityException

```mermaid
sequenceDiagram
    actor TestRunner
    participant DatabaseManager
    TestRunner->>DatabaseManager: dropDatabase()
    DatabaseManager->>DatabaseManager: check WhenPermissionDenied
    DatabaseManager-->>DatabaseManager: condition failed
    DatabaseManager-->>TestRunner: throws SecurityException
```

