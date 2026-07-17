# Sequence Diagrams: HashIndex

## 🆕 Added Properties & Methods for `HashIndex`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `HashIndex` class in your Class Diagram with these:**

- **Property** added to `HashIndex`: `hashTable` (Buckets for hashes)
- **Method** added to `HashIndex`: `computeHash(key)` (Hashing algorithm)

---

This file contains the detailed sequence diagrams for all unit tests of the **HashIndex** class in the Database Object Management subsystem.

## 1. InsertKey_ComputesHashAndAddsToBucket

```mermaid
sequenceDiagram
    actor Test
    participant HashIndex

    Test->>HashIndex: insertKey(key, rowId)
    HashIndex->>HashIndex: computeHash(key)
    HashIndex->>HashIndex: addToBucket(hash, rowId)
    HashIndex-->>Test: success
```

## 2. Search_WhenKeyExists_ResolvesHashToRowID

```mermaid
sequenceDiagram
    actor Test
    participant HashIndex

    Test->>HashIndex: search(key)
    HashIndex->>HashIndex: computeHash(key)
    HashIndex->>HashIndex: retrieveFromBucket(hash)
    HashIndex-->>Test: return rowId
```

## 3. HandleCollision_CreatesLinkedListInBucket

```mermaid
sequenceDiagram
    actor Test
    participant HashIndex

    Test->>HashIndex: insertKey(collidingKey, rowId2)
    HashIndex->>HashIndex: computeHash(collidingKey)
    HashIndex->>HashIndex: appendToBucketLinkedList(hash, rowId2)
    HashIndex-->>Test: success
```

