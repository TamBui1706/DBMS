# DBMS Architecture Design

This project is a comprehensive, high-level object-oriented design and implementation plan for a modern Database Management System (DBMS).

## 🏗️ System Architecture


## 🧠 Mind Map

Below is the mind map illustrating the layered architecture of the DBMS.

![DBMS Mindmap](./Mindmap.png)

### Mindmap (Text)

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

:

```mermaid
classDiagram
direction LR

%% 1. Core Server & Connections
class DatabaseServer {
    +serverId : UUID
    +status : String
    +start()
    +stop()
}
class ConnectionManager {
    +acceptConnection()
    +closeConnection()
}
class ClientSession {
    +sessionId : UUID
    +connectTime : Date
    +execute()
}

%% 2. Database & Schema
class DatabaseManager {
    +createDatabase()
    +dropDatabase()
}
class Database {
    +name : String
    +open()
}
class Schema {
    +name : String
    +createTable()
}
class CatalogManager {
    +registerObject()
    +findObject()
}

%% 3. Objects
class Table {
    +name : String
    +insert()
    +update()
    +delete()
}
class View {
    +queryDefinition : String
}
class StoredProcedure {
    +execute()
}
class Function {
    +evaluate()
}
class Sequence {
    +nextValue()
}
class Trigger {
    +fire()
}
class Partition {
    +partitionKey : String
}

%% 4. Table Internals
class Column {
    +name : String
    +nullable : Boolean
}
class Row {
    +rowId : UUID
    +values : List
}
class DataType {
    <<enumeration>>
    INT, VARCHAR, DATE, BOOLEAN
}

%% 5. Constraints
class Constraint {
    <<abstract>>
    +validate()
}
class PrimaryKey
class ForeignKey {
    +referenceTable : String
}
class UniqueConstraint
class CheckConstraint

%% 6. Indexes
class Index {
    <<abstract>>
    +search()
    +insertKey()
}
class BTreeIndex
class HashIndex
class BitmapIndex

%% 7. Query Processing
class QueryProcessor {
    +processQuery()
}
class SQLParser {
    +parse()
}
class Lexer {
    +tokenize()
}
class AST {
    +rootNode
}
class QueryOptimizer {
    +optimize()
}
class CostModel {
    +estimateCost()
}
class StatisticsManager {
    +collect()
}
class LogicalPlan
class LogicalOperator {
    <<abstract>>
}
class PhysicalPlan
class PhysicalOperator {
    <<abstract>>
}
class QueryExecutor {
    +executePlan()
}

%% 8. Transactions
class TransactionManager {
    +beginTransaction()
    +commit()
    +rollback()
}
class Transaction {
    +transactionId : UUID
}
class IsolationLevel {
    <<enumeration>>
    READ_COMMITTED, SERIALIZABLE
}
class TransactionState {
    <<enumeration>>
    ACTIVE, COMMITTED, ABORTED
}
class LockManager {
    +acquireLock()
    +releaseLock()
}
class LockTable {
    +getLocks()
}
class DeadlockDetector {
    +detectAndResolve()
}
class MVCCManager {
    +createVersion()
    +garbageCollect()
}

%% 9. Storage & Buffer
class StorageEngine {
    +readPage()
    +writePage()
}
class BufferPool {
    +pinPage()
    +flushPage()
}
class PageReplacementAlgorithm {
    <<interface>>
    +findVictim()
}
class Page {
    +pageId : Int
    +isDirty : Boolean
}
class FileManager {
    +allocateSpace()
}
class DataFile
class IndexFile

%% 10. Recovery & Logging
class RecoveryManager {
    +recover()
}
class CheckpointManager {
    +takeCheckpoint()
}
class WALManager {
    +appendLog()
    +flush()
}
class LogRecord {
    +lsn : Int
    +type : String
}

%% 11. Security
class SecurityManager {
    +authenticate()
    +authorize()
}
class User {
    +username : String
}
class Role
class Permission

%% --- RELATIONSHIPS ---

DatabaseServer --> ConnectionManager
DatabaseServer --> DatabaseManager
DatabaseServer --> QueryProcessor
DatabaseServer --> TransactionManager
DatabaseServer --> StorageEngine
DatabaseServer --> SecurityManager
DatabaseServer --> CatalogManager
DatabaseServer --> RecoveryManager

ConnectionManager --> ClientSession

DatabaseManager --> Database
Database --> Schema
Schema --> Table
Schema --> View
Schema --> StoredProcedure
Schema --> Function
Schema --> Sequence

Table --> Column
Table --> Row
Table --> Index
Table --> Constraint
Table --> Partition
Table --> Trigger

Column --> DataType

Constraint <|-- PrimaryKey
Constraint <|-- ForeignKey
Constraint <|-- UniqueConstraint
Constraint <|-- CheckConstraint

Index <|-- BTreeIndex
Index <|-- HashIndex
Index <|-- BitmapIndex

ForeignKey --> Table

QueryProcessor --> SQLParser
QueryProcessor --> QueryOptimizer
QueryProcessor --> QueryExecutor

SQLParser --> Lexer
SQLParser --> AST
AST --> LogicalPlan
LogicalPlan --> LogicalOperator

QueryOptimizer --> LogicalPlan
QueryOptimizer --> CostModel
QueryOptimizer --> StatisticsManager
QueryOptimizer --> PhysicalPlan
PhysicalPlan --> PhysicalOperator

QueryExecutor --> PhysicalPlan
QueryExecutor --> TransactionManager

TransactionManager --> Transaction
TransactionManager --> LockManager
TransactionManager --> MVCCManager
TransactionManager --> WALManager

Transaction --> IsolationLevel
Transaction --> TransactionState

LockManager --> LockTable
LockManager --> DeadlockDetector

StorageEngine --> BufferPool
StorageEngine --> FileManager
BufferPool --> Page
BufferPool --> PageReplacementAlgorithm
FileManager --> DataFile
FileManager --> IndexFile

RecoveryManager --> WALManager
RecoveryManager --> CheckpointManager

WALManager --> LogRecord

CatalogManager --> Schema
CatalogManager --> StatisticsManager

SecurityManager --> User
SecurityManager --> Role
Role --> Permission
```



