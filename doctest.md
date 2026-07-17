# Unit Tests for DBMS Core Architecture



---

## 1. Core Server & Connections

### 1. `DatabaseServer`
- `Start_WhenConfigValid_InitializesAllSubsystems`
- `Start_WhenAlreadyRunning_ThrowsIllegalStateException`
- `Stop_WhenRunning_ShutsDownGracefully`
- `Stop_WhenAlreadyStopped_DoesNothing`
- `Status_ReturnsCurrentOperationalState`

### 2. `ConnectionManager`
- `AcceptConnection_WhenUnderMaxLimit_CreatesClientSession`
- `AcceptConnection_WhenAtMaxLimit_RejectsConnection`
- `AcceptConnection_WhenServerPaused_QueuesOrRejects`
- `CloseConnection_WhenValidSession_ReleasesResources`
- `CloseConnection_WhenInvalidSession_ThrowsException`

### 3. `ClientSession`
- `Init_SetsSessionIdAndTimestamp`
- `Execute_WhenValidQuery_ReturnsExecutionResult`
- `Execute_WhenSessionExpired_ThrowsTimeoutException`
- `Execute_WhenConnectionLost_FailsGracefully`

### 4. `DatabaseManager`
- `CreateDatabase_WhenNameIsValid_CreatesMetadataAndFiles`
- `CreateDatabase_WhenNameExists_ThrowsDuplicateDatabaseException`
- `CreateDatabase_WhenInvalidCharacters_ThrowsValidationException`
- `DropDatabase_WhenExists_RemovesAllAssociatedData`
- `DropDatabase_WhenInUse_ThrowsConcurrencyException`

### 5. `Database`
- `Init_SetsDatabaseNameCorrectly`
- `Open_WhenValidMetadata_LoadsDatabaseContext`
- `Open_WhenCorruptedMetadata_ThrowsCorruptionException`

### 6. `CatalogManager`
- `RegisterObject_WhenObjectIsValid_UpdatesCatalogDictionary`
- `RegisterObject_WhenDuplicateId_ThrowsException`
- `FindObject_WhenExists_ReturnsObjectMetadata`
- `FindObject_WhenNotExists_ReturnsNull`

---

## 2. Database Object Management

### 7. `Schema`
- `Init_SetsSchemaName`
- `CreateTable_WhenValidTable_RegistersInSchema`
- `CreateTable_WhenTableNameExists_ThrowsException`
- `DropTable_WhenExists_RemovesFromSchema`

### 8. `Table`
- `Insert_WhenValidRowAndConstraintsMet_AppendsRow`
- `Insert_WhenPrimaryKeyViolated_ThrowsConstraintException`
- `Update_WhenRowExists_ModifiesValues`
- `Update_WhenRowNotExists_ReturnsZeroAffectedRows`
- `Delete_WhenRowExists_RemovesRow`

### 9. `View`
- `Init_SetsQueryDefinition`
- `CompileView_WhenUnderlyingTablesExist_Succeeds`

### 10. `StoredProcedure`
- `Execute_WhenValidParametersProvided_RunsLogic`
- `Execute_WhenTypeMismatchInParams_ThrowsException`

### 11. `Function`
- `Evaluate_WhenValidArguments_ReturnsComputedValue`
- `Evaluate_WhenMissingArguments_ThrowsArgumentException`

### 12. `Sequence`
- `NextValue_IncrementsByStepAndReturnsValue`
- `NextValue_WhenMaxLimitReached_ThrowsOverflowException`

### 13. `Trigger`
- `Fire_OnEventConditionMet_ExecutesTriggerAction`
- `Fire_OnEventConditionNotMet_SkipsExecution`

### 14. `Partition`
- `Init_SetsPartitionKeyCorrectly`
- `CheckBoundary_WhenValueInRange_ReturnsTrue`

### 15. `Column`
- `Init_SetsNameAndNullableFlags`
- `ValidateType_WhenDataMatchesColumnType_Succeeds`

### 16. `Row`
- `Init_GeneratesRowIdAndInitializesValueList`
- `GetValue_WhenIndexValid_ReturnsData`

