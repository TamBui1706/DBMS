# Sequence Diagrams: BitmapIndex

## 🆕 Added Properties & Methods for `BitmapIndex`
To support the detailed sequence logic for unit testing, please update the `BitmapIndex` class in your Class Diagram with the following properties and methods:

- **Property** added to `BitmapIndex`: `bitmaps (Dict)`
- **Method** added to `BitmapIndex`: `bitwiseAND()`
- **Method** added to `BitmapIndex`: `bitwiseOR()`
- **Method** added to `BitmapIndex`: `compress()`
- **Method** added to `BitmapIndex`: `deleteKey()`
- **Method** added to `BitmapIndex`: `insertKey()`
- **Method** added to `BitmapIndex`: `search()`

---

This file contains the detailed sequence diagrams for all 6 unit tests of the **BitmapIndex** class.

## 1. InsertKey_UpdatesBitmapBitsForGivenValue

```mermaid
sequenceDiagram
    actor TestRunner
    participant BitmapIndex
    TestRunner->>BitmapIndex: insertKey()
    BitmapIndex->>BitmapIndex: apply UpdatesBitmapBitsForGivenValue
    BitmapIndex->>Dependency: invoke logic
    Dependency-->>BitmapIndex: success
    BitmapIndex-->>TestRunner: Success
```

## 2. Search_WhenKeyExists_UsesBitwiseOperationsToFindRID

```mermaid
sequenceDiagram
    actor TestRunner
    participant BitmapIndex
    TestRunner->>BitmapIndex: search()
    BitmapIndex->>BitmapIndex: apply WhenKeyExists
    BitmapIndex->>Dependency: invoke logic
    Dependency-->>BitmapIndex: success
    BitmapIndex-->>TestRunner: UsesBitwiseOperationsToFindRID
```

## 3. BitwiseAND_CombinesTwoBitmapsForComplexQuery

```mermaid
sequenceDiagram
    actor TestRunner
    participant BitmapIndex
    TestRunner->>BitmapIndex: bitwiseAND()
    BitmapIndex->>BitmapIndex: apply CombinesTwoBitmapsForComplexQuery
    BitmapIndex->>Dependency: invoke logic
    Dependency-->>BitmapIndex: success
    BitmapIndex-->>TestRunner: Success
```

## 4. BitwiseOR_CombinesTwoBitmapsForOrQuery

```mermaid
sequenceDiagram
    actor TestRunner
    participant BitmapIndex
    TestRunner->>BitmapIndex: bitwiseOR()
    BitmapIndex->>BitmapIndex: apply CombinesTwoBitmapsForOrQuery
    BitmapIndex->>Dependency: invoke logic
    Dependency-->>BitmapIndex: success
    BitmapIndex-->>TestRunner: Success
```

## 5. Compress_ReducesMemoryFootprintOfSparseBitmap

```mermaid
sequenceDiagram
    actor TestRunner
    participant BitmapIndex
    TestRunner->>BitmapIndex: compress()
    BitmapIndex->>BitmapIndex: apply ReducesMemoryFootprintOfSparseBitmap
    BitmapIndex->>Dependency: invoke logic
    Dependency-->>BitmapIndex: success
    BitmapIndex-->>TestRunner: Success
```

## 6. DeleteKey_ClearsBitForDeletedRow

```mermaid
sequenceDiagram
    actor TestRunner
    participant BitmapIndex
    TestRunner->>BitmapIndex: deleteKey()
    BitmapIndex->>BitmapIndex: apply ClearsBitForDeletedRow
    BitmapIndex->>Dependency: invoke logic
    Dependency-->>BitmapIndex: success
    BitmapIndex-->>TestRunner: Success
```