## 🔍 Subsystem Class Diagrams



### 1. Query Processor Subsystem
```mermaid
classDiagram
    class QueryProcessor {
        +processQuery()
    }
    class SQLParser {
        +parse()
    }
    class Lexer {
        +tokenize()
    }
    class AST {
        +rootNode
    }
    class QueryOptimizer {
        +optimize()
    }
    class CostModel {
        +estimateCost()
    }
    class StatisticsManager {
        +collect()
    }
    class LogicalPlan
    class LogicalOperator {
        <<abstract>>
    }
    class PhysicalPlan
    class PhysicalOperator {
        <<abstract>>
    }
    class QueryExecutor {
        +executePlan()
    }

    QueryProcessor *-- SQLParser
    QueryProcessor *-- QueryOptimizer
    QueryProcessor *-- QueryExecutor
    SQLParser *-- Lexer
    SQLParser *-- AST
    AST *-- LogicalPlan
    LogicalPlan *-- LogicalOperator
    QueryOptimizer *-- CostModel
    QueryOptimizer *-- StatisticsManager
    QueryOptimizer ..> PhysicalPlan : generates
    PhysicalPlan *-- PhysicalOperator
    QueryExecutor ..> PhysicalPlan : executes
```

### 2. Storage Engine Subsystem
```mermaid
classDiagram
    class StorageEngine {
        +readPage()
        +writePage()
    }
    class BufferPool {
        +pinPage()
        +flushPage()
    }
    class PageReplacementAlgorithm {
        <<interface>>
        +findVictim()
    }
    class Page {
        +pageId : Int
        +isDirty : Boolean
    }
    class FileManager {
        +allocateSpace()
    }
    class DataFile
    class IndexFile

    StorageEngine *-- BufferPool
    StorageEngine *-- FileManager
    BufferPool *-- PageReplacementAlgorithm
    BufferPool *-- Page
    FileManager *-- DataFile
    FileManager *-- IndexFile
```

