# DBMS Architecture Design

This project is a comprehensive, high-level object-oriented design and implementation plan for a modern Database Management System (DBMS).

## 🏗️ System Architecture


## 🧠 Mind Map

Below is the mind map illustrating the layered architecture of the DBMS.

![DBMS Mindmap](./Mindmap.png)

### Mindmap (Text Representation)

```mermaid
flowchart LR
    DBMS[Database Management System]


    Concurrency[Concurrency] --- Transaction[Transaction Management]
    Deadlock[Deadlock] --- Transaction
    TxnManager[Transaction Manager] --- Transaction
    LockManager[Lock Manager] --- Transaction
    Isolation[Isolation Management] --- Transaction
    Transaction --- DBMS

    DataFile[Data File Manager] --- Storage[Storage Engine]
    BufferPool[Buffer Pool + Cache] --- Storage
    RecordMgmt[Record Management] --- Storage
    StorageIndexMgmt[Index Management] --- Storage
    AccessMethods[Access Methods] --- Storage
    StorageAlloc[Storage Allocation] --- Storage
    LogFile[Log File] --- Storage
    Storage --- DBMS

    BackupMgmt[Backup Management] --- Backup[Backup & Durability]
    RestoreMgmt[Restore Management] --- Backup
    TxnLogging[Transaction Logging] --- Backup
    Recovery[Recovery] --- Backup
    Checkpoint[Checkpoint] --- Backup
    Replication[Replication] --- Backup
    Backup --- DBMS

    BackupStrategy[Backup Strategy] --- Admin[Administration & Monitoring]
    Monitoring[Monitoring & Logging] --- Admin
    ConfigMgmt[Configuration Management] --- Admin
    ImportExport[Import and Export] --- Admin
    Admin --- DBMS


    DBMS --- QP[Query Processor]
    QP --- Parser[SQL Parser]
    QP --- Optimizer[Query Optimizer]
    QP --- Execution[Query Execution]
    QP --- Validation[Query Validation]
    QP --- Result[Result Processing]

    DBMS --- DBObject[Database Object Management]
    DBObject --- DBMgmt[Database Management]
    DBObject --- SchemaMgmt[Schema Management]
    DBObject --- TableMgmt[Table Management]
    DBObject --- ViewMgmt[View Management]
    DBObject --- RelMgmt[Relationship Management]
    DBObject --- DBObjIndexMgmt[Index Management]
    DBObject --- ConstraintMgmt[Constraint Management]
    DBObject --- ColumnMgmt[Column Management]
    DBObject --- ProgObjects[Programmable Objects]
    DBObject --- DataType[Data Type]
    DBObject --- MetaMgmt[Metadata Management]

    DBMS --- Perf[Performance]
    Perf --- PerfAnalyzer[Query Performance Analyzer]
    Perf --- Caching[Caching]
    Perf --- MemMgmt[Memory Management]
    Perf --- DataDist[Data Distribution]
    Perf --- ConnThread[Connection & Thread Management]

    DBMS --- Security[Security & Access Control]
    Security --- Auth[Authentication]
    Security --- Authorization[Authorization]
    Security --- AccessCtrl[Access Control]
    Security --- UserMgmt[User Management]
    Security --- Encryption[Encryption]
    Security --- Auditing[Auditing]

    style DBMS fill:#e6e6ff,stroke:#b3b3ff,stroke-width:2px
    style Transaction fill:#e6e6ff,stroke:#b3b3ff,stroke-width:2px
    style Storage fill:#e6e6ff,stroke:#b3b3ff,stroke-width:2px
    style Backup fill:#e6e6ff,stroke:#b3b3ff,stroke-width:2px
    style Admin fill:#e6e6ff,stroke:#b3b3ff,stroke-width:2px
    style QP fill:#e6e6ff,stroke:#b3b3ff,stroke-width:2px
    style DBObject fill:#e6e6ff,stroke:#b3b3ff,stroke-width:2px
    style Perf fill:#e6e6ff,stroke:#b3b3ff,stroke-width:2px
    style Security fill:#e6e6ff,stroke:#b3b3ff,stroke-width:2px
```

## 📐 Class Diagrams

The detailed UML Class Diagrams defining the entities, properties, and relationships within each subsystem:

