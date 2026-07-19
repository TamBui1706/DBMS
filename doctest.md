# Unit Tests for Database Management System (DBMS)

Below is a comprehensive and expanded list of Unit Tests (including positive, negative, boundary, and concurrency tests) for the 61 classes in the architectural diagram.

## 1. Core Server & Connections

### 1. `DatabaseServer`
- `Start_WhenConfigValid_InitializesAllSubsystems`
- `Start_WhenAlreadyRunning_ThrowsIllegalStateException`
- `Stop_WhenRunning_ShutsDownGracefully`
- `Stop_WhenAlreadyStopped_DoesNothing`
- `Status_ReturnsCurrentOperationalState`
- `Start_WhenPortAlreadyInUse_ThrowsBindException`
- `Stop_WhenActiveTransactionsExist_WaitsForCompletionOrTimeout`
- `Restart_GracefullyStopsAndStartsSystem`
- `Init_WithMissingConfigFilePath_ThrowsConfigurationException`
- `HealthCheck_ReturnsTrueIfAllSubsystemsAreRunning`

### 2. `ConnectionManager`
- `AcceptConnection_WhenUnderMaxLimit_CreatesClientSession`
- `AcceptConnection_WhenAtMaxLimit_RejectsConnection`
- `AcceptConnection_WhenServerPaused_QueuesOrRejects`
- `CloseConnection_WhenValidSession_ReleasesResources`
- `CloseConnection_WhenInvalidSession_ThrowsException`
- `GetActiveSessions_ReturnsSnapshotOfConnectedClients`
- `BroadcastMessage_SendsToAllActiveSessions`
- `KillSession_ForcefullyTerminatesConnection`
- `Cleanup_RemovesIdleConnectionsAutomatically`
- `AcceptConnection_WhenClientBlacklisted_RejectsImmediately`

### 3. `ClientSession`
- `Init_SetsSessionIdAndTimestamp`
- `Execute_WhenValidQuery_ReturnsExecutionResult`
- `Execute_WhenSessionExpired_ThrowsTimeoutException`
- `Execute_WhenConnectionLost_FailsGracefully`
- `SetSessionVariable_UpdatesInternalState`
- `GetSessionVariable_ReturnsSetValue`
- `Execute_WhenEmptyQuery_ReturnsEmptyResult`
- `GetSessionVariable_WhenKeyNotExists_ReturnsNull`
- `Ping_ResetsIdleTimer`

### 4. `DatabaseManager`
- `CreateDatabase_WhenNameIsValid_CreatesMetadataAndFiles`
- `CreateDatabase_WhenNameExists_ThrowsDuplicateDatabaseException`
- `CreateDatabase_WhenInvalidCharacters_ThrowsValidationException`
- `DropDatabase_WhenExists_RemovesAllAssociatedData`
- `DropDatabase_WhenInUse_ThrowsConcurrencyException`
- `GetDatabase_WhenExists_ReturnsDatabaseInstance`
- `GetDatabase_WhenNotExists_ThrowsDatabaseNotFoundException`
- `ListDatabases_ReturnsAllRegisteredDatabases`
- `RenameDatabase_WhenNewNameValid_UpdatesMetadata`
- `CreateDatabase_WhenDiskFull_ThrowsInsufficientStorageException`
- `CreateDatabase_WhenNameTooLong_ThrowsValidationException`
- `DropDatabase_WhenPermissionDenied_ThrowsSecurityException`

### 5. `Database`
- `Init_SetsDatabaseNameCorrectly`
- `Open_WhenValidMetadata_LoadsDatabaseContext`
- `Open_WhenCorruptedMetadata_ThrowsCorruptionException`
- `Close_FlushesUnsavedChangesAndReleasesLocks`
- `GetSchema_WhenSchemaExists_ReturnsSchema`
- `CreateSchema_WhenNameValid_AddsToDatabase`
- `Close_WhenAlreadyClosed_DoesNothing`
- `Open_WhenMissingDataFiles_ThrowsFileNotFoundException`

### 6. `CatalogManager`
- `RegisterObject_WhenObjectIsValid_UpdatesCatalogDictionary`
- `RegisterObject_WhenDuplicateId_ThrowsException`
- `FindObject_WhenExists_ReturnsObjectMetadata`
- `FindObject_WhenNotExists_ReturnsNull`
- `RemoveObject_WhenExists_DeletesFromCatalog`
- `RemoveObject_WhenNotExists_ThrowsNotFoundException`
- `UpdateObject_WhenExists_RefreshesMetadata`
- `FlushCatalog_WritesToStorageSuccessfully`
- `LoadCatalog_PopulatesMemoryFromDisk`
- `LoadCatalog_WhenCorruptFile_TriggersRecoveryMode`