### 3. Transaction Subsystem
```mermaid
classDiagram
    class TransactionManager {
        +beginTransaction()
        +commit()
        +rollback()
    }
    class Transaction {
        +transactionId : UUID
    }
    class IsolationLevel {
        <<enumeration>>
        READ_COMMITTED, SERIALIZABLE
    }
    class TransactionState {
        <<enumeration>>
        ACTIVE, COMMITTED, ABORTED
    }
    class LockManager {
        +acquireLock()
        +releaseLock()
    }
    class LockTable {
        +getLocks()
    }
    class DeadlockDetector {
        +detectAndResolve()
    }
    class MVCCManager {
        +createVersion()
        +garbageCollect()
    }

    TransactionManager *-- Transaction
    TransactionManager *-- LockManager
    TransactionManager *-- MVCCManager
    Transaction *-- IsolationLevel
    Transaction *-- TransactionState
    LockManager *-- LockTable
    LockManager *-- DeadlockDetector
```

### 4. Database Object Management
```mermaid
classDiagram
    class CatalogManager {
        +registerObject()
        +findObject()
    }
    class DatabaseManager {
        +createDatabase()
        +dropDatabase()
    }
    class Database {
        +name : String
        +open()
    }
    class Schema {
        +name : String
        +createTable()
    }
    class Table {
        +name : String
        +insert()
        +update()
        +delete()
    }
    class Column {
        +name : String
        +nullable : Boolean
    }
    class Row {
        +rowId : UUID
        +values : List
    }
    class DataType {
        <<enumeration>>
    }
    class Constraint {
        <<abstract>>
    }
    class PrimaryKey
    class ForeignKey {
        +referenceTable : String
    }
    class UniqueConstraint
    class CheckConstraint
    class Index {
        <<abstract>>
    }
    class BTreeIndex
    class HashIndex
    class BitmapIndex
    class View
    class StoredProcedure
    class Function
    class Sequence
    class Trigger
    class Partition

    DatabaseManager *-- Database
    Database *-- Schema
    Schema *-- Table
    Schema *-- View
    Schema *-- StoredProcedure
    Schema *-- Function
    Schema *-- Sequence
    Table *-- Column
    Table *-- Row
    Table *-- Index
    Table *-- Constraint
    Table *-- Partition
    Table *-- Trigger
    Column *-- DataType
    Constraint <|-- PrimaryKey
    Constraint <|-- ForeignKey
    Constraint <|-- UniqueConstraint
    Constraint <|-- CheckConstraint
    Index <|-- BTreeIndex
    Index <|-- HashIndex
    Index <|-- BitmapIndex
    ForeignKey --> Table
    CatalogManager ..> Schema : manages
```

### 5. Backup & Durability
```mermaid
classDiagram
    class RecoveryManager {
        +recover()
    }
    class CheckpointManager {
        +takeCheckpoint()
    }
    class WALManager {
        +appendLog()
        +flush()
    }
    class LogRecord {
        +lsn : Int
        +type : String
    }
    
    RecoveryManager *-- CheckpointManager
    RecoveryManager *-- WALManager
    WALManager *-- LogRecord
```

### 6. Security & Access Control
```mermaid
classDiagram
    class SecurityManager {
        +authenticate()
        +authorize()
    }
    class User {
        +username : String
    }
    class Role
    class Permission

    SecurityManager *-- User
    SecurityManager *-- Role
    Role *-- Permission
```

