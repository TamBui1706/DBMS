# Sequence Diagrams: SQLParser

## 🆕 Added Properties & Methods for `SQLParser`
To support the detailed sequence logic for unit testing, the following missing properties/methods have been introduced. **Please update the `SQLParser` class in your Class Diagram with these:**

- **Method** added to `SQLParser`: `buildAST(tokens)` (Constructs tree from tokens)

---

This file contains the detailed sequence diagrams for all unit tests of the **SQLParser** class in the Query Processor subsystem.

## 1. Parse_WhenValidSelectStatement_GeneratesAST

```mermaid
sequenceDiagram
    actor Test
    participant SQLParser
    participant Lexer
    participant AST

    Test->>SQLParser: parse(sql)
    SQLParser->>Lexer: tokenize(sql)
    Lexer-->>SQLParser: tokens
    SQLParser->>SQLParser: validateSyntax(tokens)
    SQLParser->>AST: new AST()
    AST-->>SQLParser: astInstance
    SQLParser->>SQLParser: buildAST(tokens)
    SQLParser-->>Test: return astInstance
```

## 2. Parse_WhenInvalidSyntax_ThrowsSyntaxErrorException

```mermaid
sequenceDiagram
    actor Test
    participant SQLParser
    participant Lexer

    Test->>SQLParser: parse(invalidSql)
    SQLParser->>Lexer: tokenize(invalidSql)
    Lexer-->>SQLParser: tokens
    SQLParser->>SQLParser: validateSyntax(tokens)
    SQLParser-->>SQLParser: invalid syntax found
    SQLParser-->>Test: throws SyntaxErrorException
```

## 3. Parse_WhenUnsupportedCommand_ThrowsNotImplementedException

```mermaid
sequenceDiagram
    actor Test
    participant SQLParser

    Test->>SQLParser: parse("CREATE QUANTUM DB")
    SQLParser->>SQLParser: validateSyntax(tokens)
    SQLParser-->>SQLParser: unsupported token "QUANTUM"
    SQLParser-->>Test: throws NotImplementedException
```