---

## 2. Database Object Management

### 7. `Schema`
- `Init_SetsSchemaName`
- `CreateTable_WhenValidTable_RegistersInSchema`
- `CreateTable_WhenTableNameExists_ThrowsException`
- `DropTable_WhenExists_RemovesFromSchema`
- `DropTable_WhenNotExists_ThrowsException`
- `GetTable_WhenExists_ReturnsTable`
- `ListTables_ReturnsAllRegisteredTables`
- `Validate_EnsuresSchemaNameIsAlphanumeric`

### 8. `Table`
- `Insert_WhenValidRowAndConstraintsMet_AppendsRow`
- `Insert_WhenPrimaryKeyViolated_ThrowsConstraintException`
- `Update_WhenRowExists_ModifiesValues`
- `Update_WhenRowNotExists_ReturnsZeroAffectedRows`
- `Delete_WhenRowExists_RemovesRow`
- `Insert_WhenForeignKeyViolated_ThrowsException`
- `Insert_WhenCheckConstraintViolated_ThrowsException`
- `Truncate_RemovesAllRowsRapidly`
- `AddColumn_AppendsColumnDefinitionToSchema`
- `DropColumn_RemovesColumnAndData`
- `GetRowCount_ReturnsAccurateCount`
- `RenameColumn_WhenExists_UpdatesMetadataAndViews`

### 9. `View`
- `Init_SetsQueryDefinition`
- `CompileView_WhenUnderlyingTablesExist_Succeeds`
- `CompileView_WhenTableDropped_ThrowsInvalidViewException`
- `Materialize_CachesResultSetToDisk`
- `Refresh_UpdatesMaterializedData`
- `CompileView_WhenCircularDependencyDetected_ThrowsException`

### 10. `StoredProcedure`
- `Execute_WhenValidParametersProvided_RunsLogic`
- `Execute_WhenTypeMismatchInParams_ThrowsException`
- `Execute_WhenMissingParameters_ThrowsArgumentException`
- `Compile_ValidatesSyntaxAndDependencies`
- `Drop_RemovesProcedureFromCatalog`
- `Execute_WhenProcedureTimesOut_KillsExecution`

### 11. `Function`
- `Evaluate_WhenValidArguments_ReturnsComputedValue`
- `Evaluate_WhenMissingArguments_ThrowsArgumentException`
- `Evaluate_WhenDivideByZero_ThrowsArithmeticException`
- `IsDeterministic_ReturnsTrueIfNoExternalStateUsed`
- `Evaluate_WhenNullPassedToStrictFunction_ReturnsNull`

### 12. `Sequence`
- `NextValue_IncrementsByStepAndReturnsValue`
- `NextValue_WhenMaxLimitReached_ThrowsOverflowException`
- `Reset_SetsValueBackToStart`
- `Init_SetsStartStepAndMaxLimit`
- `CurrentValue_ReturnsCurrentWithoutIncrementing`
- `NextValue_WhenStepIsNegative_DecrementsCorrectly`

### 13. `Trigger`
- `Fire_OnEventConditionMet_ExecutesTriggerAction`
- `Fire_OnEventConditionNotMet_SkipsExecution`
- `Fire_WhenActionFails_RollsBackTransaction`
- `Enable_ActivatesTrigger`
- `Disable_DeactivatesTrigger`
- `Validate_EnsuresNoInfiniteTriggerLoops`

### 14. `Partition`
- `Init_SetsPartitionKeyCorrectly`
- `CheckBoundary_WhenValueInRange_ReturnsTrue`
- `CheckBoundary_WhenValueOutOfRange_ReturnsFalse`
- `Merge_CombinesTwoAdjacentPartitions`
- `Split_DividesPartitionAtGivenValue`

### 15. `Column`
- `Init_SetsNameAndNullableFlags`
- `ValidateType_WhenDataMatchesColumnType_Succeeds`
- `ValidateType_WhenDataIsStringForIntColumn_ThrowsTypeException`
- `ValidateNullable_WhenNullPassedToNotNullColumn_ThrowsException`
- `SetDefaultValue_StoresDefaultExpression`
- `ChangeType_WhenCompatible_Succeeds`
- `ChangeType_WhenIncompatible_ThrowsException`

