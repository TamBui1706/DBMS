# Sequence Diagrams: LogRecord

## 🆕 Added Properties & Methods for `LogRecord`
To support the detailed sequence logic for unit testing, please update the `LogRecord` class in your Class Diagram with the following properties and methods:

- **Property** added to `LogRecord`: `lsn`
- **Property** added to `LogRecord`: `type`
- **Property** added to `LogRecord`: `payload`
- **Method** added to `LogRecord`: `deserialize()`
- **Method** added to `LogRecord`: `getTransactionId()`
- **Method** added to `LogRecord`: `getUndoInfo()`
- **Method** added to `LogRecord`: `serialize()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **LogRecord** class.

## 1. Init_SetsLsnTypeAndPayloadData

```mermaid
sequenceDiagram
    actor TestRunner
    participant LogRecord
    TestRunner->>LogRecord: init()
    LogRecord->>LogRecord: apply SetsLsnTypeAndPayloadData
    LogRecord->>Dependency: invoke logic
    Dependency-->>LogRecord: success
    LogRecord-->>TestRunner: Success
```

## 2. Serialize_ConvertsRecordToByteArray

```mermaid
sequenceDiagram
    actor TestRunner
    participant LogRecord
    TestRunner->>LogRecord: serialize()
    LogRecord->>LogRecord: apply ConvertsRecordToByteArray
    LogRecord->>Dependency: invoke logic
    Dependency-->>LogRecord: success
    LogRecord-->>TestRunner: Success
```

## 3. Deserialize_ReconstructsRecordFromBytes

```mermaid
sequenceDiagram
    actor TestRunner
    participant LogRecord
    TestRunner->>LogRecord: deserialize()
    LogRecord->>LogRecord: apply ReconstructsRecordFromBytes
    LogRecord->>Dependency: invoke logic
    Dependency-->>LogRecord: success
    LogRecord-->>TestRunner: Success
```

## 4. GetTransactionId_ReturnsAssociatedTx

```mermaid
sequenceDiagram
    actor TestRunner
    participant LogRecord
    TestRunner->>LogRecord: getTransactionId()
    LogRecord->>LogRecord: apply ReturnsAssociatedTx
    LogRecord->>Dependency: invoke logic
    Dependency-->>LogRecord: success
    LogRecord-->>TestRunner: Success
```

## 5. GetUndoInfo_ReturnsBeforeImageForRollback

```mermaid
sequenceDiagram
    actor TestRunner
    participant LogRecord
    TestRunner->>LogRecord: getUndoInfo()
    LogRecord->>LogRecord: apply ReturnsBeforeImageForRollback
    LogRecord->>Dependency: invoke logic
    Dependency-->>LogRecord: success
    LogRecord-->>TestRunner: Success
```

