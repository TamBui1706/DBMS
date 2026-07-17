# Sequence Diagrams: StatisticsManager

## 🆕 Added Properties & Methods for `StatisticsManager`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `StatisticsManager` class in your Class Diagram with these:**

- **Property** added to `StatisticsManager`: `rowCounts`, `cardinalities` (HashMaps for tables/columns)
- **Method** added to `StatisticsManager`: `updateStats(tableName)` (Recalculates metrics)

---

This file contains the detailed sequence diagrams for all unit tests of the **StatisticsManager** class in the Query Processor subsystem.

## 1. Collect_UpdatesRowCountsAndCardinality

```mermaid
sequenceDiagram
    actor Test
    participant StatisticsManager
    participant StorageEngine

    Test->>StatisticsManager: collect(table)
    StatisticsManager->>StorageEngine: scanMetadata(table)
    StorageEngine-->>StatisticsManager: rawData
    StatisticsManager->>StatisticsManager: updateStats(table)
    StatisticsManager->>StatisticsManager: self.rowCounts[table] = ...
    StatisticsManager-->>Test: success
```

## 2. GetStatistics_WhenCalled_ReturnsAccurateMetadata

```mermaid
sequenceDiagram
    actor Test
    participant StatisticsManager

    Test->>StatisticsManager: getStatistics(table)
    StatisticsManager->>StatisticsManager: self.rowCounts.get(table)
    StatisticsManager-->>Test: return MetadataStats
```

