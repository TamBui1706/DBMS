# Sequence Diagrams: DataType

This file contains the detailed sequence diagrams for all unit tests of the **DataType** class in the Database Object Management subsystem.

## 1. EnumValues_IncludeIntVarcharDateBoolean

```mermaid
sequenceDiagram
    actor Test
    participant DataType

    Test->>DataType: checkEnumValues()
    DataType-->>Test: return [INT, VARCHAR, DATE, BOOLEAN]
```

## 2. ParseString_WhenValidFormat_ReturnsDataTypeInstance

```mermaid
sequenceDiagram
    actor Test
    participant DataType

    Test->>DataType: parseString("VARCHAR")
    DataType-->>Test: return DataType.VARCHAR
```