### 16. `Row`
- `Init_GeneratesRowIdAndInitializesValueList`
- `GetValue_WhenIndexValid_ReturnsData`
- `GetValue_WhenIndexOutOfBounds_ThrowsIndexException`
- `SetValue_UpdatesDataAtIndex`
- `Serialize_ConvertsToByteArray`
- `Deserialize_ReadsFromByteArray`
- `GetSize_ReturnsByteSizeOfAllValues`

### 17. `DataType`
- `EnumValues_IncludeIntVarcharDateBoolean`
- `ParseString_WhenValidFormat_ReturnsDataTypeInstance`
- `ParseString_WhenInvalidFormat_ThrowsParseException`
- `GetSize_ReturnsByteSizeForFixedTypes`
- `IsVariableLength_ReturnsTrueForVarchar`

### 18. `Constraint`
- `Instantiation_OfAbstractClass_FailsWithTypeError`

### 19. `PrimaryKey`
- `Validate_WhenValueIsUniqueAndNotNull_Succeeds`
- `Validate_WhenValueIsNull_ThrowsNullException`
- `Validate_WhenValueIsDuplicate_ThrowsDuplicateKeyException`
- `Validate_WithCompositeKey_ChecksAllColumns`
- `Drop_RemovesIndexFromStorage`

### 20. `ForeignKey`
- `Validate_WhenReferencedRowExists_Succeeds`
- `Validate_WhenReferencedRowDoesNotExist_ThrowsForeignKeyException`
- `Init_SetsReferenceTableCorrectly`
- `OnDeleteCascade_RemovesChildRowsWhenParentDeleted`
- `OnDeleteRestrict_ThrowsExceptionWhenParentDeleted`
- `OnUpdateCascade_ModifiesChildRowsWhenParentKeyChanges`

### 21. `UniqueConstraint`
- `Validate_WhenValueIsGloballyUnique_Succeeds`
- `Validate_WhenValueExistsInAnotherRow_ThrowsException`
- `Validate_WhenValueIsNull_SucceedsIfNullable`

### 22. `CheckConstraint`
- `Validate_WhenExpressionEvaluatesToTrue_Succeeds`
- `Validate_WhenExpressionEvaluatesToFalse_ThrowsCheckException`
- `Validate_WhenExpressionUsesInvalidColumn_ThrowsException`

### 23. `Index`
- `Instantiation_OfAbstractClass_FailsWithTypeError`

### 24. `BTreeIndex`
- `InsertKey_WhenValid_AddsNodeToTreeBalancing`
- `Search_WhenKeyExists_ReturnsCorrespondingRowID`
- `Search_WhenKeyNotExists_ReturnsEmptyResult`
- `DeleteKey_WhenExists_RemovesNodeAndRebalances`
- `RangeSearch_ReturnsAllRowIDsInRange`
- `BulkLoad_BuildsTreeEfficientlyFromSortedData`
- `SplitNode_WhenFull_CreatesSibling`
- `MergeNodes_WhenUnderfull_CombinesSiblings`

### 25. `HashIndex`
- `InsertKey_ComputesHashAndAddsToBucket`
- `Search_WhenKeyExists_ResolvesHashToRowID`
- `HandleCollision_CreatesLinkedListInBucket`
- `Resize_ExpandsHashTableWhenLoadFactorExceeded`
- `DeleteKey_RemovesFromBucketLinkedList`
- `ComputeHash_DistributesKeysEvenly`

### 26. `BitmapIndex`
- `InsertKey_UpdatesBitmapBitsForGivenValue`
- `Search_WhenKeyExists_UsesBitwiseOperationsToFindRID`
- `BitwiseAND_CombinesTwoBitmapsForComplexQuery`
- `BitwiseOR_CombinesTwoBitmapsForOrQuery`
- `Compress_ReducesMemoryFootprintOfSparseBitmap`
- `DeleteKey_ClearsBitForDeletedRow`

---

## 3. Query Processor

### 27. `QueryProcessor`
- `ProcessQuery_WhenValidSQL_ReturnsQueryResult`
- `ProcessQuery_WhenExecutionFails_RollsBackAndThrows`
- `ProcessQuery_WhenTimeoutReached_AbortsQuery`
- `Explain_ReturnsQueryExecutionPlanWithoutRunning`
- `PrepareStatement_CachesCompiledPlanForReuse`

