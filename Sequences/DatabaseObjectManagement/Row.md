# Sequence Diagrams: Row

## 🆕 Added Properties & Methods for `Row`
To support the detailed sequence logic for unit testing, please update the `Row` class in your Class Diagram with the following properties and methods:

- **Property** added to `Row`: `rowId (UUID)`
- **Property** added to `Row`: `values (List)`
- **Method** added to `Row`: `deserialize()`
- **Method** added to `Row`: `getSize()`
- **Method** added to `Row`: `getValue()`
- **Method** added to `Row`: `serialize()`
- **Method** added to `Row`: `setValue()`

---

This file contains the detailed sequence diagrams for all 7 unit tests of the **Row** class.

## 1. Init_GeneratesRowIdAndInitializesValueList

```mermaid
sequenceDiagram
    actor TestRunner
    participant Row
    TestRunner->>Row: init()
    Row->>Row: apply GeneratesRowIdAndInitializesValueList
    Row->>Dependency: invoke logic
    Dependency-->>Row: success
    Row-->>TestRunner: Success
```

## 2. GetValue_WhenIndexValid_ReturnsData

```mermaid
sequenceDiagram
    actor TestRunner
    participant Row
    TestRunner->>Row: getValue()
    Row->>Row: validate WhenIndexValid
    Row->>Row: process GetValue
    Row-->>TestRunner: return Data
```

## 3. GetValue_WhenIndexOutOfBounds_ThrowsIndexException

```mermaid
sequenceDiagram
    actor TestRunner
    participant Row
    TestRunner->>Row: getValue()
    Row->>Row: check WhenIndexOutOfBounds
    Row-->>Row: condition failed
    Row-->>TestRunner: throws IndexException
```

## 4. SetValue_UpdatesDataAtIndex

```mermaid
sequenceDiagram
    actor TestRunner
    participant Row
    TestRunner->>Row: setValue()
    Row->>Row: apply UpdatesDataAtIndex
    Row->>Dependency: invoke logic
    Dependency-->>Row: success
    Row-->>TestRunner: Success
```

## 5. Serialize_ConvertsToByteArray

```mermaid
sequenceDiagram
    actor TestRunner
    participant Row
    TestRunner->>Row: serialize()
    Row->>Row: apply ConvertsToByteArray
    Row->>Dependency: invoke logic
    Dependency-->>Row: success
    Row-->>TestRunner: Success
```

## 6. Deserialize_ReadsFromByteArray

```mermaid
sequenceDiagram
    actor TestRunner
    participant Row
    TestRunner->>Row: deserialize()
    Row->>Row: apply ReadsFromByteArray
    Row->>Dependency: invoke logic
    Dependency-->>Row: success
    Row-->>TestRunner: Success
```

## 7. GetSize_ReturnsByteSizeOfAllValues

```mermaid
sequenceDiagram
    actor TestRunner
    participant Row
    TestRunner->>Row: getSize()
    Row->>Row: apply ReturnsByteSizeOfAllValues
    Row->>Dependency: invoke logic
    Dependency-->>Row: success
    Row-->>TestRunner: Success
```

