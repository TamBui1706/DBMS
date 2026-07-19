# Sequence Diagrams: QueryProcessor

## 🆕 Added Properties & Methods for `QueryProcessor`
To support the detailed sequence logic for unit testing, please update the `QueryProcessor` class in your Class Diagram with the following properties and methods:

- **Method** added to `QueryProcessor`: `explain()`
- **Method** added to `QueryProcessor`: `prepareStatement()`
- **Method** added to `QueryProcessor`: `processQuery()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **QueryProcessor** class.

## 1. ProcessQuery_WhenValidSQL_ReturnsQueryResult

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryProcessor
    TestRunner->>QueryProcessor: processQuery()
    QueryProcessor->>QueryProcessor: validate WhenValidSQL
    QueryProcessor->>QueryProcessor: process ProcessQuery
    QueryProcessor-->>TestRunner: return QueryResult
```

## 2. ProcessQuery_WhenExecutionFails_RollsBackAndThrows

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryProcessor
    TestRunner->>QueryProcessor: processQuery()
    QueryProcessor->>QueryProcessor: check WhenExecutionFails
    QueryProcessor-->>QueryProcessor: condition failed
    QueryProcessor-->>TestRunner: throws RollsBackAnd
```

## 3. ProcessQuery_WhenTimeoutReached_AbortsQuery

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryProcessor
    TestRunner->>QueryProcessor: processQuery()
    QueryProcessor->>QueryProcessor: apply WhenTimeoutReached
    QueryProcessor->>Dependency: invoke logic
    Dependency-->>QueryProcessor: success
    QueryProcessor-->>TestRunner: AbortsQuery
```

## 4. Explain_ReturnsQueryExecutionPlanWithoutRunning

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryProcessor
    TestRunner->>QueryProcessor: explain()
    QueryProcessor->>QueryProcessor: apply ReturnsQueryExecutionPlanWithoutRunning
    QueryProcessor->>Dependency: invoke logic
    Dependency-->>QueryProcessor: success
    QueryProcessor-->>TestRunner: Success
```

## 5. PrepareStatement_CachesCompiledPlanForReuse

```mermaid
sequenceDiagram
    actor TestRunner
    participant QueryProcessor
    TestRunner->>QueryProcessor: prepareStatement()
    QueryProcessor->>QueryProcessor: apply CachesCompiledPlanForReuse
    QueryProcessor->>Dependency: invoke logic
    Dependency-->>QueryProcessor: success
    QueryProcessor-->>TestRunner: Success
```