### 17. `DataType` (Enum)
- `EnumValues_IncludeIntVarcharDateBoolean`
- `ParseString_WhenValidFormat_ReturnsDataTypeInstance`

### 18. `Constraint` (Abstract)
- `Instantiation_OfAbstractClass_FailsWithTypeError`

### 19. `PrimaryKey`
- `Validate_WhenValueIsUniqueAndNotNull_Succeeds`
- `Validate_WhenValueIsNull_ThrowsNullException`
- `Validate_WhenValueIsDuplicate_ThrowsDuplicateKeyException`

### 20. `ForeignKey`
- `Validate_WhenReferencedRowExists_Succeeds`
- `Validate_WhenReferencedRowDoesNotExist_ThrowsForeignKeyException`
- `Init_SetsReferenceTableCorrectly`

### 21. `UniqueConstraint`
- `Validate_WhenValueIsGloballyUnique_Succeeds`
- `Validate_WhenValueExistsInAnotherRow_ThrowsException`

### 22. `CheckConstraint`
- `Validate_WhenExpressionEvaluatesToTrue_Succeeds`
- `Validate_WhenExpressionEvaluatesToFalse_ThrowsCheckException`

### 23. `Index` (Abstract)
- `Instantiation_OfAbstractClass_FailsWithTypeError`

### 24. `BTreeIndex`
- `InsertKey_WhenValid_AddsNodeToTreeBalancing`
- `Search_WhenKeyExists_ReturnsCorrespondingRowID`
- `Search_WhenKeyNotExists_ReturnsEmptyResult`

### 25. `HashIndex`
- `InsertKey_ComputesHashAndAddsToBucket`
- `Search_WhenKeyExists_ResolvesHashToRowID`
- `HandleCollision_CreatesLinkedListInBucket`

### 26. `BitmapIndex`
- `InsertKey_UpdatesBitmapBitsForGivenValue`
- `Search_WhenKeyExists_UsesBitwiseOperationsToFindRID`

---

## 3. Query Processor

### 27. `QueryProcessor`
- `ProcessQuery_WhenValidSQL_ReturnsQueryResult`
- `ProcessQuery_WhenExecutionFails_RollsBackAndThrows`

### 28. `SQLParser`
- `Parse_WhenValidSelectStatement_GeneratesAST`
- `Parse_WhenInvalidSyntax_ThrowsSyntaxErrorException`
- `Parse_WhenUnsupportedCommand_ThrowsNotImplementedException`

### 29. `Lexer`
- `Tokenize_WhenValidString_ReturnsListOfTokens`
- `Tokenize_IgnoresWhitespaceAndComments`

### 30. `AST`
- `Init_SetsRootNode`
- `Traverse_VisitsAllNodesInCorrectOrder`

### 31. `QueryOptimizer`
- `Optimize_WhenGivenLogicalPlan_TransformsToPhysicalPlan`
- `Optimize_AppliesFilterPushdownRule`

### 32. `CostModel`
- `EstimateCost_CalculatesIOAndCPUCost`
- `EstimateCost_WhenUsingIndex_ReturnsLowerCostThanSeqScan`

### 33. `StatisticsManager`
- `Collect_UpdatesRowCountsAndCardinality`
- `GetStatistics_WhenCalled_ReturnsAccurateMetadata`

### 34. `LogicalPlan`
- `Init_CreatesEmptyOperatorTree`
- `AddOperator_AppendsToPlan`

### 35. `LogicalOperator` (Abstract)
- `Instantiation_OfAbstractClass_FailsWithTypeError`

### 36. `PhysicalPlan`
- `Init_CreatesEmptyOperatorTree`
- `ValidatePipeline_EnsuresOperatorCompatibility`

### 37. `PhysicalOperator` (Abstract)
- `Instantiation_OfAbstractClass_FailsWithTypeError`

### 38. `QueryExecutor`
- `ExecutePlan_WhenValidPhysicalPlan_IteratesAndYieldsResults`
- `ExecutePlan_WhenMemoryExceeded_SpillsToDiskOrThrows`

---

## 4. Transaction Management

