# Sequence Diagrams: Function

## 🆕 Added Properties & Methods for `Function`
To support the detailed sequence logic for unit testing, please update the `Function` class in your Class Diagram with the following properties and methods:

- **Property** added to `Function`: `arguments (List)`
- **Method** added to `Function`: `evaluate()`
- **Method** added to `Function`: `isDeterministic()`

---

This file contains the detailed sequence diagrams for all 5 unit tests of the **Function** class.

## 1. Evaluate_WhenValidArguments_ReturnsComputedValue

```mermaid
sequenceDiagram
    actor TestRunner
    participant Function
    TestRunner->>Function: evaluate()
    Function->>Function: validate WhenValidArguments
    Function->>Function: process Evaluate
    Function-->>TestRunner: return ComputedValue
```

## 2. Evaluate_WhenMissingArguments_ThrowsArgumentException

```mermaid
sequenceDiagram
    actor TestRunner
    participant Function
    TestRunner->>Function: evaluate()
    Function->>Function: check WhenMissingArguments
    Function-->>Function: condition failed
    Function-->>TestRunner: throws ArgumentException
```

## 3. Evaluate_WhenDivideByZero_ThrowsArithmeticException

```mermaid
sequenceDiagram
    actor TestRunner
    participant Function
    TestRunner->>Function: evaluate()
    Function->>Function: check WhenDivideByZero
    Function-->>Function: condition failed
    Function-->>TestRunner: throws ArithmeticException
```

## 4. IsDeterministic_ReturnsTrueIfNoExternalStateUsed

```mermaid
sequenceDiagram
    actor TestRunner
    participant Function
    TestRunner->>Function: isDeterministic()
    Function->>Function: apply ReturnsTrueIfNoExternalStateUsed
    Function->>Dependency: invoke logic
    Dependency-->>Function: success
    Function-->>TestRunner: Success
```

## 5. Evaluate_WhenNullPassedToStrictFunction_ReturnsNull

```mermaid
sequenceDiagram
    actor TestRunner
    participant Function
    TestRunner->>Function: evaluate()
    Function->>Function: validate WhenNullPassedToStrictFunction
    Function->>Function: process Evaluate
    Function-->>TestRunner: return Null
```

