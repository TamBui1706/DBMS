# Sequence Diagrams: Partition

## 🆕 Added Properties & Methods for `Partition`
To support the detailed sequence logic for unit testing, please update the `Partition` class in your Class Diagram with the following properties and methods:

- **Property** added to `Partition`: `partitionKey`
- **Property** added to `Partition`: `minValue`
- **Property** added to `Partition`: `maxValue`
- **Method** added to `Partition`: `checkBoundary()`
- **Method** added to `Partition`: `merge()`
- **Method** added to `Partition`: `split()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **Partition** class.

## 1. Init_SetsPartitionKeyCorrectly

```mermaid
sequenceDiagram
    actor TestRunner
    participant Partition
    TestRunner->>Partition: init()
    Partition->>Partition: apply SetsPartitionKeyCorrectly
    Partition->>Dependency: invoke logic
    Dependency-->>Partition: success
    Partition-->>TestRunner: Success
```

## 2. CheckBoundary_WhenValueInRange_ReturnsTrue

```mermaid
sequenceDiagram
    actor TestRunner
    participant Partition
    TestRunner->>Partition: checkBoundary()
    Partition->>Partition: validate WhenValueInRange
    Partition->>Partition: process CheckBoundary
    Partition-->>TestRunner: return True
```

## 3. CheckBoundary_WhenValueOutOfRange_ReturnsFalse

```mermaid
sequenceDiagram
    actor TestRunner
    participant Partition
    TestRunner->>Partition: checkBoundary()
    Partition->>Partition: validate WhenValueOutOfRange
    Partition->>Partition: process CheckBoundary
    Partition-->>TestRunner: return False
```

## 4. Merge_CombinesTwoAdjacentPartitions

```mermaid
sequenceDiagram
    actor TestRunner
    participant Partition
    TestRunner->>Partition: merge()
    Partition->>Partition: apply CombinesTwoAdjacentPartitions
    Partition->>Dependency: invoke logic
    Dependency-->>Partition: success
    Partition-->>TestRunner: Success
```

## 5. Split_DividesPartitionAtGivenValue

```mermaid
sequenceDiagram
    actor TestRunner
    participant Partition
    TestRunner->>Partition: split()
    Partition->>Partition: apply DividesPartitionAtGivenValue
    Partition->>Dependency: invoke logic
    Dependency-->>Partition: success
    Partition-->>TestRunner: Success
```

