# Sequence Diagrams: Lexer

## 🆕 Added Properties & Methods for `Lexer`
To support the detailed sequence logic for unit testing, please update the `Lexer` class in your Class Diagram with the following properties and methods:

- **Method** added to `Lexer`: `tokenize()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **Lexer** class.

## 1. Tokenize_WhenValidString_ReturnsListOfTokens

```mermaid
sequenceDiagram
    actor TestRunner
    participant Lexer
    TestRunner->>Lexer: tokenize()
    Lexer->>Lexer: validate WhenValidString
    Lexer->>Lexer: process Tokenize
    Lexer-->>TestRunner: return ListOfTokens
```

## 2. Tokenize_IgnoresWhitespaceAndComments

```mermaid
sequenceDiagram
    actor TestRunner
    participant Lexer
    TestRunner->>Lexer: tokenize()
    Lexer->>Lexer: apply IgnoresWhitespaceAndComments
    Lexer->>Dependency: invoke logic
    Dependency-->>Lexer: success
    Lexer-->>TestRunner: Success
```

## 3. Tokenize_WhenUnclosedStringLiteral_ThrowsLexerException

```mermaid
sequenceDiagram
    actor TestRunner
    participant Lexer
    TestRunner->>Lexer: tokenize()
    Lexer->>Lexer: check WhenUnclosedStringLiteral
    Lexer-->>Lexer: condition failed
    Lexer-->>TestRunner: throws LexerException
```

## 4. Tokenize_IdentifiesOperatorsAndPunctuationCorrectly

```mermaid
sequenceDiagram
    actor TestRunner
    participant Lexer
    TestRunner->>Lexer: tokenize()
    Lexer->>Lexer: apply IdentifiesOperatorsAndPunctuationCorrectly
    Lexer->>Dependency: invoke logic
    Dependency-->>Lexer: success
    Lexer-->>TestRunner: Success
```

## 5. Tokenize_HandlesEscapedCharactersInStrings

```mermaid
sequenceDiagram
    actor TestRunner
    participant Lexer
    TestRunner->>Lexer: tokenize()
    Lexer->>Lexer: apply HandlesEscapedCharactersInStrings
    Lexer->>Dependency: invoke logic
    Dependency-->>Lexer: success
    Lexer-->>TestRunner: Success
```