```mermaid
classDiagram
    class DBMS {
        -QueryProcessor queryProcessor
        -StorageEngine storageEngine
        -TransactionManager transactionManager
        -DatabaseObjectManager objectManager
        -SecurityManager securityManager
        -BackupDurabilityManager backupManager
        -PerformanceManager performanceManager
        -AdminMonitorManager adminManager
        +startSystem()
        +stopSystem()
    }

    class QueryProcessor {
        -SQLParser sqlParser
        -QueryOptimizer queryOptimizer
        -QueryExecution queryExecution
        -QueryValidation queryValidation
    }
    class SQLParser {
        -LexicalAnalyzer lexer
        -SyntaxAnalyzer syntaxAnalyzer
        -ASTBuilder astBuilder
    }
    class LexicalAnalyzer {
        +tokenize(String sql)
    }
    class SyntaxAnalyzer {
        +checkSyntax(TokenList tokens)
    }
    class ASTBuilder {
        +buildTree(TokenList tokens)
    }
    class QueryOptimizer {
        -CostBasedOptimizer cbo
        -RuleBasedOptimizer rbo
    }
    class CostBasedOptimizer {
        +estimateCost(Plan p)
    }
    class RuleBasedOptimizer {
        +applyRules(Plan p)
    }
    class QueryExecution {
        -OperatorScheduler scheduler
        -ExecutionEngine engine
        -ResourceManager resourceManager
    }
    class OperatorScheduler {
        +schedule(Plan p)
    }
    class ExecutionEngine {
        +executeNode(OpNode n)
    }

    QueryProcessor *-- SQLParser
    QueryProcessor *-- QueryOptimizer
    QueryProcessor *-- QueryExecution
    SQLParser *-- LexicalAnalyzer
    SQLParser *-- SyntaxAnalyzer
    SQLParser *-- ASTBuilder
    QueryOptimizer *-- CostBasedOptimizer
    QueryOptimizer *-- RuleBasedOptimizer
    QueryExecution *-- OperatorScheduler
    QueryExecution *-- ExecutionEngine

    class StorageEngine {
        -BufferPoolManager bufferPool
        -RecordManager recordManager
        -IndexManager indexManager
        -AccessMethods accessMethods
        -LogManager logManager
    }
    class BufferPoolManager {
        -PageReplacementAlgorithm replacementAlgo
        -BufferFrameManager frameManager
        -DirtyPageWriter dirtyWriter
        +fetchPage(PageID pid)
    }
    class PageReplacementAlgorithm {
        <<interface>>
        +findVictim()
    }
    class BufferFrameManager {
        +allocateFrame()
    }
    class DirtyPageWriter {
        +flushDirtyPages()
    }
    class RecordManager {
        -RecordLayoutManager layoutManager
        -TupleHeaderManager headerManager
        -RIDGenerator ridGenerator
    }
    class RecordLayoutManager {
        +formatRecord(Tuple t)
    }
    class RIDGenerator {
        +generateRID()
    }
    class IndexManager {
        -IndexMetadata metadata
        -BTreeCoreEngine bTreeEngine
    }
    class BTreeCoreEngine {
        +insertNode(Key k, RID r)
    }
    class AccessMethods {
        -SequentialScan seqScan
        -IndexScan idxScan
    }
    class SequentialScan {
        +scan()
    }
    class IndexScan {
        +scan(Key k)
    }
    class LogManager {
        -LSNGenerator lsnGenerator
        -WALBuffer walBuffer
    }
    class LSNGenerator {
        +nextLSN()
    }
    class WALBuffer {
        +appendLog(LogRecord l)
    }

    StorageEngine *-- BufferPoolManager
    StorageEngine *-- RecordManager
    StorageEngine *-- IndexManager
    StorageEngine *-- AccessMethods
    StorageEngine *-- LogManager
    BufferPoolManager *-- PageReplacementAlgorithm
    BufferPoolManager *-- BufferFrameManager
    BufferPoolManager *-- DirtyPageWriter
    RecordManager *-- RecordLayoutManager
    RecordManager *-- RIDGenerator
    IndexManager *-- BTreeCoreEngine
    AccessMethods *-- SequentialScan
    AccessMethods *-- IndexScan
    LogManager *-- LSNGenerator
    LogManager *-- WALBuffer

    class TransactionManager {
        -TransactionTable txnTable
        -LockManager lockManager
        -IsolationManager isolationManager
        -DeadlockDetector deadlockDetector
    }
    class LockManager {
        -LockTable lockTable
        +acquireLock(TransactionID txnId, ResourceID resId, LockMode mode)
    }
    class LockTable {
        +getLocks(ResourceID r)
    }
    class DeadlockDetector {
        -WaitForGraph waitGraph
        -VictimSelectionStrategy victimStrategy
    }
    class WaitForGraph {
        +addEdge(TransactionID t1, TransactionID t2)
    }
    class IsolationManager {
        -ReadViewGenerator snapshotGen
        -VersionChainBuilder mvccBuilder
    }
    class ReadViewGenerator {
        +createSnapshot(TransactionID t)
    }
    class VersionChainBuilder {
        +linkVersion(Record r1, Record r2)
    }

    TransactionManager *-- LockManager
    TransactionManager *-- DeadlockDetector
    TransactionManager *-- IsolationManager
    LockManager *-- LockTable
    DeadlockDetector *-- WaitForGraph
    IsolationManager *-- ReadViewGenerator
    IsolationManager *-- VersionChainBuilder

    class DatabaseObjectManager {
        -SchemaManager schemaManager
        -TableManager tableManager
        -ViewManager viewManager
        -ConstraintManager constraintManager
        -ColumnManager columnManager
    }
    class SchemaManager {
        +createSchema(String name)
    }
    class TableManager {
        -TableCreator tableCreator
        -PhysicalFileRegistration fileRegistry
    }
    class PhysicalFileRegistration {
        +registerFile(String path)
    }
    class ConstraintManager {
        -PrimaryKeyValidator pkValidator
        -UniqueConstraintManager ukManager
        -CheckConstraintEvaluator checkEvaluator
    }
    class PrimaryKeyValidator {
        +validatePK(Record r)
    }
    class ColumnManager {
        -ColumnDefinitionManager colDefMgr
        -DefaultValueManager defValMgr
    }

    DatabaseObjectManager *-- SchemaManager
    DatabaseObjectManager *-- TableManager
    DatabaseObjectManager *-- ConstraintManager
    DatabaseObjectManager *-- ColumnManager
    ConstraintManager *-- PrimaryKeyValidator
    TableManager *-- PhysicalFileRegistration

    class BackupDurabilityManager {
        -BackupManager backupManager
        -RestoreManager restoreManager
        -RecoveryManager recoveryManager
        -CheckpointManager checkpointMgr
    }
    class RecoveryManager {
        -CrashRecoveryManager crashRecovery
        -REDOLogApplier redoApplier
        -UNDOLogApplier undoApplier
    }
    class REDOLogApplier {
        +apply(LogRecord l)
    }
    class UNDOLogApplier {
        +rollback(LogRecord l)
    }
    class CheckpointManager {
        -CheckpointerDaemon checkpointer
        -FuzzyCheckpointController fuzzyController
    }
    class FuzzyCheckpointController {
        +triggerFuzzy()
    }
    class RestoreManager {
        -RestoreValidator validator
        -FileRestorer fileRestorer
    }
    BackupDurabilityManager *-- RecoveryManager
    BackupDurabilityManager *-- CheckpointManager
    BackupDurabilityManager *-- RestoreManager
    RecoveryManager *-- REDOLogApplier
    RecoveryManager *-- UNDOLogApplier
    CheckpointManager *-- FuzzyCheckpointController

    class SecurityManager {
        -Authentication authModule
        -Authorization authzModule
        -AccessControl accessControl
        -UserManagement userMgmt
    }
    class Authentication {
        +authenticateUser(Credentials creds)
    }
    class AccessControl {
        -RBACPolicyEvaluator rbacEvaluator
        -DACEvaluator dacEvaluator
    }
    class RBACPolicyEvaluator {
        +evaluate(Role r, Action a)
    }
    class UserManagement {
        -UserCatalog userCatalog
        -RoleHierarchyResolver roleResolver
    }
    class RoleHierarchyResolver {
        +resolveRoles(User u)
    }
    SecurityManager *-- Authentication
    SecurityManager *-- AccessControl
    SecurityManager *-- UserManagement
    AccessControl *-- RBACPolicyEvaluator
    UserManagement *-- RoleHierarchyResolver

    class PerformanceManager {
        -QueryPerformanceAnalyzer perfAnalyzer
        -MemoryManagement memMgmt
        -Caching cacheMgmt
    }
    class QueryPerformanceAnalyzer {
        -IndexUsageAdvisor indexAdvisor
        -SlowQueryProfiler slowProfiler
    }
    class MemoryManagement {
        -SharedMemoryAllocator sharedAlloc
        -MemoryPoolManager poolMgr
    }
    class AdminMonitorManager {
        -MonitoringLogging monitoring
        -ConfigurationManagement configMgmt
    }
    class MonitoringLogging {
        -PerformanceMetricsCollector metricsCollector
        -SystemErrorLogWriter errorWriter
    }

    PerformanceManager *-- QueryPerformanceAnalyzer
    PerformanceManager *-- MemoryManagement
    AdminMonitorManager *-- MonitoringLogging

    DBMS *-- QueryProcessor
    DBMS *-- StorageEngine
    DBMS *-- TransactionManager
    DBMS *-- DatabaseObjectManager
    DBMS *-- SecurityManager
    DBMS *-- BackupDurabilityManager
    DBMS *-- PerformanceManager
    DBMS *-- AdminMonitorManager

    QueryExecution ..> StorageEngine
    QueryExecution ..> TransactionManager
    StorageEngine ..> LogManager
    RecoveryManager ..> LogManager
    AccessMethods ..> BufferPoolManager
    TransactionManager ..> LogManager
    %% Missing classes defined for strict parsers
    class TupleHeaderManager
    class ResourceManager
    class SlowQueryProfiler
    class PerformanceMetricsCollector
    class ViewManager
    class ConfigurationManagement
    class SharedMemoryAllocator
    class ColumnDefinitionManager
    class DACEvaluator
    class TransactionTable
    class Authorization
    class CheckpointerDaemon
    class UserCatalog
    class TableCreator
    class SystemErrorLogWriter
    class IndexUsageAdvisor
    class BackupManager
    class FileRestorer
    class QueryValidation
    class Caching
    class MemoryPoolManager
    class UniqueConstraintManager
    class DefaultValueManager
    class IndexMetadata
    class CrashRecoveryManager
    class CheckConstraintEvaluator
    class VictimSelectionStrategy
    class RestoreValidator
```



