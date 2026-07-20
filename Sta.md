# DBMS Unit Tests Statistics

## Core Server & Connections (Total: 59 tests)
- `DatabaseServer`: 10 tests (Done)
- `ConnectionManager`: 10 tests (Done)
- `ClientSession`: 9 tests
- `DatabaseManager`: 12 tests (Done)
- `Database`: 8 tests (Done)
- `CatalogManager`: 10 tests

## Database Object Management (Total: 112 tests)
- `Schema`: 8 tests (Done)
- `Table`: 12 tests (Done)
- `View`: 6 tests  (Done)
- `StoredProcedure`: 6 tests
- `Function`: 5 tests (Done)
- `Sequence`: 6 tests
- `Trigger`: 6 tests
- `Partition`: 5 tests
- `Column`: 7 tests (Done)
- `Row`: 7 tests (Done)
- `DataType`: 5 tests (Done)
- `Constraint`: 1 tests (Done)
- `PrimaryKey`: 5 tests (Done)
- `ForeignKey`: 6 tests (Done)
- `UniqueConstraint`: 3 tests (Done)
- `CheckConstraint`: 3 tests (Done)
- `Index`: 1 tests (Done)
- `BTreeIndex`: 8 tests
- `HashIndex`: 6 tests
- `BitmapIndex`: 6 tests

## Query Processor (Total: 57 tests)
- `QueryProcessor`: 5 tests
- `SQLParser`: 7 tests
- `Lexer`: 5 tests
- `AST`: 5 tests
- `QueryOptimizer`: 7 tests
- `CostModel`: 5 tests
- `StatisticsManager`: 5 tests
- `LogicalPlan`: 5 tests
- `LogicalOperator`: 1 tests
- `PhysicalPlan`: 5 tests
- `PhysicalOperator`: 1 tests
- `QueryExecutor`: 6 tests

## Transaction Management (Total: 39 tests)
- `TransactionManager`: 8 tests
- `Transaction`: 6 tests
- `IsolationLevel`: 1 tests
- `TransactionState`: 1 tests
- `LockManager`: 8 tests
- `LockTable`: 5 tests
- `DeadlockDetector`: 5 tests
- `MVCCManager`: 5 tests

## Storage Engine (Total: 38 tests)
- `StorageEngine`: 6 tests
- `BufferPool`: 8 tests
- `PageReplacementAlgorithm`: 1 tests
- `Page`: 7 tests
- `FileManager`: 6 tests
- `DataFile`: 5 tests
- `IndexFile`: 5 tests

## Backup & Durability (Total: 23 tests)
- `RecoveryManager`: 6 tests
- `CheckpointManager`: 5 tests
- `WALManager`: 7 tests
- `LogRecord`: 5 tests

## Security & Access Control (Total: 26 tests)
- `SecurityManager`: 8 tests
- `User`: 7 tests
- `Role`: 6 tests
- `Permission`: 5 tests

---
## 🏆 SYSTEM GRAND TOTAL: **354** Unit Tests