### 39. `TransactionManager`
- `BeginTransaction_CreatesAndRegistersNewActiveTransaction`
- `Commit_WhenSuccessful_WritesToLogAndChangesState`
- `Rollback_WhenCalled_RevertsAllModifications`
- `Commit_WhenValidationFails_ForcesRollback`

### 40. `Transaction`
- `Init_GeneratesUniqueTransactionId`
- `SetIsolationLevel_UpdatesTransactionProperties`

### 41. `IsolationLevel` (Enum)
- `EnumValues_IncludeReadCommittedAndSerializable`

### 42. `TransactionState` (Enum)
- `EnumValues_IncludeActiveCommittedAborted`

### 43. `LockManager`
- `AcquireLock_WhenResourceFree_GrantsLockInstantly`
- `AcquireLock_WhenResourceLocked_BlocksOrThrowsTimeout`
- `ReleaseLock_WhenHoldingLock_FreesResourceAndWakesWaiters`

### 44. `LockTable`
- `GetLocks_ReturnsCurrentLockInformation`
- `AddLock_RegistersNewLockForResource`

### 45. `DeadlockDetector`
- `DetectAndResolve_WhenCycleFound_AbortsVictimTransaction`
- `DetectAndResolve_WhenNoCycleFound_DoesNothing`

### 46. `MVCCManager`
- `CreateVersion_AppendsNewRecordVersionToChain`
- `GarbageCollect_RemovesVersionsInvisibleToAllActiveTransactions`

---

## 5. Storage Engine

### 47. `StorageEngine`
- `ReadPage_WhenPageNotInBuffer_LoadsFromDisk`
- `WritePage_WhenPageIsDirty_FlushesToDisk`

### 48. `BufferPool`
- `PinPage_IncrementsPinCountAndPreventsEviction`
- `UnpinPage_DecrementsPinCount`
- `FlushPage_ForcesDirtyPageToDisk`
- `FetchPage_WhenPoolFull_EvictsUnpinnedPage`

### 49. `PageReplacementAlgorithm` (Interface)
- `Instantiation_OfInterface_FailsWithTypeError`
- `FindVictim_Implementation_ReturnsUnpinnedPageId`

### 50. `Page`
- `Init_SetsPageIdAndClearsDirtyFlag`
- `MarkDirty_SetsDirtyFlagToTrue`

### 51. `FileManager`
- `AllocateSpace_CreatesNewBlockAndReturnsId`
- `DeallocateSpace_MarksBlockAsFree`

### 52. `DataFile`
- `Init_OpensFileStreamForDataBlocks`
- `ReadBlock_LoadsBytesFromDisk`

### 53. `IndexFile`
- `Init_OpensFileStreamForIndexBlocks`
- `WriteBlock_SavesBytesToDisk`

---

## 6. Backup & Durability

### 54. `RecoveryManager`
- `Recover_WhenSystemCrashes_ReplaysWALToRestoreState`
- `Recover_WhenUndoNeeded_RollsBackUncommittedTransactions`

### 55. `CheckpointManager`
- `TakeCheckpoint_FlushesAllDirtyPages`
- `TakeCheckpoint_WritesCheckpointRecordToLog`

### 56. `WALManager`
- `AppendLog_AddsRecordToMemoryBuffer`
- `Flush_WritesBufferToDiskSynchronously`
- `AppendLog_WhenBufferFull_TriggersAutomaticFlush`

### 57. `LogRecord`
- `Init_SetsLsnTypeAndPayloadData`
- `Serialize_ConvertsRecordToByteArray`

---

## 7. Security & Access Control

### 58. `SecurityManager`
- `Authenticate_WhenValidCredentials_ReturnsSessionToken`
- `Authenticate_WhenInvalidCredentials_ThrowsAuthException`
- `Authorize_WhenUserHasRequiredRole_Succeeds`
- `Authorize_WhenUserLacksPermission_ThrowsAccessException`

### 59. `User`
- `Init_SetsUsernameAndHashedPassword`
- `AddRole_AssignsNewRoleToUser`

### 60. `Role`
- `Init_SetsRoleName`
- `AddPermission_GrantsPermissionToRole`

### 61. `Permission`
- `Init_SetsResourceAndActionType`
- `Matches_WhenActionAndResourceAlign_ReturnsTrue`