### 7. Core Server & Connections
```mermaid
classDiagram
    class DatabaseServer {
        +serverId : UUID
        +status : String
        +start()
        +stop()
    }
    class ConnectionManager {
        +acceptConnection()
        +closeConnection()
    }
    class ClientSession {
        +sessionId : UUID
        +connectTime : Date
        +execute()
    }
    
    DatabaseServer *-- ConnectionManager
    ConnectionManager *-- ClientSession
```



## 🧪 Unit Test 

### Core Server & Connections Unit Tests

```mermaid
graph LR
    S0["Core Server & Connections"]
    S0 --> C0_0["DatabaseServer"]
    C0_0 --> T0_0_0["Start_WhenConfigValid_InitializesAllSubsystems"]
    C0_0 --> T0_0_1["Start_WhenAlreadyRunning_ThrowsIllegalStateException"]
    C0_0 --> T0_0_2["Stop_WhenRunning_ShutsDownGracefully"]
    C0_0 --> T0_0_3["Stop_WhenAlreadyStopped_DoesNothing"]
    C0_0 --> T0_0_4["Status_ReturnsCurrentOperationalState"]
    S0 --> C0_1["ConnectionManager"]
    C0_1 --> T0_1_0["AcceptConnection_WhenUnderMaxLimit_CreatesClientSession"]
    C0_1 --> T0_1_1["AcceptConnection_WhenAtMaxLimit_RejectsConnection"]
    C0_1 --> T0_1_2["AcceptConnection_WhenServerPaused_QueuesOrRejects"]
    C0_1 --> T0_1_3["CloseConnection_WhenValidSession_ReleasesResources"]
    C0_1 --> T0_1_4["CloseConnection_WhenInvalidSession_ThrowsException"]
    S0 --> C0_2["ClientSession"]
    C0_2 --> T0_2_0["Init_SetsSessionIdAndTimestamp"]
    C0_2 --> T0_2_1["Execute_WhenValidQuery_ReturnsExecutionResult"]
    C0_2 --> T0_2_2["Execute_WhenSessionExpired_ThrowsTimeoutException"]
    C0_2 --> T0_2_3["Execute_WhenConnectionLost_FailsGracefully"]
    S0 --> C0_3["DatabaseManager"]
    C0_3 --> T0_3_0["CreateDatabase_WhenNameIsValid_CreatesMetadataAndFiles"]
    C0_3 --> T0_3_1["CreateDatabase_WhenNameExists_ThrowsDuplicateDatabaseException"]
    C0_3 --> T0_3_2["CreateDatabase_WhenInvalidCharacters_ThrowsValidationException"]
    C0_3 --> T0_3_3["DropDatabase_WhenExists_RemovesAllAssociatedData"]
    C0_3 --> T0_3_4["DropDatabase_WhenInUse_ThrowsConcurrencyException"]
    S0 --> C0_4["Database"]
    C0_4 --> T0_4_0["Init_SetsDatabaseNameCorrectly"]
    C0_4 --> T0_4_1["Open_WhenValidMetadata_LoadsDatabaseContext"]
    C0_4 --> T0_4_2["Open_WhenCorruptedMetadata_ThrowsCorruptionException"]
    S0 --> C0_5["CatalogManager"]
    C0_5 --> T0_5_0["RegisterObject_WhenObjectIsValid_UpdatesCatalogDictionary"]
    C0_5 --> T0_5_1["RegisterObject_WhenDuplicateId_ThrowsException"]
    C0_5 --> T0_5_2["FindObject_WhenExists_ReturnsObjectMetadata"]
    C0_5 --> T0_5_3["FindObject_WhenNotExists_ReturnsNull"]
```

### Database Object Management Unit Tests

