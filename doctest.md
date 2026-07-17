# 🧪 Unit Tests Architecture

## 1. Core Architecture Unit Tests

```mermaid
mindmap
  root_1["Core Architecture"]
    cls_1_1["DBMS"]
      t_1_1_1["Init_WhenCalled_ShouldInitializeDBMS"]
      t_1_1_2["StartSystem_WhenValid_ShouldSucceed"]
      t_1_1_3["StartSystem_WhenInvalid_ShouldThrow"]
      t_1_1_4["StopSystem_WhenValid_ShouldSucceed"]
      t_1_1_5["StopSystem_WhenInvalid_ShouldThrow"]
```

## 2. Query Processor Subsystem Unit Tests

```mermaid
mindmap
  root_2["Query Processor Subsystem"]
    cls_2_1["QueryProcessor"]
      t_2_1_1["Init_WhenCalled_ShouldInitializeQueryProcessor"]
    cls_2_2["SQLParser"]
      t_2_2_1["Init_WhenCalled_ShouldInitializeSQLParser"]
    cls_2_3["LexicalAnalyzer"]
      t_2_3_1["Init_WhenCalled_ShouldInitializeLexicalAnalyzer"]
      t_2_3_2["Tokenize_WhenValid_ShouldSucceed"]
      t_2_3_3["Tokenize_WhenInvalid_ShouldThrow"]
    cls_2_4["SyntaxAnalyzer"]
      t_2_4_1["Init_WhenCalled_ShouldInitializeSyntaxAnalyzer"]
      t_2_4_2["CheckSyntax_WhenValid_ShouldSucceed"]
      t_2_4_3["CheckSyntax_WhenInvalid_ShouldThrow"]
    cls_2_5["ASTBuilder"]
      t_2_5_1["Init_WhenCalled_ShouldInitializeASTBuilder"]
      t_2_5_2["BuildTree_WhenValid_ShouldSucceed"]
      t_2_5_3["BuildTree_WhenInvalid_ShouldThrow"]
    cls_2_6["QueryOptimizer"]
      t_2_6_1["Init_WhenCalled_ShouldInitializeQueryOptimizer"]
    cls_2_7["CostBasedOptimizer"]
      t_2_7_1["Init_WhenCalled_ShouldInitializeCostBasedOptimizer"]
      t_2_7_2["EstimateCost_WhenValid_ShouldSucceed"]
      t_2_7_3["EstimateCost_WhenInvalid_ShouldThrow"]
    cls_2_8["RuleBasedOptimizer"]
      t_2_8_1["Init_WhenCalled_ShouldInitializeRuleBasedOptimizer"]
      t_2_8_2["ApplyRules_WhenValid_ShouldSucceed"]
      t_2_8_3["ApplyRules_WhenInvalid_ShouldThrow"]
    cls_2_9["QueryExecution"]
      t_2_9_1["Init_WhenCalled_ShouldInitializeQueryExecution"]
    cls_2_10["OperatorScheduler"]
      t_2_10_1["Init_WhenCalled_ShouldInitializeOperatorScheduler"]
      t_2_10_2["Schedule_WhenValid_ShouldSucceed"]
      t_2_10_3["Schedule_WhenInvalid_ShouldThrow"]
    cls_2_11["ExecutionEngine"]
      t_2_11_1["Init_WhenCalled_ShouldInitializeExecutionEngine"]
      t_2_11_2["ExecuteNode_WhenValid_ShouldSucceed"]
      t_2_11_3["ExecuteNode_WhenInvalid_ShouldThrow"]
```

## 3. Storage Engine Subsystem Unit Tests

