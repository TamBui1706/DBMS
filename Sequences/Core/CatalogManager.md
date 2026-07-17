# Sequence Diagrams: CatalogManager

## 🆕 Added Properties & Methods for `CatalogManager`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `CatalogManager` class in your Class Diagram with these:**

- **Property** added to `CatalogManager`: `catalogDict` (Dictionary/Map mapping object IDs to their Metadata)
- **Method** added to `CatalogManager`: `checkExists(objectId)` (Returns a boolean indicating if an object exists)
- **Method** added to `CatalogManager`: `removeObject(objectId)` (Removes an object from `catalogDict`)
- **Method** added to `CatalogManager`: `validate(dbObject)` (Validates object integrity before registering)

---

This file contains the detailed sequence diagrams for all unit tests of the **CatalogManager** class in the Core Server & Connections subsystem.

## 1. RegisterObject_WhenObjectIsValid_UpdatesCatalogDictionary

```mermaid
sequenceDiagram
    actor Test
    participant CatalogManager
    participant StorageEngine

    Test->>CatalogManager: registerObject(dbObject)
    CatalogManager->>CatalogManager: validate(dbObject)
    CatalogManager->>CatalogManager: checkExists(dbObject.id)
    CatalogManager-->>CatalogManager: false
    CatalogManager->>CatalogManager: catalogDict.put(dbObject.id, dbObject)
    CatalogManager->>StorageEngine: flushCatalogToDisk()
    StorageEngine-->>CatalogManager: success
    CatalogManager-->>Test: return success
```

## 2. RegisterObject_WhenDuplicateId_ThrowsException

```mermaid
sequenceDiagram
    actor Test
    participant CatalogManager

    Test->>CatalogManager: registerObject(dbObject)
    CatalogManager->>CatalogManager: validate(dbObject)
    CatalogManager->>CatalogManager: checkExists(dbObject.id)
    CatalogManager-->>CatalogManager: true
    CatalogManager-->>Test: throws DuplicateObjectIdException
```

## 3. FindObject_WhenExists_ReturnsObjectMetadata

```mermaid
sequenceDiagram
    actor Test
    participant CatalogManager

    Test->>CatalogManager: findObject(objectId)
    CatalogManager->>CatalogManager: checkExists(objectId)
    CatalogManager-->>CatalogManager: true
    CatalogManager->>CatalogManager: catalogDict.get(objectId)
    CatalogManager-->>Test: return objectMetadata
```

## 4. FindObject_WhenNotExists_ReturnsNull

```mermaid
sequenceDiagram
    actor Test
    participant CatalogManager

    Test->>CatalogManager: findObject(nonExistentId)
    CatalogManager->>CatalogManager: checkExists(nonExistentId)
    CatalogManager-->>CatalogManager: false
    CatalogManager-->>Test: return null
```

