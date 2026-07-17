# Sequence Diagrams: DatabaseManager

## 🆕 Added Properties & Methods for `DatabaseManager`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `DatabaseManager` class in your Class Diagram with these:**

- **Method** added to `DatabaseManager`: `validateName(name: String)` (Checks for invalid characters in the DB name before creation)

---

This file contains the detailed sequence diagrams for all unit tests of the **DatabaseManager** class in the Core Server & Connections subsystem.

## 1. CreateDatabase_WhenNameIsValid_CreatesMetadataAndFiles

```mermaid
sequenceDiagram
    actor Test
    participant DatabaseManager
    participant CatalogManager
    participant StorageEngine
    participant Database

    Test->>DatabaseManager: createDatabase(dbName)
    DatabaseManager->>DatabaseManager: validateName(dbName)
    DatabaseManager->>CatalogManager: checkExists(dbName)
    CatalogManager-->>DatabaseManager: false
    DatabaseManager->>StorageEngine: allocateSpaceForDB(dbName)
    StorageEngine-->>DatabaseManager: blockId
    DatabaseManager->>Database: new Database(dbName)
    Database-->>DatabaseManager: dbInstance
    DatabaseManager->>CatalogManager: registerObject(dbInstance)
    CatalogManager-->>DatabaseManager: success
    DatabaseManager-->>Test: return dbInstance
```

## 2. CreateDatabase_WhenNameExists_ThrowsDuplicateDatabaseException

```mermaid
sequenceDiagram
    actor Test
    participant DatabaseManager
    participant CatalogManager

    Test->>DatabaseManager: createDatabase(dbName)
    DatabaseManager->>DatabaseManager: validateName(dbName)
    DatabaseManager->>CatalogManager: checkExists(dbName)
    CatalogManager-->>DatabaseManager: true
    DatabaseManager-->>Test: throws DuplicateDatabaseException
```

## 3. CreateDatabase_WhenInvalidCharacters_ThrowsValidationException

```mermaid
sequenceDiagram
    actor Test
    participant DatabaseManager

    Test->>DatabaseManager: createDatabase(invalidDbName)
    DatabaseManager->>DatabaseManager: validateName(invalidDbName)
    DatabaseManager-->>DatabaseManager: invalid
    DatabaseManager-->>Test: throws ValidationException
```

## 4. DropDatabase_WhenExists_RemovesAllAssociatedData

```mermaid
sequenceDiagram
    actor Test
    participant DatabaseManager
    participant ConnectionManager
    participant CatalogManager
    participant StorageEngine

    Test->>DatabaseManager: dropDatabase(dbName)
    DatabaseManager->>ConnectionManager: getActiveSessions(dbName)
    ConnectionManager-->>DatabaseManager: empty
    DatabaseManager->>CatalogManager: checkExists(dbName)
    CatalogManager-->>DatabaseManager: true
    DatabaseManager->>CatalogManager: removeObject(dbName)
    CatalogManager-->>DatabaseManager: success
    DatabaseManager->>StorageEngine: deallocateSpace(dbName)
    StorageEngine-->>DatabaseManager: success
    DatabaseManager-->>Test: return success
```

## 5. DropDatabase_WhenInUse_ThrowsConcurrencyException

```mermaid
sequenceDiagram
    actor Test
    participant DatabaseManager
    participant ConnectionManager

    Test->>DatabaseManager: dropDatabase(dbName)
    DatabaseManager->>ConnectionManager: getActiveSessions(dbName)
    ConnectionManager-->>DatabaseManager: [session1, session2]
    DatabaseManager-->>Test: throws ConcurrencyException
```

