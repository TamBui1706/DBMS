# DBMS Architecture Design

This project is a comprehensive, high-level object-oriented design and implementation plan for a modern Database Management System (DBMS).

## 🏗️ System Architecture


## 🧠 Mind Map

Below is the mind map illustrating the layered architecture of the DBMS.

![DBMS Mindmap](./Mindmap.png)

### Mindmap (Text Representation)

```mermaid
flowchart LR
    %% Root Node
    DBMS[Database Management System]

    %% -----------------------------------------
    %% LEFT SIDE BRANCHES (Child --- Parent --- DBMS)
    %% -----------------------------------------

    %% Transaction Branch (Left)
    Concurrency[Concurrency] --- Transaction[Transaction Management]
    Deadlock[Deadlock] --- Transaction
    TxnManager[Transaction Manager] --- Transaction
    LockManager[Lock Manager] --- Transaction
    Isolation[Isolation Management] --- Transaction
    Transaction --- DBMS

    %% Storage Engine Branch (Left)
    DataFile[Data File Manager] --- Storage[Storage Engine]
    BufferPool[Buffer Pool + Cache] --- Storage
    RecordMgmt[Record Management] --- Storage
    StorageIndexMgmt[Index Management] --- Storage
    AccessMethods[Access Methods] --- Storage
    StorageAlloc[Storage Allocation] --- Storage
    LogFile[Log File] --- Storage
    Storage --- DBMS

    %% Backup & Durability Branch (Left)
    BackupMgmt[Backup Management] --- Backup[Backup & Durability]
    RestoreMgmt[Restore Management] --- Backup
    TxnLogging[Transaction Logging] --- Backup
    Recovery[Recovery] --- Backup
    Checkpoint[Checkpoint] --- Backup
    Replication[Replication] --- Backup
    Backup --- DBMS

    %% Administration & Monitoring Branch (Left)
    BackupStrategy[Backup Strategy] --- Admin[Administration & Monitoring]
    Monitoring[Monitoring & Logging] --- Admin
    ConfigMgmt[Configuration Management] --- Admin
    ImportExport[Import and Export] --- Admin
    Admin --- DBMS

    %% -----------------------------------------
    %% RIGHT SIDE BRANCHES (DBMS --- Parent --- Child)
    %% -----------------------------------------

    %% Query Processor Branch (Right)
    DBMS --- QP[Query Processor]
    QP --- Parser[SQL Parser]
    QP --- Optimizer[Query Optimizer]
    QP --- Execution[Query Execution]
    QP --- Validation[Query Validation]
    QP --- Result[Result Processing]

    %% Database Object Management Branch (Right)
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

    %% Performance Branch (Right)
    DBMS --- Perf[Performance]
    Perf --- PerfAnalyzer[Query Performance Analyzer]
    Perf --- Caching[Caching]
    Perf --- MemMgmt[Memory Management]
    Perf --- DataDist[Data Distribution]
    Perf --- ConnThread[Connection & Thread Management]

    %% Security & Access Control Branch (Right)
    DBMS --- Security[Security & Access Control]
    Security --- Auth[Authentication]
    Security --- Authorization[Authorization]
    Security --- AccessCtrl[Access Control]
    Security --- UserMgmt[User Management]
    Security --- Encryption[Encryption]
    Security --- Auditing[Auditing]

    %% -----------------------------------------
    %% STYLING
    %% -----------------------------------------
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
        +startSystem() void
        +stopSystem() void
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
        +tokenize(String sql) List_Token
    }
    class SyntaxAnalyzer {
        +checkSyntax(List_Token tokens) boolean
    }
    class ASTBuilder {
        +buildTree(List_Token tokens) ASTNode
    }
    class QueryOptimizer {
        -CostBasedOptimizer cbo
        -RuleBasedOptimizer rbo
    }
    class CostBasedOptimizer {
        +estimateCost(Plan p) double
    }
    class RuleBasedOptimizer {
        +applyRules(Plan p) Plan
    }
    class QueryExecution {
        -OperatorScheduler scheduler
        -ExecutionEngine engine
        -ResourceManager resourceManager
    }
    class OperatorScheduler {
        +schedule(Plan p) void
    }
    class ExecutionEngine {
        +executeNode(OpNode n) Result
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
        +fetchPage(PageID pid) Page
    }
    class PageReplacementAlgorithm {
        <<interface>>
        +findVictim() PageID
    }
    class BufferFrameManager {
        +allocateFrame() Frame
    }
    class DirtyPageWriter {
        +flushDirtyPages() void
    }
    class RecordManager {
        -RecordLayoutManager layoutManager
        -TupleHeaderManager headerManager
        -RIDGenerator ridGenerator
    }
    class RecordLayoutManager {
        +formatRecord(Tuple t) ByteArray
    }
    class RIDGenerator {
        +generateRID() RID
    }
    class IndexManager {
        -IndexMetadata metadata
        -BTreeCoreEngine bTreeEngine
    }
    class BTreeCoreEngine {
        +insertNode(Key k, RID r) void
    }
    class AccessMethods {
        -SequentialScan seqScan
        -IndexScan idxScan
    }
    class SequentialScan {
        +scan() Iterator
    }
    class IndexScan {
        +scan(Key k) Iterator
    }
    class LogManager {
        -LSNGenerator lsnGenerator
        -WALBuffer walBuffer
    }
    class LSNGenerator {
        +nextLSN() LSN
    }
    class WALBuffer {
        +appendLog(LogRecord l) void
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
        +acquireLock(TransactionID txnId, ResourceID resId, LockMode mode) boolean
    }
    class LockTable {
        +getLocks(ResourceID r) List_Lock
    }
    class DeadlockDetector {
        -WaitForGraph waitGraph
        -VictimSelectionStrategy victimStrategy
    }
    class WaitForGraph {
        +addEdge(TransactionID t1, TransactionID t2) void
    }
    class IsolationManager {
        -ReadViewGenerator snapshotGen
        -VersionChainBuilder mvccBuilder
    }
    class ReadViewGenerator {
        +createSnapshot(TransactionID t) Snapshot
    }
    class VersionChainBuilder {
        +linkVersion(Record r1, Record r2) void
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
        +createSchema(String name) void
    }
    class TableManager {
        -TableCreator tableCreator
        -PhysicalFileRegistration fileRegistry
    }
    class PhysicalFileRegistration {
        +registerFile(String path) void
    }
    class ConstraintManager {
        -PrimaryKeyValidator pkValidator
        -UniqueConstraintManager ukManager
        -CheckConstraintEvaluator checkEvaluator
    }
    class PrimaryKeyValidator {
        +validatePK(Record r) boolean
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
        +apply(LogRecord l) void
    }
    class UNDOLogApplier {
        +rollback(LogRecord l) void
    }
    class CheckpointManager {
        -CheckpointerDaemon checkpointer
        -FuzzyCheckpointController fuzzyController
    }
    class FuzzyCheckpointController {
        +triggerFuzzy() void
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
        +authenticateUser(Credentials creds) SessionToken
    }
    class AccessControl {
        -RBACPolicyEvaluator rbacEvaluator
        -DACEvaluator dacEvaluator
    }
    class RBACPolicyEvaluator {
        +evaluate(Role r, Action a) boolean
    }
    class UserManagement {
        -UserCatalog userCatalog
        -RoleHierarchyResolver roleResolver
    }
    class RoleHierarchyResolver {
        +resolveRoles(User u) List_Role
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
        +tokenize(String sql) List_Token
    }
    class SyntaxAnalyzer {
        +checkSyntax(List_Token tokens) boolean
    }
    class ASTBuilder {
        +buildTree(List_Token tokens) ASTNode
    }
    class QueryOptimizer {
        -CostBasedOptimizer cbo
        -RuleBasedOptimizer rbo
    }
    class CostBasedOptimizer {
        +estimateCost(Plan p) double
    }
    class RuleBasedOptimizer {
        +applyRules(Plan p) Plan
    }
    class QueryExecution {
        -OperatorScheduler scheduler
        -ExecutionEngine engine
        -ResourceManager resourceManager
    }
    class OperatorScheduler {
        +schedule(Plan p) void
    }
    class ExecutionEngine {
        +executeNode(OpNode n) Result
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
        +fetchPage(PageID pid) Page
    }
    class PageReplacementAlgorithm {
        <<interface>>
        +findVictim() PageID
    }
    class BufferFrameManager {
        +allocateFrame() Frame
    }
    class DirtyPageWriter {
        +flushDirtyPages() void
    }
    class RecordManager {
        -RecordLayoutManager layoutManager
        -TupleHeaderManager headerManager
        -RIDGenerator ridGenerator
    }
    class RecordLayoutManager {
        +formatRecord(Tuple t) ByteArray
    }
    class RIDGenerator {
        +generateRID() RID
    }
    class IndexManager {
        -IndexMetadata metadata
        -BTreeCoreEngine bTreeEngine
    }
    class BTreeCoreEngine {
        +insertNode(Key k, RID r) void
    }
    class AccessMethods {
        -SequentialScan seqScan
        -IndexScan idxScan
    }
    class SequentialScan {
        +scan() Iterator
    }
    class IndexScan {
        +scan(Key k) Iterator
    }
    class LogManager {
        -LSNGenerator lsnGenerator
        -WALBuffer walBuffer
    }
    class LSNGenerator {
        +nextLSN() LSN
    }
    class WALBuffer {
        +appendLog(LogRecord l) void
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
        +acquireLock(TransactionID txnId, ResourceID resId, LockMode mode) boolean
    }
    class LockTable {
        +getLocks(ResourceID r) List_Lock
    }
    class DeadlockDetector {
        -WaitForGraph waitGraph
        -VictimSelectionStrategy victimStrategy
    }
    class WaitForGraph {
        +addEdge(TransactionID t1, TransactionID t2) void
    }
    class IsolationManager {
        -ReadViewGenerator snapshotGen
        -VersionChainBuilder mvccBuilder
    }
    class ReadViewGenerator {
        +createSnapshot(TransactionID t) Snapshot
    }
    class VersionChainBuilder {
        +linkVersion(Record r1, Record r2) void
    }

    TransactionManager *-- LockManager
    TransactionManager *-- DeadlockDetector
    TransactionManager *-- IsolationManager
    LockManager *-- LockTable
    DeadlockDetector *-- WaitForGraph
    IsolationManager *-- ReadViewGenerator
    IsolationManager *-- VersionChainBuilder
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
        +createSchema(String name) void
    }
    class TableManager {
        -TableCreator tableCreator
        -PhysicalFileRegistration fileRegistry
    }
    class PhysicalFileRegistration {
        +registerFile(String path) void
    }
    class ConstraintManager {
        -PrimaryKeyValidator pkValidator
        -UniqueConstraintManager ukManager
        -CheckConstraintEvaluator checkEvaluator
    }
    class PrimaryKeyValidator {
        +validatePK(Record r) boolean
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
        +apply(LogRecord l) void
    }
    class UNDOLogApplier {
        +rollback(LogRecord l) void
    }
    class CheckpointManager {
        -CheckpointerDaemon checkpointer
        -FuzzyCheckpointController fuzzyController
    }
    class FuzzyCheckpointController {
        +triggerFuzzy() void
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
        +authenticateUser(Credentials creds) SessionToken
    }
    class AccessControl {
        -RBACPolicyEvaluator rbacEvaluator
        -DACEvaluator dacEvaluator
    }
    class RBACPolicyEvaluator {
        +evaluate(Role r, Action a) boolean
    }
    class UserManagement {
        -UserCatalog userCatalog
        -RoleHierarchyResolver roleResolver
    }
    class RoleHierarchyResolver {
        +resolveRoles(User u) List_Role
    }
    SecurityManager *-- Authentication
    SecurityManager *-- AccessControl
    SecurityManager *-- UserManagement
    AccessControl *-- RBACPolicyEvaluator
    UserManagement *-- RoleHierarchyResolver
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
```