```mermaid
mindmap
  root_3["Storage Engine Subsystem"]
    cls_3_1["StorageEngine"]
      t_3_1_1["Init_WhenCalled_ShouldInitializeStorageEngine"]
    cls_3_2["BufferPoolManager"]
      t_3_2_1["Init_WhenCalled_ShouldInitializeBufferPoolManager"]
      t_3_2_2["FetchPage_WhenValid_ShouldSucceed"]
      t_3_2_3["FetchPage_WhenInvalid_ShouldThrow"]
    cls_3_3["PageReplacementAlgorithm"]
      t_3_3_1["Init_WhenCalled_ShouldInitializePageReplacementAlgorithm"]
      t_3_3_2["FindVictim_WhenValid_ShouldSucceed"]
      t_3_3_3["FindVictim_WhenInvalid_ShouldThrow"]
    cls_3_4["BufferFrameManager"]
      t_3_4_1["Init_WhenCalled_ShouldInitializeBufferFrameManager"]
      t_3_4_2["AllocateFrame_WhenValid_ShouldSucceed"]
      t_3_4_3["AllocateFrame_WhenInvalid_ShouldThrow"]
    cls_3_5["DirtyPageWriter"]
      t_3_5_1["Init_WhenCalled_ShouldInitializeDirtyPageWriter"]
      t_3_5_2["FlushDirtyPages_WhenValid_ShouldSucceed"]
      t_3_5_3["FlushDirtyPages_WhenInvalid_ShouldThrow"]
    cls_3_6["RecordManager"]
      t_3_6_1["Init_WhenCalled_ShouldInitializeRecordManager"]
    cls_3_7["RecordLayoutManager"]
      t_3_7_1["Init_WhenCalled_ShouldInitializeRecordLayoutManager"]
      t_3_7_2["FormatRecord_WhenValid_ShouldSucceed"]
      t_3_7_3["FormatRecord_WhenInvalid_ShouldThrow"]
    cls_3_8["RIDGenerator"]
      t_3_8_1["Init_WhenCalled_ShouldInitializeRIDGenerator"]
      t_3_8_2["GenerateRID_WhenValid_ShouldSucceed"]
      t_3_8_3["GenerateRID_WhenInvalid_ShouldThrow"]
    cls_3_9["IndexManager"]
      t_3_9_1["Init_WhenCalled_ShouldInitializeIndexManager"]
    cls_3_10["BTreeCoreEngine"]
      t_3_10_1["Init_WhenCalled_ShouldInitializeBTreeCoreEngine"]
      t_3_10_2["InsertNode_WhenValid_ShouldSucceed"]
      t_3_10_3["InsertNode_WhenInvalid_ShouldThrow"]
    cls_3_11["AccessMethods"]
      t_3_11_1["Init_WhenCalled_ShouldInitializeAccessMethods"]
    cls_3_12["SequentialScan"]
      t_3_12_1["Init_WhenCalled_ShouldInitializeSequentialScan"]
      t_3_12_2["Scan_WhenValid_ShouldSucceed"]
      t_3_12_3["Scan_WhenInvalid_ShouldThrow"]
    cls_3_13["IndexScan"]
      t_3_13_1["Init_WhenCalled_ShouldInitializeIndexScan"]
      t_3_13_2["Scan_WhenValid_ShouldSucceed"]
      t_3_13_3["Scan_WhenInvalid_ShouldThrow"]
    cls_3_14["LogManager"]
      t_3_14_1["Init_WhenCalled_ShouldInitializeLogManager"]
    cls_3_15["LSNGenerator"]
      t_3_15_1["Init_WhenCalled_ShouldInitializeLSNGenerator"]
      t_3_15_2["NextLSN_WhenValid_ShouldSucceed"]
      t_3_15_3["NextLSN_WhenInvalid_ShouldThrow"]
    cls_3_16["WALBuffer"]
      t_3_16_1["Init_WhenCalled_ShouldInitializeWALBuffer"]
      t_3_16_2["AppendLog_WhenValid_ShouldSucceed"]
      t_3_16_3["AppendLog_WhenInvalid_ShouldThrow"]
```

## 4. Transaction Subsystem Unit Tests

```mermaid
mindmap
  root_4["Transaction Subsystem"]
    cls_4_1["TransactionManager"]
      t_4_1_1["Init_WhenCalled_ShouldInitializeTransactionManager"]
    cls_4_2["LockManager"]
      t_4_2_1["Init_WhenCalled_ShouldInitializeLockManager"]
      t_4_2_2["AcquireLock_WhenValid_ShouldSucceed"]
      t_4_2_3["AcquireLock_WhenInvalid_ShouldThrow"]
    cls_4_3["LockTable"]
      t_4_3_1["Init_WhenCalled_ShouldInitializeLockTable"]
      t_4_3_2["GetLocks_WhenValid_ShouldSucceed"]
      t_4_3_3["GetLocks_WhenInvalid_ShouldThrow"]
    cls_4_4["DeadlockDetector"]
      t_4_4_1["Init_WhenCalled_ShouldInitializeDeadlockDetector"]
    cls_4_5["WaitForGraph"]
      t_4_5_1["Init_WhenCalled_ShouldInitializeWaitForGraph"]
      t_4_5_2["AddEdge_WhenValid_ShouldSucceed"]
      t_4_5_3["AddEdge_WhenInvalid_ShouldThrow"]
    cls_4_6["IsolationManager"]
      t_4_6_1["Init_WhenCalled_ShouldInitializeIsolationManager"]
    cls_4_7["ReadViewGenerator"]
      t_4_7_1["Init_WhenCalled_ShouldInitializeReadViewGenerator"]
      t_4_7_2["CreateSnapshot_WhenValid_ShouldSucceed"]
      t_4_7_3["CreateSnapshot_WhenInvalid_ShouldThrow"]
    cls_4_8["VersionChainBuilder"]
      t_4_8_1["Init_WhenCalled_ShouldInitializeVersionChainBuilder"]
      t_4_8_2["LinkVersion_WhenValid_ShouldSucceed"]
      t_4_8_3["LinkVersion_WhenInvalid_ShouldThrow"]
```

## 5. Database Object Management Unit Tests

