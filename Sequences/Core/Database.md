# Sequence Diagrams: Database

## 🆕 Added Properties & Methods for `Database`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `Database` class in your Class Diagram with these:**

- **Method** added to `Database`: `loadContext(pageData)` (Parses metadata loaded from StorageEngine)
- **Method** added to `Database`: `validateChecksum(pageData)` (Checks for data corruption before loading)

---

This file contains the detailed sequence diagrams for all unit tests of the **Database** class in the Core Server & Connections subsystem.

## 1. Init_SetsDatabaseNameCorrectly

```mermaid
sequenceDiagram
    actor Test
    participant Database

    Test->>Database: new Database(name)
    Database->>Database: name = name
    Database-->>Test: return instance
```

## 2. Open_WhenValidMetadata_LoadsDatabaseContext

```mermaid
sequenceDiagram
    actor Test
    participant Database
    participant StorageEngine
    participant BufferPool

    Test->>Database: open()
    Database->>StorageEngine: readMetadataPage(name)
    StorageEngine-->>Database: metadataPageId
    Database->>BufferPool: pinPage(metadataPageId)
    BufferPool-->>Database: pageData
    Database->>Database: validateChecksum(pageData)
    Database-->>Database: valid
    Database->>Database: loadContext(pageData)
    Database-->>Test: success
```

## 3. Open_WhenCorruptedMetadata_ThrowsCorruptionException

```mermaid
sequenceDiagram
    actor Test
    participant Database
    participant StorageEngine
    participant BufferPool

    Test->>Database: open()
    Database->>StorageEngine: readMetadataPage(name)
    StorageEngine-->>Database: metadataPageId
    Database->>BufferPool: pinPage(metadataPageId)
    BufferPool-->>Database: corruptedPageData
    Database->>Database: validateChecksum(corruptedPageData)
    Database-->>Database: invalid
    Database-->>Test: throws CorruptionException
```

