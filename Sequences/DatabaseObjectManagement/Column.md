# Sequence Diagrams: Column

## 🆕 Added Properties & Methods for `Column`
To support the detailed sequence logic for unit testing, please update the `Column` class in your Class Diagram with the following properties and methods:

- **Property** added to `Column`: `dataType`
- **Property** added to `Column`: `isNullable (Bool)`
- **Property** added to `Column`: `defaultValue`
- **Method** added to `Column`: `changeType()`
- **Method** added to `Column`: `setDefaultValue()`
- **Method** added to `Column`: `validateNullable()`
- **Method** added to `Column`: `validateType()`

---

This file contains the detailed sequence diagrams for all 7 unit tests of the **Column** class.

## 1. Init_SetsNameAndNullableFlags

```mermaid
sequenceDiagram
    actor TestRunner
    participant Column
    TestRunner->>Column: init()
    Column->>Column: apply SetsNameAndNullableFlags
    Column->>Dependency: invoke logic
    Dependency-->>Column: success
    Column-->>TestRunner: Success
```

## 2. ValidateType_WhenDataMatchesColumnType_Succeeds

```mermaid
sequenceDiagram
    actor TestRunner
    participant Column
    TestRunner->>Column: validateType()
    Column->>Column: validate WhenDataMatchesColumnType
    Column->>Column: process ValidateType
    Column-->>TestRunner: return Succeeds
```

## 3. ValidateType_WhenDataIsStringForIntColumn_ThrowsTypeException

```mermaid
sequenceDiagram
    actor TestRunner
    participant Column
    TestRunner->>Column: validateType()
    Column->>Column: check WhenDataIsStringForIntColumn
    Column-->>Column: condition failed
    Column-->>TestRunner: throws TypeException
```

## 4. ValidateNullable_WhenNullPassedToNotNullColumn_ThrowsException

```mermaid
sequenceDiagram
    actor TestRunner
    participant Column
    TestRunner->>Column: validateNullable()
    Column->>Column: check WhenNullPassedToNotNullColumn
    Column-->>Column: condition failed
    Column-->>TestRunner: throws Exception
```

## 5. SetDefaultValue_StoresDefaultExpression

```mermaid
sequenceDiagram
    actor TestRunner
    participant Column
    TestRunner->>Column: setDefaultValue()
    Column->>Column: apply StoresDefaultExpression
    Column->>Dependency: invoke logic
    Dependency-->>Column: success
    Column-->>TestRunner: Success
```

## 6. ChangeType_WhenCompatible_Succeeds

```mermaid
sequenceDiagram
    actor TestRunner
    participant Column
    TestRunner->>Column: changeType()
    Column->>Column: validate WhenCompatible
    Column->>Column: process ChangeType
    Column-->>TestRunner: return Succeeds
```

## 7. ChangeType_WhenIncompatible_ThrowsException

```mermaid
sequenceDiagram
    actor TestRunner
    participant Column
    TestRunner->>Column: changeType()
    Column->>Column: check WhenIncompatible
    Column-->>Column: condition failed
    Column-->>TestRunner: throws Exception
```

