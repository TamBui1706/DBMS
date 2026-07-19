# Sequence Diagrams: SQLParser

## 🆕 Added Properties & Methods for `SQLParser`
To support the detailed sequence logic for unit testing, please update the `SQLParser` class in your Class Diagram with the following properties and methods:

- **Method** added to `SQLParser`: `parse()`

---

This file contains the detailed sequence diagrams for all 7 unit tests of the **SQLParser** class.

## 1. Parse_WhenValidSelectStatement_GeneratesAST

```mermaid
sequenceDiagram
    actor TestRunner
    participant SQLParser
    TestRunner->>SQLParser: parse()
    SQLParser->>SQLParser: apply WhenValidSelectStatement
    SQLParser->>Dependency: invoke logic
    Dependency-->>SQLParser: success
    SQLParser-->>TestRunner: GeneratesAST
```

## 2. Parse_WhenInvalidSyntax_ThrowsSyntaxErrorException

```mermaid
sequenceDiagram
    actor TestRunner
    participant SQLParser
    TestRunner->>SQLParser: parse()
    SQLParser->>SQLParser: check WhenInvalidSyntax
    SQLParser-->>SQLParser: condition failed
    SQLParser-->>TestRunner: throws SyntaxErrorException
```

## 3. Parse_WhenUnsupportedCommand_ThrowsNotImplementedException

```mermaid
sequenceDiagram
    actor TestRunner
    participant SQLParser
    TestRunner->>SQLParser: parse()
    SQLParser->>SQLParser: check WhenUnsupportedCommand
    SQLParser-->>SQLParser: condition failed
    SQLParser-->>TestRunner: throws NotImplementedException
```

## 4. Parse_WhenMissingSemicolon_SucceedsOrThrowsBasedOnDialect

```mermaid
sequenceDiagram
    actor TestRunner
    participant SQLParser
    TestRunner->>SQLParser: parse()
    SQLParser->>SQLParser: check WhenMissingSemicolon
    SQLParser-->>SQLParser: condition failed
    SQLParser-->>TestRunner: throws SucceedsOrBasedOnDialect
```

## 5. Parse_ComplexJoinAndGroupBy_ConstructsCorrectTree

```mermaid
sequenceDiagram
    actor TestRunner
    participant SQLParser
    TestRunner->>SQLParser: parse()
    SQLParser->>SQLParser: apply ComplexJoinAndGroupBy
    SQLParser->>Dependency: invoke logic
    Dependency-->>SQLParser: success
    SQLParser-->>TestRunner: ConstructsCorrectTree
```

## 6. Parse_NestedSubqueries_HandlesDepthLimits

```mermaid
sequenceDiagram
    actor TestRunner
    participant SQLParser
    TestRunner->>SQLParser: parse()
    SQLParser->>SQLParser: apply NestedSubqueries
    SQLParser->>Dependency: invoke logic
    Dependency-->>SQLParser: success
    SQLParser-->>TestRunner: HandlesDepthLimits
```

## 7. Parse_WhenMalformedDateLiteral_ThrowsException

```mermaid
sequenceDiagram
    actor TestRunner
    participant SQLParser
    TestRunner->>SQLParser: parse()
    SQLParser->>SQLParser: check WhenMalformedDateLiteral
    SQLParser-->>SQLParser: condition failed
    SQLParser-->>TestRunner: throws Exception
```

