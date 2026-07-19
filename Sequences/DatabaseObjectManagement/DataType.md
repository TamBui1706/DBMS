# Sequence Diagrams: DataType

## 🆕 Added Properties & Methods for `DataType`
To support the detailed sequence logic for unit testing, please update the `DataType` class in your Class Diagram with the following properties and methods:

- **Method** added to `DataType`: `getSize()`
- **Method** added to `DataType`: `isVariableLength()`
- **Method** added to `DataType`: `parseString()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **DataType** class.

## 1. EnumValues_IncludeIntVarcharDateBoolean

```mermaid
sequenceDiagram
    actor TestRunner
    participant DataType
    TestRunner->>DataType: enumValues()
    DataType->>DataType: apply IncludeIntVarcharDateBoolean
    DataType->>Dependency: invoke logic
    Dependency-->>DataType: success
    DataType-->>TestRunner: Success
```

## 2. ParseString_WhenValidFormat_ReturnsDataTypeInstance

```mermaid
sequenceDiagram
    actor TestRunner
    participant DataType
    TestRunner->>DataType: parseString()
    DataType->>DataType: validate WhenValidFormat
    DataType->>DataType: process ParseString
    DataType-->>TestRunner: return DataTypeInstance
```

## 3. ParseString_WhenInvalidFormat_ThrowsParseException

```mermaid
sequenceDiagram
    actor TestRunner
    participant DataType
    TestRunner->>DataType: parseString()
    DataType->>DataType: check WhenInvalidFormat
    DataType-->>DataType: condition failed
    DataType-->>TestRunner: throws ParseException
```

## 4. GetSize_ReturnsByteSizeForFixedTypes

```mermaid
sequenceDiagram
    actor TestRunner
    participant DataType
    TestRunner->>DataType: getSize()
    DataType->>DataType: apply ReturnsByteSizeForFixedTypes
    DataType->>Dependency: invoke logic
    Dependency-->>DataType: success
    DataType-->>TestRunner: Success
```

## 5. IsVariableLength_ReturnsTrueForVarchar

```mermaid
sequenceDiagram
    actor TestRunner
    participant DataType
    TestRunner->>DataType: isVariableLength()
    DataType->>DataType: apply ReturnsTrueForVarchar
    DataType->>Dependency: invoke logic
    Dependency-->>DataType: success
    DataType-->>TestRunner: Success
```