### 28. `SQLParser`
- `Parse_WhenValidSelectStatement_GeneratesAST`
- `Parse_WhenInvalidSyntax_ThrowsSyntaxErrorException`
- `Parse_WhenUnsupportedCommand_ThrowsNotImplementedException`
- `Parse_WhenMissingSemicolon_SucceedsOrThrowsBasedOnDialect`
- `Parse_ComplexJoinAndGroupBy_ConstructsCorrectTree`
- `Parse_NestedSubqueries_HandlesDepthLimits`
- `Parse_WhenMalformedDateLiteral_ThrowsException`

### 29. `Lexer`
- `Tokenize_WhenValidString_ReturnsListOfTokens`
- `Tokenize_IgnoresWhitespaceAndComments`
- `Tokenize_WhenUnclosedStringLiteral_ThrowsLexerException`
- `Tokenize_IdentifiesOperatorsAndPunctuationCorrectly`
- `Tokenize_HandlesEscapedCharactersInStrings`

### 30. `AST`
- `Init_SetsRootNode`
- `Traverse_VisitsAllNodesInCorrectOrder`
- `ToSQL_ReconstructsSQLStringFromTree`
- `Clone_CreatesDeepCopyOfTree`
- `CountNodes_ReturnsTotalSizeOfTree`

### 31. `QueryOptimizer`
- `Optimize_WhenGivenLogicalPlan_TransformsToPhysicalPlan`
- `Optimize_AppliesFilterPushdownRule`
- `Optimize_AppliesJoinReorderingForEfficiency`
- `Optimize_ChoosesIndexScanOverSeqScanWhenSelective`
- `Optimize_EliminatesDeadCodeOrAlwaysFalseConditions`
- `Optimize_FlattensUnnecessarySubqueries`
- `Optimize_WhenStatsMissing_DefaultsToHeuristicRules`

### 32. `CostModel`
- `EstimateCost_CalculatesIOAndCPUCost`
- `EstimateCost_WhenUsingIndex_ReturnsLowerCostThanSeqScan`
- `EstimateCost_ForNestedLoopJoin_IsHigherThanHashJoinForLargeTables`
- `UpdateStatistics_AdjustsInternalWeightsBasedOnFeedback`
- `EstimateMemoryUsage_ForSortOperator_ReturnsExpectedBytes`

### 33. `StatisticsManager`
- `Collect_UpdatesRowCountsAndCardinality`
- `GetStatistics_WhenCalled_ReturnsAccurateMetadata`
- `EstimateSelectivity_ReturnsPercentageOfRowsMatchingFilter`
- `BuildHistogram_ForSkewedDataDistribution`
- `InvalidateStats_WhenTableModifiedSignificantly`

### 34. `LogicalPlan`
- `Init_CreatesEmptyOperatorTree`
- `AddOperator_AppendsToPlan`
- `Validate_EnsuresReferencesExistInCatalog`
- `PrintTree_OutputsFormattedStringForDebugging`
- `GetLeaves_ReturnsBaseTableScans`

### 35. `LogicalOperator`
- `Instantiation_OfAbstractClass_FailsWithTypeError`

### 36. `PhysicalPlan`
- `Init_CreatesEmptyOperatorTree`
- `ValidatePipeline_EnsuresOperatorCompatibility`
- `EstimateTotalCost_SumsCostOfAllOperators`
- `GetRoot_ReturnsTopOperator`
- `Clone_CreatesIsolatedExecutionInstance`

### 37. `PhysicalOperator`
- `Instantiation_OfAbstractClass_FailsWithTypeError`

### 38. `QueryExecutor`
- `ExecutePlan_WhenValidPhysicalPlan_IteratesAndYieldsResults`
- `ExecutePlan_WhenMemoryExceeded_SpillsToDiskOrThrows`
- `ExecutePlan_WhenCanceledByUser_AbortsImmediately`
- `StreamResults_YieldsBatchesInsteadOfLoadingAllIntoMemory`
- `Initialize_AllocatesRequiredTempSpace`
- `Close_ReleasesAllInternalIterators`

---

## 4. Transaction Management