```mermaid
graph LR
    S1["Database Object Management"]
    S1 --> C1_0["Schema"]
    C1_0 --> T1_0_0["Init_SetsSchemaName"]
    C1_0 --> T1_0_1["CreateTable_WhenValidTable_RegistersInSchema"]
    C1_0 --> T1_0_2["CreateTable_WhenTableNameExists_ThrowsException"]
    C1_0 --> T1_0_3["DropTable_WhenExists_RemovesFromSchema"]
    S1 --> C1_1["Table"]
    C1_1 --> T1_1_0["Insert_WhenValidRowAndConstraintsMet_AppendsRow"]
    C1_1 --> T1_1_1["Insert_WhenPrimaryKeyViolated_ThrowsConstraintException"]
    C1_1 --> T1_1_2["Update_WhenRowExists_ModifiesValues"]
    C1_1 --> T1_1_3["Update_WhenRowNotExists_ReturnsZeroAffectedRows"]
    C1_1 --> T1_1_4["Delete_WhenRowExists_RemovesRow"]
    S1 --> C1_2["View"]
    C1_2 --> T1_2_0["Init_SetsQueryDefinition"]
    C1_2 --> T1_2_1["CompileView_WhenUnderlyingTablesExist_Succeeds"]
    S1 --> C1_3["StoredProcedure"]
    C1_3 --> T1_3_0["Execute_WhenValidParametersProvided_RunsLogic"]
    C1_3 --> T1_3_1["Execute_WhenTypeMismatchInParams_ThrowsException"]
    S1 --> C1_4["Function"]
    C1_4 --> T1_4_0["Evaluate_WhenValidArguments_ReturnsComputedValue"]
    C1_4 --> T1_4_1["Evaluate_WhenMissingArguments_ThrowsArgumentException"]
    S1 --> C1_5["Sequence"]
    C1_5 --> T1_5_0["NextValue_IncrementsByStepAndReturnsValue"]
    C1_5 --> T1_5_1["NextValue_WhenMaxLimitReached_ThrowsOverflowException"]
    S1 --> C1_6["Trigger"]
    C1_6 --> T1_6_0["Fire_OnEventConditionMet_ExecutesTriggerAction"]
    C1_6 --> T1_6_1["Fire_OnEventConditionNotMet_SkipsExecution"]
    S1 --> C1_7["Partition"]
    C1_7 --> T1_7_0["Init_SetsPartitionKeyCorrectly"]
    C1_7 --> T1_7_1["CheckBoundary_WhenValueInRange_ReturnsTrue"]
    S1 --> C1_8["Column"]
    C1_8 --> T1_8_0["Init_SetsNameAndNullableFlags"]
    C1_8 --> T1_8_1["ValidateType_WhenDataMatchesColumnType_Succeeds"]
    S1 --> C1_9["Row"]
    C1_9 --> T1_9_0["Init_GeneratesRowIdAndInitializesValueList"]
    C1_9 --> T1_9_1["GetValue_WhenIndexValid_ReturnsData"]
    S1 --> C1_10["DataType"]
    C1_10 --> T1_10_0["EnumValues_IncludeIntVarcharDateBoolean"]
    C1_10 --> T1_10_1["ParseString_WhenValidFormat_ReturnsDataTypeInstance"]
    S1 --> C1_11["Constraint"]
    C1_11 --> T1_11_0["Instantiation_OfAbstractClass_FailsWithTypeError"]
    S1 --> C1_12["PrimaryKey"]
    C1_12 --> T1_12_0["Validate_WhenValueIsUniqueAndNotNull_Succeeds"]
    C1_12 --> T1_12_1["Validate_WhenValueIsNull_ThrowsNullException"]
    C1_12 --> T1_12_2["Validate_WhenValueIsDuplicate_ThrowsDuplicateKeyException"]
    S1 --> C1_13["ForeignKey"]
    C1_13 --> T1_13_0["Validate_WhenReferencedRowExists_Succeeds"]
    C1_13 --> T1_13_1["Validate_WhenReferencedRowDoesNotExist_ThrowsForeignKeyException"]
    C1_13 --> T1_13_2["Init_SetsReferenceTableCorrectly"]
    S1 --> C1_14["UniqueConstraint"]
    C1_14 --> T1_14_0["Validate_WhenValueIsGloballyUnique_Succeeds"]
    C1_14 --> T1_14_1["Validate_WhenValueExistsInAnotherRow_ThrowsException"]
    S1 --> C1_15["CheckConstraint"]
    C1_15 --> T1_15_0["Validate_WhenExpressionEvaluatesToTrue_Succeeds"]
    C1_15 --> T1_15_1["Validate_WhenExpressionEvaluatesToFalse_ThrowsCheckException"]
    S1 --> C1_16["Index"]
    C1_16 --> T1_16_0["Instantiation_OfAbstractClass_FailsWithTypeError"]
    S1 --> C1_17["BTreeIndex"]
    C1_17 --> T1_17_0["InsertKey_WhenValid_AddsNodeToTreeBalancing"]
    C1_17 --> T1_17_1["Search_WhenKeyExists_ReturnsCorrespondingRowID"]
    C1_17 --> T1_17_2["Search_WhenKeyNotExists_ReturnsEmptyResult"]
    S1 --> C1_18["HashIndex"]
    C1_18 --> T1_18_0["InsertKey_ComputesHashAndAddsToBucket"]
    C1_18 --> T1_18_1["Search_WhenKeyExists_ResolvesHashToRowID"]
    C1_18 --> T1_18_2["HandleCollision_CreatesLinkedListInBucket"]
    S1 --> C1_19["BitmapIndex"]
    C1_19 --> T1_19_0["InsertKey_UpdatesBitmapBitsForGivenValue"]
    C1_19 --> T1_19_1["Search_WhenKeyExists_UsesBitwiseOperationsToFindRID"]
```

