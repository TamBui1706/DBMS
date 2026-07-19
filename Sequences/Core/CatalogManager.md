# Sequence Diagrams: CatalogManager

## 🆕 Added Properties & Methods for `CatalogManager`
To support the detailed sequence logic for unit testing, please update the `CatalogManager` class in your Class Diagram with the following properties and methods:

- **Property** added to `CatalogManager`: `catalogDict (Dict)`
- **Method** added to `CatalogManager`: `findObject()`
- **Method** added to `CatalogManager`: `flushCatalog()`
- **Method** added to `CatalogManager`: `loadCatalog()`
- **Method** added to `CatalogManager`: `registerObject()`
- **Method** added to `CatalogManager`: `removeObject()`
- **Method** added to `CatalogManager`: `updateObject()`

---

This file contains the detailed sequence diagrams for all 10 unit tests of the **CatalogManager** class.

## 1. RegisterObject_WhenObjectIsValid_UpdatesCatalogDictionary

```mermaid
sequenceDiagram
    actor TestRunner
    participant CatalogManager
    TestRunner->>CatalogManager: registerObject()
    CatalogManager->>CatalogManager: validate WhenObjectIsValid
    CatalogManager->>CatalogManager: process RegisterObject
    CatalogManager-->>TestRunner: return UpdatesCatalogDictionary
```

## 2. RegisterObject_WhenDuplicateId_ThrowsException

```mermaid
sequenceDiagram
    actor TestRunner
    participant CatalogManager
    TestRunner->>CatalogManager: registerObject()
    CatalogManager->>CatalogManager: check WhenDuplicateId
    CatalogManager-->>CatalogManager: condition failed
    CatalogManager-->>TestRunner: throws Exception
```

## 3. FindObject_WhenExists_ReturnsObjectMetadata

```mermaid
sequenceDiagram
    actor TestRunner
    participant CatalogManager
    TestRunner->>CatalogManager: findObject()
    CatalogManager->>CatalogManager: validate WhenExists
    CatalogManager->>CatalogManager: process FindObject
    CatalogManager-->>TestRunner: return ObjectMetadata
```

## 4. FindObject_WhenNotExists_ReturnsNull

```mermaid
sequenceDiagram
    actor TestRunner
    participant CatalogManager
    TestRunner->>CatalogManager: findObject()
    CatalogManager->>CatalogManager: validate WhenNotExists
    CatalogManager->>CatalogManager: process FindObject
    CatalogManager-->>TestRunner: return Null
```

## 5. RemoveObject_WhenExists_DeletesFromCatalog

```mermaid
sequenceDiagram
    actor TestRunner
    participant CatalogManager
    TestRunner->>CatalogManager: removeObject()
    CatalogManager->>CatalogManager: apply WhenExists
    CatalogManager->>Dependency: invoke logic
    Dependency-->>CatalogManager: success
    CatalogManager-->>TestRunner: DeletesFromCatalog
```

## 6. RemoveObject_WhenNotExists_ThrowsNotFoundException

```mermaid
sequenceDiagram
    actor TestRunner
    participant CatalogManager
    TestRunner->>CatalogManager: removeObject()
    CatalogManager->>CatalogManager: check WhenNotExists
    CatalogManager-->>CatalogManager: condition failed
    CatalogManager-->>TestRunner: throws NotFoundException
```

## 7. UpdateObject_WhenExists_RefreshesMetadata

```mermaid
sequenceDiagram
    actor TestRunner
    participant CatalogManager
    TestRunner->>CatalogManager: updateObject()
    CatalogManager->>CatalogManager: apply WhenExists
    CatalogManager->>Dependency: invoke logic
    Dependency-->>CatalogManager: success
    CatalogManager-->>TestRunner: RefreshesMetadata
```

## 8. FlushCatalog_WritesToStorageSuccessfully

```mermaid
sequenceDiagram
    actor TestRunner
    participant CatalogManager
    TestRunner->>CatalogManager: flushCatalog()
    CatalogManager->>CatalogManager: apply WritesToStorageSuccessfully
    CatalogManager->>Dependency: invoke logic
    Dependency-->>CatalogManager: success
    CatalogManager-->>TestRunner: Success
```

## 9. LoadCatalog_PopulatesMemoryFromDisk

```mermaid
sequenceDiagram
    actor TestRunner
    participant CatalogManager
    TestRunner->>CatalogManager: loadCatalog()
    CatalogManager->>CatalogManager: apply PopulatesMemoryFromDisk
    CatalogManager->>Dependency: invoke logic
    Dependency-->>CatalogManager: success
    CatalogManager-->>TestRunner: Success
```

## 10. LoadCatalog_WhenCorruptFile_TriggersRecoveryMode

```mermaid
sequenceDiagram
    actor TestRunner
    participant CatalogManager
    TestRunner->>CatalogManager: loadCatalog()
    CatalogManager->>CatalogManager: apply WhenCorruptFile
    CatalogManager->>Dependency: invoke logic
    Dependency-->>CatalogManager: success
    CatalogManager-->>TestRunner: TriggersRecoveryMode
```