### 39. `TransactionManager`
- `BeginTransaction_CreatesAndRegistersNewActiveTransaction`
- `Commit_WhenSuccessful_WritesToLogAndChangesState`
- `Rollback_WhenCalled_RevertsAllModifications`
- `Commit_WhenValidationFails_ForcesRollback`
- `GetActiveTransactions_ReturnsListOfCurrentlyRunningTx`
- `SuspendTransaction_TemporarilyHaltsExecution`
- `ResumeTransaction_ContinuesSuspendedExecution`
- `ForceRollbackAll_UsedDuringServerShutdown`

### 40. `Transaction`
- `Init_GeneratesUniqueTransactionId`
- `SetIsolationLevel_UpdatesTransactionProperties`
- `AddLock_TracksLocksHeldByThisTransaction`
- `ReleaseAllLocks_CalledDuringCommitOrRollback`
- `SetSavepoint_CreatesPartialRollbackMarker`
- `RollbackToSavepoint_RevertsChangesAfterMarker`

### 41. `IsolationLevel`
- `EnumValues_IncludeReadCommittedAndSerializable`

### 42. `TransactionState`
- `EnumValues_IncludeActiveCommittedAborted`

### 43. `LockManager`
- `AcquireLock_WhenResourceFree_GrantsLockInstantly`
- `AcquireLock_WhenResourceLocked_BlocksOrThrowsTimeout`
- `ReleaseLock_WhenHoldingLock_FreesResourceAndWakesWaiters`
- `AcquireLock_WhenSharedLockExists_GrantsAnotherSharedLock`
- `AcquireLock_WhenSharedLockExists_BlocksExclusiveLock`
- `UpgradeLock_ConvertsSharedToExclusiveIfPossible`
- `DowngradeLock_ConvertsExclusiveToShared`
- `ReleaseLock_WhenNotHoldingLock_ThrowsException`

### 44. `LockTable`
- `GetLocks_ReturnsCurrentLockInformation`
- `AddLock_RegistersNewLockForResource`
- `RemoveLock_DeletesRegistration`
- `Clear_RemovesAllLocksDuringSystemReset`
- `CountLocks_ForSpecificTransactionId`

### 45. `DeadlockDetector`
- `DetectAndResolve_WhenCycleFound_AbortsVictimTransaction`
- `DetectAndResolve_WhenNoCycleFound_DoesNothing`
- `BuildWaitForGraph_CorrectlyMapsDependencies`
- `ChooseVictim_SelectsTransactionWithLeastWorkDone`
- `SetTimeout_ControlsBackgroundDetectionInterval`

### 46. `MVCCManager`
- `CreateVersion_AppendsNewRecordVersionToChain`
- `GarbageCollect_RemovesVersionsInvisibleToAllActiveTransactions`
- `ReadVersion_ReturnsCorrectDataBasedOnTxSnapshot`
- `DetectWriteConflict_WhenTwoTxUpdateSameRecord_ThrowsException`
- `ReadVersion_WhenNoVisibleVersion_ReturnsNull`

---

## 5. Storage Engine

### 47. `StorageEngine`
- `ReadPage_WhenPageNotInBuffer_LoadsFromDisk`
- `WritePage_WhenPageIsDirty_FlushesToDisk`
- `AllocatePage_CreatesNewPageAndReturnsId`
- `DeallocatePage_FreesPageSpace`
- `Sync_ForcesAllDirtyPagesToDisk`
- `FormatDrive_InitializesDataDirectoryStructure`

### 48. `BufferPool`
- `PinPage_IncrementsPinCountAndPreventsEviction`
- `UnpinPage_DecrementsPinCount`
- `FlushPage_ForcesDirtyPageToDisk`
- `FetchPage_WhenPoolFull_EvictsUnpinnedPage`
- `FetchPage_WhenAllPagesPinned_ThrowsBufferFullException`
- `GetHitRate_ReturnsCacheHitRatioMetrics`
- `Clear_EvictsAllUnpinnedPages`
- `UnpinPage_WhenCountIsZero_ThrowsException`

### 49. `PageReplacementAlgorithm`
- `Instantiation_OfInterface_FailsWithTypeError`

### 50. `Page`
- `Init_SetsPageIdAndClearsDirtyFlag`
- `MarkDirty_SetsDirtyFlagToTrue`
- `ReadTuple_ReturnsDataAtOffset`
- `WriteTuple_SavesDataAndUpdatesFreeSpace`
- `HasSpace_ReturnsTrueIfTupleFits`
- `Compact_ReorganizesTuplesToRemoveFragmentation`
- `DeleteTuple_MarksSlotAsEmpty`