### Query Processor Unit Tests

```mermaid
graph LR
    S2["Query Processor"]
    S2 --> C2_0["QueryProcessor"]
    C2_0 --> T2_0_0["ProcessQuery_WhenValidSQL_ReturnsQueryResult"]
    C2_0 --> T2_0_1["ProcessQuery_WhenExecutionFails_RollsBackAndThrows"]
    S2 --> C2_1["SQLParser"]
    C2_1 --> T2_1_0["Parse_WhenValidSelectStatement_GeneratesAST"]
    C2_1 --> T2_1_1["Parse_WhenInvalidSyntax_ThrowsSyntaxErrorException"]
    C2_1 --> T2_1_2["Parse_WhenUnsupportedCommand_ThrowsNotImplementedException"]
    S2 --> C2_2["Lexer"]
    C2_2 --> T2_2_0["Tokenize_WhenValidString_ReturnsListOfTokens"]
    C2_2 --> T2_2_1["Tokenize_IgnoresWhitespaceAndComments"]
    S2 --> C2_3["AST"]
    C2_3 --> T2_3_0["Init_SetsRootNode"]
    C2_3 --> T2_3_1["Traverse_VisitsAllNodesInCorrectOrder"]
    S2 --> C2_4["QueryOptimizer"]
    C2_4 --> T2_4_0["Optimize_WhenGivenLogicalPlan_TransformsToPhysicalPlan"]
    C2_4 --> T2_4_1["Optimize_AppliesFilterPushdownRule"]
    S2 --> C2_5["CostModel"]
    C2_5 --> T2_5_0["EstimateCost_CalculatesIOAndCPUCost"]
    C2_5 --> T2_5_1["EstimateCost_WhenUsingIndex_ReturnsLowerCostThanSeqScan"]
    S2 --> C2_6["StatisticsManager"]
    C2_6 --> T2_6_0["Collect_UpdatesRowCountsAndCardinality"]
    C2_6 --> T2_6_1["GetStatistics_WhenCalled_ReturnsAccurateMetadata"]
    S2 --> C2_7["LogicalPlan"]
    C2_7 --> T2_7_0["Init_CreatesEmptyOperatorTree"]
    C2_7 --> T2_7_1["AddOperator_AppendsToPlan"]
    S2 --> C2_8["LogicalOperator"]
    C2_8 --> T2_8_0["Instantiation_OfAbstractClass_FailsWithTypeError"]
    S2 --> C2_9["PhysicalPlan"]
    C2_9 --> T2_9_0["Init_CreatesEmptyOperatorTree"]
    C2_9 --> T2_9_1["ValidatePipeline_EnsuresOperatorCompatibility"]
    S2 --> C2_10["PhysicalOperator"]
    C2_10 --> T2_10_0["Instantiation_OfAbstractClass_FailsWithTypeError"]
    S2 --> C2_11["QueryExecutor"]
    C2_11 --> T2_11_0["ExecutePlan_WhenValidPhysicalPlan_IteratesAndYieldsResults"]
    C2_11 --> T2_11_1["ExecutePlan_WhenMemoryExceeded_SpillsToDiskOrThrows"]
```

