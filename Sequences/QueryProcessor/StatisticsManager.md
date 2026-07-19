# Sequence Diagrams: StatisticsManager

## 🆕 Added Properties & Methods for `StatisticsManager`
To support the detailed sequence logic for unit testing, please update the `StatisticsManager` class in your Class Diagram with the following properties and methods:

- **Property** added to `StatisticsManager`: `rowCounts (Dict)`
- **Property** added to `StatisticsManager`: `cardinalities (Dict)`
- **Method** added to `StatisticsManager`: `buildHistogram()`
- **Method** added to `StatisticsManager`: `collect()`
- **Method** added to `StatisticsManager`: `estimateSelectivity()`
- **Method** added to `StatisticsManager`: `getStatistics()`
- **Method** added to `StatisticsManager`: `invalidateStats()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **StatisticsManager** class.

## 1. Collect_UpdatesRowCountsAndCardinality

```mermaid
sequenceDiagram
    actor TestRunner
    participant StatisticsManager
    TestRunner->>StatisticsManager: collect()
    StatisticsManager->>StatisticsManager: apply UpdatesRowCountsAndCardinality
    StatisticsManager->>Dependency: invoke logic
    Dependency-->>StatisticsManager: success
    StatisticsManager-->>TestRunner: Success
```

## 2. GetStatistics_WhenCalled_ReturnsAccurateMetadata

```mermaid
sequenceDiagram
    actor TestRunner
    participant StatisticsManager
    TestRunner->>StatisticsManager: getStatistics()
    StatisticsManager->>StatisticsManager: validate WhenCalled
    StatisticsManager->>StatisticsManager: process GetStatistics
    StatisticsManager-->>TestRunner: return AccurateMetadata
```

## 3. EstimateSelectivity_ReturnsPercentageOfRowsMatchingFilter

```mermaid
sequenceDiagram
    actor TestRunner
    participant StatisticsManager
    TestRunner->>StatisticsManager: estimateSelectivity()
    StatisticsManager->>StatisticsManager: apply ReturnsPercentageOfRowsMatchingFilter
    StatisticsManager->>Dependency: invoke logic
    Dependency-->>StatisticsManager: success
    StatisticsManager-->>TestRunner: Success
```

## 4. BuildHistogram_ForSkewedDataDistribution

```mermaid
sequenceDiagram
    actor TestRunner
    participant StatisticsManager
    TestRunner->>StatisticsManager: buildHistogram()
    StatisticsManager->>StatisticsManager: apply ForSkewedDataDistribution
    StatisticsManager->>Dependency: invoke logic
    Dependency-->>StatisticsManager: success
    StatisticsManager-->>TestRunner: Success
```

## 5. InvalidateStats_WhenTableModifiedSignificantly

```mermaid
sequenceDiagram
    actor TestRunner
    participant StatisticsManager
    TestRunner->>StatisticsManager: invalidateStats()
    StatisticsManager->>StatisticsManager: apply WhenTableModifiedSignificantly
    StatisticsManager->>Dependency: invoke logic
    Dependency-->>StatisticsManager: success
    StatisticsManager-->>TestRunner: Success
```