### 51. `FileManager`
- `AllocateSpace_CreatesNewBlockAndReturnsId`
- `DeallocateSpace_MarksBlockAsFree`
- `ExtendFile_IncreasesFileSizeWhenFull`
- `CloseAll_ReleasesFileHandles`
- `GetFileSize_ReturnsSizeInBytes`
- `CheckSpace_ReturnsAvailableBlocks`

### 52. `DataFile`
- `Init_OpensFileStreamForDataBlocks`
- `ReadBlock_LoadsBytesFromDisk`
- `WriteBlock_SavesBytesToDisk`
- `DeleteFile_RemovesFromOS`
- `Init_WhenFileLockedByOS_ThrowsIOException`

### 53. `IndexFile`
- `Init_OpensFileStreamForIndexBlocks`
- `WriteBlock_SavesBytesToDisk`
- `ReadBlock_LoadsBytesFromDisk`
- `Rebuild_CompactsIndexData`
- `VerifyChecksum_DetectsCorruption`

---

## 6. Backup & Durability

### 54. `RecoveryManager`
- `Recover_WhenSystemCrashes_ReplaysWALToRestoreState`
- `Recover_WhenUndoNeeded_RollsBackUncommittedTransactions`
- `AnalyzePhase_IdentifiesDirtyPagesAndActiveTx`
- `RedoPhase_ReappliesChangesFromLog`
- `UndoPhase_RevertsChangesOfAbortedTx`
- `Recover_WhenWALFileCorrupt_ThrowsFatalException`

### 55. `CheckpointManager`
- `TakeCheckpoint_FlushesAllDirtyPages`
- `TakeCheckpoint_WritesCheckpointRecordToLog`
- `AutoCheckpoint_TriggersWhenLogReachesSizeLimit`
- `AutoCheckpoint_TriggersWhenTimeIntervalElapsed`
- `GetLastCheckpointLSN_ReadsFromMasterRecord`

### 56. `WALManager`
- `AppendLog_AddsRecordToMemoryBuffer`
- `Flush_WritesBufferToDiskSynchronously`
- `AppendLog_WhenBufferFull_TriggersAutomaticFlush`
- `ReadLog_ReturnsRecordByLSN`
- `TruncateLog_DeletesLogsOlderThanCheckpoint`
- `Flush_WhenDiskFull_ThrowsStorageException`
- `SwitchLogFile_CreatesNewSegmentWhenMaxFileSizeReached`

### 57. `LogRecord`
- `Init_SetsLsnTypeAndPayloadData`
- `Serialize_ConvertsRecordToByteArray`
- `Deserialize_ReconstructsRecordFromBytes`
- `GetTransactionId_ReturnsAssociatedTx`
- `GetUndoInfo_ReturnsBeforeImageForRollback`

---

## 7. Security & Access Control

### 58. `SecurityManager`
- `Authenticate_WhenValidCredentials_ReturnsSessionToken`
- `Authenticate_WhenInvalidCredentials_ThrowsAuthException`
- `Authorize_WhenUserHasRequiredRole_Succeeds`
- `Authorize_WhenUserLacksPermission_ThrowsAccessException`
- `RevokeToken_InvalidatesSessionImmediately`
- `HashPassword_UsesStrongCryptography`
- `Authenticate_WhenAccountLocked_ThrowsLockedException`
- `CleanupTokens_RemovesExpiredSessions`

### 59. `User`
- `Init_SetsUsernameAndHashedPassword`
- `AddRole_AssignsNewRoleToUser`
- `RemoveRole_TakesAwayPermissions`
- `UpdatePassword_HashesAndSavesNewPassword`
- `LockAccount_PreventsLoginAfterFailedAttempts`
- `IsLocked_ReturnsStatus`
- `HasRole_ReturnsTrueIfAssigned`

### 60. `Role`
- `Init_SetsRoleName`
- `AddPermission_GrantsPermissionToRole`
- `RemovePermission_RevokesAccess`
- `HasPermission_ReturnsTrueIfMatchFound`
- `GetAllPermissions_ReturnsCombinedList`
- `InheritRole_AppliesParentPermissionsToChildRole`

### 61. `Permission`
- `Init_SetsResourceAndActionType`
- `Matches_WhenActionAndResourceAlign_ReturnsTrue`
- `Matches_WhenWildcardResource_ReturnsTrueForAll`
- `ToString_FormatsPermissionForLogging`
- `Matches_WhenActionIsDeny_OverridesGrant`

---