### Transaction Management Unit Tests

```mermaid
graph LR
    S3["Transaction Management"]
    S3 --> C3_0["TransactionManager"]
    C3_0 --> T3_0_0["BeginTransaction_CreatesAndRegistersNewActiveTransaction"]
    C3_0 --> T3_0_1["Commit_WhenSuccessful_WritesToLogAndChangesState"]
    C3_0 --> T3_0_2["Rollback_WhenCalled_RevertsAllModifications"]
    C3_0 --> T3_0_3["Commit_WhenValidationFails_ForcesRollback"]
    S3 --> C3_1["Transaction"]
    C3_1 --> T3_1_0["Init_GeneratesUniqueTransactionId"]
    C3_1 --> T3_1_1["SetIsolationLevel_UpdatesTransactionProperties"]
    S3 --> C3_2["IsolationLevel"]
    C3_2 --> T3_2_0["EnumValues_IncludeReadCommittedAndSerializable"]
    S3 --> C3_3["TransactionState"]
    C3_3 --> T3_3_0["EnumValues_IncludeActiveCommittedAborted"]
    S3 --> C3_4["LockManager"]
    C3_4 --> T3_4_0["AcquireLock_WhenResourceFree_GrantsLockInstantly"]
    C3_4 --> T3_4_1["AcquireLock_WhenResourceLocked_BlocksOrThrowsTimeout"]
    C3_4 --> T3_4_2["ReleaseLock_WhenHoldingLock_FreesResourceAndWakesWaiters"]
    S3 --> C3_5["LockTable"]
    C3_5 --> T3_5_0["GetLocks_ReturnsCurrentLockInformation"]
    C3_5 --> T3_5_1["AddLock_RegistersNewLockForResource"]
    S3 --> C3_6["DeadlockDetector"]
    C3_6 --> T3_6_0["DetectAndResolve_WhenCycleFound_AbortsVictimTransaction"]
    C3_6 --> T3_6_1["DetectAndResolve_WhenNoCycleFound_DoesNothing"]
    S3 --> C3_7["MVCCManager"]
    C3_7 --> T3_7_0["CreateVersion_AppendsNewRecordVersionToChain"]
    C3_7 --> T3_7_1["GarbageCollect_RemovesVersionsInvisibleToAllActiveTransactions"]
```

### Storage Engine Unit Tests