## 🔍 Subsystem Class Diagrams



### 1. Query Processor Subsystem
```mermaid
classDiagram
    class QueryProcessor {
        -SQLParser sqlParser
        -QueryOptimizer queryOptimizer
        -QueryExecution queryExecution
        -QueryValidation queryValidation
    }
    class SQLParser {
        -LexicalAnalyzer lexer
        -SyntaxAnalyzer syntaxAnalyzer
        -ASTBuilder astBuilder
    }
    class LexicalAnalyzer {
        +tokenize(String sql)
    }
    class SyntaxAnalyzer {
        +checkSyntax(TokenList tokens)
    }
    class ASTBuilder {
        +buildTree(TokenList tokens)
    }
    class QueryOptimizer {
        -CostBasedOptimizer cbo
        -RuleBasedOptimizer rbo
    }
    class CostBasedOptimizer {
        +estimateCost(Plan p)
    }
    class RuleBasedOptimizer {
        +applyRules(Plan p)
    }
    class QueryExecution {
        -OperatorScheduler scheduler
        -ExecutionEngine engine
        -ResourceManager resourceManager
    }
    class OperatorScheduler {
        +schedule(Plan p)
    }
    class ExecutionEngine {
        +executeNode(OpNode n)
    }

    QueryProcessor *-- SQLParser
    QueryProcessor *-- QueryOptimizer
    QueryProcessor *-- QueryExecution
    SQLParser *-- LexicalAnalyzer
    SQLParser *-- SyntaxAnalyzer
    SQLParser *-- ASTBuilder
    QueryOptimizer *-- CostBasedOptimizer
    QueryOptimizer *-- RuleBasedOptimizer
    QueryExecution *-- OperatorScheduler
    QueryExecution *-- ExecutionEngine
    %% Missing classes defined for strict parsers
    class QueryValidation
    class ResourceManager
```

