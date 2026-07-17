# Sequence Diagrams: Index

This file contains the detailed sequence diagrams for all unit tests of the **Index** class in the Database Object Management subsystem.

## 1. Instantiation_OfAbstractClass_FailsWithTypeError

```mermaid
sequenceDiagram
    actor Test
    participant Index

    Test->>Index: new Index()
    Index-->>Test: throws TypeError (Cannot instantiate abstract class)
```