```mermaid
graph LR
    S4["Storage Engine"]
    S4 --> C4_0["StorageEngine"]
    C4_0 --> T4_0_0["ReadPage_WhenPageNotInBuffer_LoadsFromDisk"]
    C4_0 --> T4_0_1["WritePage_WhenPageIsDirty_FlushesToDisk"]
    S4 --> C4_1["BufferPool"]
    C4_1 --> T4_1_0["PinPage_IncrementsPinCountAndPreventsEviction"]
    C4_1 --> T4_1_1["UnpinPage_DecrementsPinCount"]
    C4_1 --> T4_1_2["FlushPage_ForcesDirtyPageToDisk"]
    C4_1 --> T4_1_3["FetchPage_WhenPoolFull_EvictsUnpinnedPage"]
    S4 --> C4_2["PageReplacementAlgorithm"]
    C4_2 --> T4_2_0["Instantiation_OfInterface_FailsWithTypeError"]
    C4_2 --> T4_2_1["FindVictim_Implementation_ReturnsUnpinnedPageId"]
    S4 --> C4_3["Page"]
    C4_3 --> T4_3_0["Init_SetsPageIdAndClearsDirtyFlag"]
    C4_3 --> T4_3_1["MarkDirty_SetsDirtyFlagToTrue"]
    S4 --> C4_4["FileManager"]
    C4_4 --> T4_4_0["AllocateSpace_CreatesNewBlockAndReturnsId"]
    C4_4 --> T4_4_1["DeallocateSpace_MarksBlockAsFree"]
    S4 --> C4_5["DataFile"]
    C4_5 --> T4_5_0["Init_OpensFileStreamForDataBlocks"]
    C4_5 --> T4_5_1["ReadBlock_LoadsBytesFromDisk"]
    S4 --> C4_6["IndexFile"]
    C4_6 --> T4_6_0["Init_OpensFileStreamForIndexBlocks"]
    C4_6 --> T4_6_1["WriteBlock_SavesBytesToDisk"]
```

### Backup & Durability Unit Tests

```mermaid
graph LR
    S5["Backup & Durability"]
    S5 --> C5_0["RecoveryManager"]
    C5_0 --> T5_0_0["Recover_WhenSystemCrashes_ReplaysWALToRestoreState"]
    C5_0 --> T5_0_1["Recover_WhenUndoNeeded_RollsBackUncommittedTransactions"]
    S5 --> C5_1["CheckpointManager"]
    C5_1 --> T5_1_0["TakeCheckpoint_FlushesAllDirtyPages"]
    C5_1 --> T5_1_1["TakeCheckpoint_WritesCheckpointRecordToLog"]
    S5 --> C5_2["WALManager"]
    C5_2 --> T5_2_0["AppendLog_AddsRecordToMemoryBuffer"]
    C5_2 --> T5_2_1["Flush_WritesBufferToDiskSynchronously"]
    C5_2 --> T5_2_2["AppendLog_WhenBufferFull_TriggersAutomaticFlush"]
    S5 --> C5_3["LogRecord"]
    C5_3 --> T5_3_0["Init_SetsLsnTypeAndPayloadData"]
    C5_3 --> T5_3_1["Serialize_ConvertsRecordToByteArray"]
```

### Security & Access Control Unit Tests

```mermaid
graph LR
    S6["Security & Access Control"]
    S6 --> C6_0["SecurityManager"]
    C6_0 --> T6_0_0["Authenticate_WhenValidCredentials_ReturnsSessionToken"]
    C6_0 --> T6_0_1["Authenticate_WhenInvalidCredentials_ThrowsAuthException"]
    C6_0 --> T6_0_2["Authorize_WhenUserHasRequiredRole_Succeeds"]
    C6_0 --> T6_0_3["Authorize_WhenUserLacksPermission_ThrowsAccessException"]
    S6 --> C6_1["User"]
    C6_1 --> T6_1_0["Init_SetsUsernameAndHashedPassword"]
    C6_1 --> T6_1_1["AddRole_AssignsNewRoleToUser"]
    S6 --> C6_2["Role"]
    C6_2 --> T6_2_0["Init_SetsRoleName"]
    C6_2 --> T6_2_1["AddPermission_GrantsPermissionToRole"]
    S6 --> C6_3["Permission"]
    C6_3 --> T6_3_0["Init_SetsResourceAndActionType"]
    C6_3 --> T6_3_1["Matches_WhenActionAndResourceAlign_ReturnsTrue"]
```