### 2. Storage Engine Subsystem
```mermaid
classDiagram
    class StorageEngine {
        -BufferPoolManager bufferPool
        -RecordManager recordManager
        -IndexManager indexManager
        -AccessMethods accessMethods
        -LogManager logManager
    }
    class BufferPoolManager {
        -PageReplacementAlgorithm replacementAlgo
        -BufferFrameManager frameManager
        -DirtyPageWriter dirtyWriter
        +fetchPage(PageID pid)
    }
    class PageReplacementAlgorithm {
        <<interface>>
        +findVictim()
    }
    class BufferFrameManager {
        +allocateFrame()
    }
    class DirtyPageWriter {
        +flushDirtyPages()
    }
    class RecordManager {
        -RecordLayoutManager layoutManager
        -TupleHeaderManager headerManager
        -RIDGenerator ridGenerator
    }
    class RecordLayoutManager {
        +formatRecord(Tuple t)
    }
    class RIDGenerator {
        +generateRID()
    }
    class IndexManager {
        -IndexMetadata metadata
        -BTreeCoreEngine bTreeEngine
    }
    class BTreeCoreEngine {
        +insertNode(Key k, RID r)
    }
    class AccessMethods {
        -SequentialScan seqScan
        -IndexScan idxScan
    }
    class SequentialScan {
        +scan()
    }
    class IndexScan {
        +scan(Key k)
    }
    class LogManager {
        -LSNGenerator lsnGenerator
        -WALBuffer walBuffer
    }
    class LSNGenerator {
        +nextLSN()
    }
    class WALBuffer {
        +appendLog(LogRecord l)
    }

    StorageEngine *-- BufferPoolManager
    StorageEngine *-- RecordManager
    StorageEngine *-- IndexManager
    StorageEngine *-- AccessMethods
    StorageEngine *-- LogManager
    BufferPoolManager *-- PageReplacementAlgorithm
    BufferPoolManager *-- BufferFrameManager
    BufferPoolManager *-- DirtyPageWriter
    RecordManager *-- RecordLayoutManager
    RecordManager *-- RIDGenerator
    IndexManager *-- BTreeCoreEngine
    AccessMethods *-- SequentialScan
    AccessMethods *-- IndexScan
    LogManager *-- LSNGenerator
    LogManager *-- WALBuffer
    %% Missing classes defined for strict parsers
    class IndexMetadata
    class TupleHeaderManager
```

