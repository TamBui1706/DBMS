# Sequence Diagrams: HashIndex

## 🆕 Added Properties & Methods for `HashIndex`
To support the detailed sequence logic for unit testing, please update the `HashIndex` class in your Class Diagram with the following properties and methods:

- **Property** added to `HashIndex`: `hashTable (Dict)`
- **Method** added to `HashIndex`: `computeHash()`
- **Method** added to `HashIndex`: `deleteKey()`
- **Method** added to `HashIndex`: `handleCollision()`
- **Method** added to `HashIndex`: `insertKey()`
- **Method** added to `HashIndex`: `resize()`
- **Method** added to `HashIndex`: `search()`

---

This file contains the detailed sequence diagrams for all 6 unit tests of the **HashIndex** class.

## 1. InsertKey_ComputesHashAndAddsToBucket

```mermaid
sequenceDiagram
    actor TestRunner
    participant HashIndex
    TestRunner->>HashIndex: insertKey()
    HashIndex->>HashIndex: apply ComputesHashAndAddsToBucket
    HashIndex->>Dependency: invoke logic
    Dependency-->>HashIndex: success
    HashIndex-->>TestRunner: Success
```

## 2. Search_WhenKeyExists_ResolvesHashToRowID

```mermaid
sequenceDiagram
    actor TestRunner
    participant HashIndex
    TestRunner->>HashIndex: search()
    HashIndex->>HashIndex: apply WhenKeyExists
    HashIndex->>Dependency: invoke logic
    Dependency-->>HashIndex: success
    HashIndex-->>TestRunner: ResolvesHashToRowID
```

## 3. HandleCollision_CreatesLinkedListInBucket

```mermaid
sequenceDiagram
    actor TestRunner
    participant HashIndex
    TestRunner->>HashIndex: handleCollision()
    HashIndex->>HashIndex: apply CreatesLinkedListInBucket
    HashIndex->>Dependency: invoke logic
    Dependency-->>HashIndex: success
    HashIndex-->>TestRunner: Success
```

## 4. Resize_ExpandsHashTableWhenLoadFactorExceeded

```mermaid
sequenceDiagram
    actor TestRunner
    participant HashIndex
    TestRunner->>HashIndex: resize()
    HashIndex->>HashIndex: apply ExpandsHashTableWhenLoadFactorExceeded
    HashIndex->>Dependency: invoke logic
    Dependency-->>HashIndex: success
    HashIndex-->>TestRunner: Success
```

## 5. DeleteKey_RemovesFromBucketLinkedList

```mermaid
sequenceDiagram
    actor TestRunner
    participant HashIndex
    TestRunner->>HashIndex: deleteKey()
    HashIndex->>HashIndex: apply RemovesFromBucketLinkedList
    HashIndex->>Dependency: invoke logic
    Dependency-->>HashIndex: success
    HashIndex-->>TestRunner: Success
```

## 6. ComputeHash_DistributesKeysEvenly

```mermaid
sequenceDiagram
    actor TestRunner
    participant HashIndex
    TestRunner->>HashIndex: computeHash()
    HashIndex->>HashIndex: apply DistributesKeysEvenly
    HashIndex->>Dependency: invoke logic
    Dependency-->>HashIndex: success
    HashIndex-->>TestRunner: Success
```