```mermaid
mindmap
  root_5["Database Object Management"]
    cls_5_1["DatabaseObjectManager"]
      t_5_1_1["Init_WhenCalled_ShouldInitializeDatabaseObjectManager"]
    cls_5_2["SchemaManager"]
      t_5_2_1["Init_WhenCalled_ShouldInitializeSchemaManager"]
      t_5_2_2["CreateSchema_WhenValid_ShouldSucceed"]
      t_5_2_3["CreateSchema_WhenInvalid_ShouldThrow"]
    cls_5_3["TableManager"]
      t_5_3_1["Init_WhenCalled_ShouldInitializeTableManager"]
    cls_5_4["PhysicalFileRegistration"]
      t_5_4_1["Init_WhenCalled_ShouldInitializePhysicalFileRegistration"]
      t_5_4_2["RegisterFile_WhenValid_ShouldSucceed"]
      t_5_4_3["RegisterFile_WhenInvalid_ShouldThrow"]
    cls_5_5["ConstraintManager"]
      t_5_5_1["Init_WhenCalled_ShouldInitializeConstraintManager"]
    cls_5_6["PrimaryKeyValidator"]
      t_5_6_1["Init_WhenCalled_ShouldInitializePrimaryKeyValidator"]
      t_5_6_2["ValidatePK_WhenValid_ShouldSucceed"]
      t_5_6_3["ValidatePK_WhenInvalid_ShouldThrow"]
    cls_5_7["ColumnManager"]
      t_5_7_1["Init_WhenCalled_ShouldInitializeColumnManager"]
```

## 6. Backup & Durability Unit Tests

```mermaid
mindmap
  root_6["Backup & Durability"]
    cls_6_1["BackupDurabilityManager"]
      t_6_1_1["Init_WhenCalled_ShouldInitializeBackupDurabilityManager"]
    cls_6_2["RecoveryManager"]
      t_6_2_1["Init_WhenCalled_ShouldInitializeRecoveryManager"]
    cls_6_3["REDOLogApplier"]
      t_6_3_1["Init_WhenCalled_ShouldInitializeREDOLogApplier"]
      t_6_3_2["Apply_WhenValid_ShouldSucceed"]
      t_6_3_3["Apply_WhenInvalid_ShouldThrow"]
    cls_6_4["UNDOLogApplier"]
      t_6_4_1["Init_WhenCalled_ShouldInitializeUNDOLogApplier"]
      t_6_4_2["Rollback_WhenValid_ShouldSucceed"]
      t_6_4_3["Rollback_WhenInvalid_ShouldThrow"]
    cls_6_5["CheckpointManager"]
      t_6_5_1["Init_WhenCalled_ShouldInitializeCheckpointManager"]
    cls_6_6["FuzzyCheckpointController"]
      t_6_6_1["Init_WhenCalled_ShouldInitializeFuzzyCheckpointController"]
      t_6_6_2["TriggerFuzzy_WhenValid_ShouldSucceed"]
      t_6_6_3["TriggerFuzzy_WhenInvalid_ShouldThrow"]
    cls_6_7["RestoreManager"]
      t_6_7_1["Init_WhenCalled_ShouldInitializeRestoreManager"]
```

## 7. Security & Access Control Unit Tests

```mermaid
mindmap
  root_7["Security & Access Control"]
    cls_7_1["SecurityManager"]
      t_7_1_1["Init_WhenCalled_ShouldInitializeSecurityManager"]
    cls_7_2["Authentication"]
      t_7_2_1["Init_WhenCalled_ShouldInitializeAuthentication"]
      t_7_2_2["AuthenticateUser_WhenValid_ShouldSucceed"]
      t_7_2_3["AuthenticateUser_WhenInvalid_ShouldThrow"]
    cls_7_3["AccessControl"]
      t_7_3_1["Init_WhenCalled_ShouldInitializeAccessControl"]
    cls_7_4["RBACPolicyEvaluator"]
      t_7_4_1["Init_WhenCalled_ShouldInitializeRBACPolicyEvaluator"]
      t_7_4_2["Evaluate_WhenValid_ShouldSucceed"]
      t_7_4_3["Evaluate_WhenInvalid_ShouldThrow"]
    cls_7_5["UserManagement"]
      t_7_5_1["Init_WhenCalled_ShouldInitializeUserManagement"]
    cls_7_6["RoleHierarchyResolver"]
      t_7_6_1["Init_WhenCalled_ShouldInitializeRoleHierarchyResolver"]
      t_7_6_2["ResolveRoles_WhenValid_ShouldSucceed"]
      t_7_6_3["ResolveRoles_WhenInvalid_ShouldThrow"]
```

## 8. Performance and Admin Subsystems Unit Tests

```mermaid
mindmap
  root_8["Performance and Admin Subsystems"]
    cls_8_1["PerformanceManager"]
      t_8_1_1["Init_WhenCalled_ShouldInitializePerformanceManager"]
    cls_8_2["QueryPerformanceAnalyzer"]
      t_8_2_1["Init_WhenCalled_ShouldInitializeQueryPerformanceAnalyzer"]
    cls_8_3["MemoryManagement"]
      t_8_3_1["Init_WhenCalled_ShouldInitializeMemoryManagement"]
    cls_8_4["AdminMonitorManager"]
      t_8_4_1["Init_WhenCalled_ShouldInitializeAdminMonitorManager"]
    cls_8_5["MonitoringLogging"]
      t_8_5_1["Init_WhenCalled_ShouldInitializeMonitoringLogging"]
```