### 3. Transaction Subsystem
```mermaid
classDiagram
    class TransactionManager {
        -TransactionTable txnTable
        -LockManager lockManager
        -IsolationManager isolationManager
        -DeadlockDetector deadlockDetector
    }
    class LockManager {
        -LockTable lockTable
        +acquireLock(TransactionID txnId, ResourceID resId, LockMode mode)
    }
    class LockTable {
        +getLocks(ResourceID r)
    }
    class DeadlockDetector {
        -WaitForGraph waitGraph
        -VictimSelectionStrategy victimStrategy
    }
    class WaitForGraph {
        +addEdge(TransactionID t1, TransactionID t2)
    }
    class IsolationManager {
        -ReadViewGenerator snapshotGen
        -VersionChainBuilder mvccBuilder
    }
    class ReadViewGenerator {
        +createSnapshot(TransactionID t)
    }
    class VersionChainBuilder {
        +linkVersion(Record r1, Record r2)
    }

    TransactionManager *-- LockManager
    TransactionManager *-- DeadlockDetector
    TransactionManager *-- IsolationManager
    LockManager *-- LockTable
    DeadlockDetector *-- WaitForGraph
    IsolationManager *-- ReadViewGenerator
    IsolationManager *-- VersionChainBuilder
    %% Missing classes defined for strict parsers
    class TransactionTable
    class VictimSelectionStrategy
```

### 4. Database Object Management
```mermaid
classDiagram
    class DatabaseObjectManager {
        -SchemaManager schemaManager
        -TableManager tableManager
        -ViewManager viewManager
        -ConstraintManager constraintManager
        -ColumnManager columnManager
    }
    class SchemaManager {
        +createSchema(String name)
    }
    class TableManager {
        -TableCreator tableCreator
        -PhysicalFileRegistration fileRegistry
    }
    class PhysicalFileRegistration {
        +registerFile(String path)
    }
    class ConstraintManager {
        -PrimaryKeyValidator pkValidator
        -UniqueConstraintManager ukManager
        -CheckConstraintEvaluator checkEvaluator
    }
    class PrimaryKeyValidator {
        +validatePK(Record r)
    }
    class ColumnManager {
        -ColumnDefinitionManager colDefMgr
        -DefaultValueManager defValMgr
    }

    DatabaseObjectManager *-- SchemaManager
    DatabaseObjectManager *-- TableManager
    DatabaseObjectManager *-- ConstraintManager
    DatabaseObjectManager *-- ColumnManager
    ConstraintManager *-- PrimaryKeyValidator
    TableManager *-- PhysicalFileRegistration
    %% Missing classes defined for strict parsers
    class UniqueConstraintManager
    class TableCreator
    class CheckConstraintEvaluator
    class ColumnDefinitionManager
    class DefaultValueManager
    class ViewManager
```

