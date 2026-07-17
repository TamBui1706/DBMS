# Sequence Diagrams: LogRecord

## 🆕 Added Properties & Methods for `LogRecord`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `LogRecord` class in your Class Diagram with these:**

- **Property** added to `LogRecord`: `lsn` (Log Sequence Number), `type`, `payload`

---

This file contains the detailed sequence diagrams for all unit tests of the **LogRecord** class in the Backup & Durability subsystem.

## 1. Init_SetsLsnTypeAndPayloadData

```mermaid
sequenceDiagram
    actor Test
    participant LogRecord

    Test->>LogRecord: new LogRecord(lsn, type, payload)
    LogRecord->>LogRecord: assign properties
    LogRecord-->>Test: return instance
```

## 2. Serialize_ConvertsRecordToByteArray

```mermaid
sequenceDiagram
    actor Test
    participant LogRecord

    Test->>LogRecord: serialize()
    LogRecord->>LogRecord: encode(lsn, type, payload)
    LogRecord-->>Test: return byte[]
```

