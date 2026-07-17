# Sequence Diagrams: Row

## 🆕 Added Properties & Methods for `Row`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `Row` class in your Class Diagram with these:**

- **Property** added to `Row`: `rowId` (Unique identifier), `values` (Dictionary mapping col to value)

---

This file contains the detailed sequence diagrams for all unit tests of the **Row** class in the Database Object Management subsystem.

## 1. Init_GeneratesRowIdAndInitializesValueList

```mermaid
sequenceDiagram
    actor Test
    participant Row

    Test->>Row: new Row(values)
    Row->>Row: generate UUID for rowId
    Row->>Row: self.values = values
    Row-->>Test: return instance
```

## 2. GetValue_WhenIndexValid_ReturnsData

```mermaid
sequenceDiagram
    actor Test
    participant Row

    Test->>Row: getValue(columnIndex)
    Row->>Row: check columnIndex < len(self.values)
    Row-->>Test: return self.values[columnIndex]
```