### 5. Backup & Durability
```mermaid
classDiagram
    class BackupDurabilityManager {
        -BackupManager backupManager
        -RestoreManager restoreManager
        -RecoveryManager recoveryManager
        -CheckpointManager checkpointMgr
    }
    class RecoveryManager {
        -CrashRecoveryManager crashRecovery
        -REDOLogApplier redoApplier
        -UNDOLogApplier undoApplier
    }
    class REDOLogApplier {
        +apply(LogRecord l)
    }
    class UNDOLogApplier {
        +rollback(LogRecord l)
    }
    class CheckpointManager {
        -CheckpointerDaemon checkpointer
        -FuzzyCheckpointController fuzzyController
    }
    class FuzzyCheckpointController {
        +triggerFuzzy()
    }
    class RestoreManager {
        -RestoreValidator validator
        -FileRestorer fileRestorer
    }
    BackupDurabilityManager *-- RecoveryManager
    BackupDurabilityManager *-- CheckpointManager
    BackupDurabilityManager *-- RestoreManager
    RecoveryManager *-- REDOLogApplier
    RecoveryManager *-- UNDOLogApplier
    CheckpointManager *-- FuzzyCheckpointController
    %% Missing classes defined for strict parsers
    class CheckpointerDaemon
    class BackupManager
    class RestoreValidator
    class FileRestorer
    class CrashRecoveryManager
```

### 6. Security & Access Control
```mermaid
classDiagram
    class SecurityManager {
        -Authentication authModule
        -Authorization authzModule
        -AccessControl accessControl
        -UserManagement userMgmt
    }
    class Authentication {
        +authenticateUser(Credentials creds)
    }
    class AccessControl {
        -RBACPolicyEvaluator rbacEvaluator
        -DACEvaluator dacEvaluator
    }
    class RBACPolicyEvaluator {
        +evaluate(Role r, Action a)
    }
    class UserManagement {
        -UserCatalog userCatalog
        -RoleHierarchyResolver roleResolver
    }
    class RoleHierarchyResolver {
        +resolveRoles(User u)
    }
    SecurityManager *-- Authentication
    SecurityManager *-- AccessControl
    SecurityManager *-- UserManagement
    AccessControl *-- RBACPolicyEvaluator
    UserManagement *-- RoleHierarchyResolver
    %% Missing classes defined for strict parsers
    class UserCatalog
    class Authorization
    class DACEvaluator
```

### 7. Performance and Admin Subsystems
```mermaid
classDiagram
    class PerformanceManager {
        -QueryPerformanceAnalyzer perfAnalyzer
        -MemoryManagement memMgmt
        -Caching cacheMgmt
    }
    class QueryPerformanceAnalyzer {
        -IndexUsageAdvisor indexAdvisor
        -SlowQueryProfiler slowProfiler
    }
    class MemoryManagement {
        -SharedMemoryAllocator sharedAlloc
        -MemoryPoolManager poolMgr
    }
    class AdminMonitorManager {
        -MonitoringLogging monitoring
        -ConfigurationManagement configMgmt
    }
    class MonitoringLogging {
        -PerformanceMetricsCollector metricsCollector
        -SystemErrorLogWriter errorWriter
    }

    PerformanceManager *-- QueryPerformanceAnalyzer
    PerformanceManager *-- MemoryManagement
    AdminMonitorManager *-- MonitoringLogging
    %% Missing classes defined for strict parsers
    class ConfigurationManagement
    class SharedMemoryAllocator
    class MemoryPoolManager
    class PerformanceMetricsCollector
    class SlowQueryProfiler
    class IndexUsageAdvisor
    class SystemErrorLogWriter
    class Caching
```

