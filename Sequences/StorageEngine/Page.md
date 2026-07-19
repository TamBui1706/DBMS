# Sequence Diagrams: Page

## 🆕 Added Properties & Methods for `Page`
To support the detailed sequence logic for unit testing, please update the `Page` class in your Class Diagram with the following properties and methods:

- **Property** added to `Page`: `pageId`
- **Property** added to `Page`: `isDirty (Bool)`
- **Property** added to `Page`: `pinCount (Int)`
- **Method** added to `Page`: `compact()`
- **Method** added to `Page`: `deleteTuple()`
- **Method** added to `Page`: `hasSpace()`
- **Method** added to `Page`: `markDirty()`
- **Method** added to `Page`: `readTuple()`
- **Method** added to `Page`: `writeTuple()`

---

This file contains the detailed sequence diagrams for all 7 unit tests of the **Page** class.

## 1. Init_SetsPageIdAndClearsDirtyFlag

```mermaid
sequenceDiagram
    actor TestRunner
    participant Page
    TestRunner->>Page: init()
    Page->>Page: apply SetsPageIdAndClearsDirtyFlag
    Page->>Dependency: invoke logic
    Dependency-->>Page: success
    Page-->>TestRunner: Success
```

## 2. MarkDirty_SetsDirtyFlagToTrue

```mermaid
sequenceDiagram
    actor TestRunner
    participant Page
    TestRunner->>Page: markDirty()
    Page->>Page: apply SetsDirtyFlagToTrue
    Page->>Dependency: invoke logic
    Dependency-->>Page: success
    Page-->>TestRunner: Success
```

## 3. ReadTuple_ReturnsDataAtOffset

```mermaid
sequenceDiagram
    actor TestRunner
    participant Page
    TestRunner->>Page: readTuple()
    Page->>Page: apply ReturnsDataAtOffset
    Page->>Dependency: invoke logic
    Dependency-->>Page: success
    Page-->>TestRunner: Success
```

## 4. WriteTuple_SavesDataAndUpdatesFreeSpace

```mermaid
sequenceDiagram
    actor TestRunner
    participant Page
    TestRunner->>Page: writeTuple()
    Page->>Page: apply SavesDataAndUpdatesFreeSpace
    Page->>Dependency: invoke logic
    Dependency-->>Page: success
    Page-->>TestRunner: Success
```

## 5. HasSpace_ReturnsTrueIfTupleFits

```mermaid
sequenceDiagram
    actor TestRunner
    participant Page
    TestRunner->>Page: hasSpace()
    Page->>Page: apply ReturnsTrueIfTupleFits
    Page->>Dependency: invoke logic
    Dependency-->>Page: success
    Page-->>TestRunner: Success
```

## 6. Compact_ReorganizesTuplesToRemoveFragmentation

```mermaid
sequenceDiagram
    actor TestRunner
    participant Page
    TestRunner->>Page: compact()
    Page->>Page: apply ReorganizesTuplesToRemoveFragmentation
    Page->>Dependency: invoke logic
    Dependency-->>Page: success
    Page-->>TestRunner: Success
```

## 7. DeleteTuple_MarksSlotAsEmpty

```mermaid
sequenceDiagram
    actor TestRunner
    participant Page
    TestRunner->>Page: deleteTuple()
    Page->>Page: apply MarksSlotAsEmpty
    Page->>Dependency: invoke logic
    Dependency-->>Page: success
    Page-->>TestRunner: Success
```

