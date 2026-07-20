#  Unit Test Implementation Status

##  Summary Statistics


### Test Cases
- **Total Test Cases:** 354
- ** Done Test Cases:** 75 (21.2%)
- ** Not Done Test Cases:** 279 (78.8%)

##  Implementation Plan (Priority List)

This section suggests the prioritized order for implementing the remaining Unit Tests (TDD Logic). You can tick off individual tests as you implement them.

### Priority 1: 1. Core Server & Connections
#### ⏳ `ConnectionManager`
  - [ ] AcceptConnection_WhenUnderMaxLimit_CreatesClientSession
  - [ ] AcceptConnection_WhenAtMaxLimit_RejectsConnection
  - [ ] AcceptConnection_WhenServerPaused_QueuesOrRejects
  - [ ] CloseConnection_WhenValidSession_ReleasesResources
  - [ ] CloseConnection_WhenInvalidSession_ThrowsException
  - [ ] GetActiveSessions_ReturnsSnapshotOfConnectedClients
  - [ ] BroadcastMessage_SendsToAllActiveSessions
  - [ ] KillSession_ForcefullyTerminatesConnection
  - [ ] Cleanup_RemovesIdleConnectionsAutomatically
  - [ ] AcceptConnection_WhenClientBlacklisted_RejectsImmediately

#### ⏳ `ClientSession`
  - [ ] Init_SetsSessionIdAndTimestamp
  - [ ] Execute_WhenValidQuery_ReturnsExecutionResult
  - [ ] Execute_WhenSessionExpired_ThrowsTimeoutException
  - [ ] Execute_WhenConnectionLost_FailsGracefully
  - [ ] SetSessionVariable_UpdatesInternalState
  - [ ] GetSessionVariable_ReturnsSetValue
  - [ ] Execute_WhenEmptyQuery_ReturnsEmptyResult
  - [ ] GetSessionVariable_WhenKeyNotExists_ReturnsNull
  - [ ] Ping_ResetsIdleTimer

#### ⏳ `DatabaseManager`
  - [ ] CreateDatabase_WhenNameIsValid_CreatesMetadataAndFiles
  - [ ] CreateDatabase_WhenNameExists_ThrowsDuplicateDatabaseException
  - [ ] CreateDatabase_WhenInvalidCharacters_ThrowsValidationException
  - [ ] DropDatabase_WhenExists_RemovesAllAssociatedData
  - [ ] DropDatabase_WhenInUse_ThrowsConcurrencyException
  - [ ] GetDatabase_WhenExists_ReturnsDatabaseInstance
  - [ ] GetDatabase_WhenNotExists_ThrowsDatabaseNotFoundException
  - [ ] ListDatabases_ReturnsAllRegisteredDatabases
  - [ ] RenameDatabase_WhenNewNameValid_UpdatesMetadata
  - [ ] CreateDatabase_WhenDiskFull_ThrowsInsufficientStorageException
  - [ ] CreateDatabase_WhenNameTooLong_ThrowsValidationException
  - [ ] DropDatabase_WhenPermissionDenied_ThrowsSecurityException

#### ⏳ `CatalogManager`
  - [ ] RegisterObject_WhenObjectIsValid_UpdatesCatalogDictionary
  - [ ] RegisterObject_WhenDuplicateId_ThrowsException
  - [ ] FindObject_WhenExists_ReturnsObjectMetadata
  - [ ] FindObject_WhenNotExists_ReturnsNull
  - [ ] RemoveObject_WhenExists_DeletesFromCatalog
  - [ ] RemoveObject_WhenNotExists_ThrowsNotFoundException
  - [ ] UpdateObject_WhenExists_RefreshesMetadata
  - [ ] FlushCatalog_WritesToStorageSuccessfully
  - [ ] LoadCatalog_PopulatesMemoryFromDisk
  - [ ] LoadCatalog_WhenCorruptFile_TriggersRecoveryMode

### Priority 2: 2. Database Object Management
#### ⏳ `View`
  - [ ] Init_SetsQueryDefinition
  - [ ] CompileView_WhenUnderlyingTablesExist_Succeeds
  - [ ] CompileView_WhenTableDropped_ThrowsInvalidViewException
  - [ ] Materialize_CachesResultSetToDisk
  - [ ] Refresh_UpdatesMaterializedData
  - [ ] CompileView_WhenCircularDependencyDetected_ThrowsException

#### ⏳ `StoredProcedure`
  - [ ] Execute_WhenValidParametersProvided_RunsLogic
  - [ ] Execute_WhenTypeMismatchInParams_ThrowsException
  - [ ] Execute_WhenMissingParameters_ThrowsArgumentException
  - [ ] Compile_ValidatesSyntaxAndDependencies
  - [ ] Drop_RemovesProcedureFromCatalog
  - [ ] Execute_WhenProcedureTimesOut_KillsExecution

#### ⏳ `Function`
  - [ ] Evaluate_WhenValidArguments_ReturnsComputedValue
  - [ ] Evaluate_WhenMissingArguments_ThrowsArgumentException
  - [ ] Evaluate_WhenDivideByZero_ThrowsArithmeticException
  - [ ] IsDeterministic_ReturnsTrueIfNoExternalStateUsed
  - [ ] Evaluate_WhenNullPassedToStrictFunction_ReturnsNull

#### ⏳ `Sequence`
  - [ ] NextValue_IncrementsByStepAndReturnsValue
  - [ ] NextValue_WhenMaxLimitReached_ThrowsOverflowException
  - [ ] Reset_SetsValueBackToStart
  - [ ] Init_SetsStartStepAndMaxLimit
  - [ ] CurrentValue_ReturnsCurrentWithoutIncrementing
  - [ ] NextValue_WhenStepIsNegative_DecrementsCorrectly

#### ⏳ `Trigger`
  - [ ] Fire_OnEventConditionMet_ExecutesTriggerAction
  - [ ] Fire_OnEventConditionNotMet_SkipsExecution
  - [ ] Fire_WhenActionFails_RollsBackTransaction
  - [ ] Enable_ActivatesTrigger
  - [ ] Disable_DeactivatesTrigger
  - [ ] Validate_EnsuresNoInfiniteTriggerLoops

#### ⏳ `Partition`
  - [ ] Init_SetsPartitionKeyCorrectly
  - [ ] CheckBoundary_WhenValueInRange_ReturnsTrue
  - [ ] CheckBoundary_WhenValueOutOfRange_ReturnsFalse
  - [ ] Merge_CombinesTwoAdjacentPartitions
  - [ ] Split_DividesPartitionAtGivenValue

#### ⏳ `Index`
  - [ ] Instantiation_OfAbstractClass_FailsWithTypeError

#### ⏳ `BTreeIndex`
  - [ ] InsertKey_WhenValid_AddsNodeToTreeBalancing
  - [ ] Search_WhenKeyExists_ReturnsCorrespondingRowID
  - [ ] Search_WhenKeyNotExists_ReturnsEmptyResult
  - [ ] DeleteKey_WhenExists_RemovesNodeAndRebalances
  - [ ] RangeSearch_ReturnsAllRowIDsInRange
  - [ ] BulkLoad_BuildsTreeEfficientlyFromSortedData
  - [ ] SplitNode_WhenFull_CreatesSibling
  - [ ] MergeNodes_WhenUnderfull_CombinesSiblings

#### ⏳ `HashIndex`
  - [ ] InsertKey_ComputesHashAndAddsToBucket
  - [ ] Search_WhenKeyExists_ResolvesHashToRowID
  - [ ] HandleCollision_CreatesLinkedListInBucket
  - [ ] Resize_ExpandsHashTableWhenLoadFactorExceeded
  - [ ] DeleteKey_RemovesFromBucketLinkedList
  - [ ] ComputeHash_DistributesKeysEvenly

#### ⏳ `BitmapIndex`
  - [ ] InsertKey_UpdatesBitmapBitsForGivenValue
  - [ ] Search_WhenKeyExists_UsesBitwiseOperationsToFindRID
  - [ ] BitwiseAND_CombinesTwoBitmapsForComplexQuery
  - [ ] BitwiseOR_CombinesTwoBitmapsForOrQuery
  - [ ] Compress_ReducesMemoryFootprintOfSparseBitmap
  - [ ] DeleteKey_ClearsBitForDeletedRow

### Priority 3: 3. Query Processor
#### ⏳ `QueryProcessor`
  - [ ] ProcessQuery_WhenValidSQL_ReturnsQueryResult
  - [ ] ProcessQuery_WhenExecutionFails_RollsBackAndThrows
  - [ ] ProcessQuery_WhenTimeoutReached_AbortsQuery
  - [ ] Explain_ReturnsQueryExecutionPlanWithoutRunning
  - [ ] PrepareStatement_CachesCompiledPlanForReuse

#### ⏳ `SQLParser`
  - [ ] Parse_WhenValidSelectStatement_GeneratesAST
  - [ ] Parse_WhenInvalidSyntax_ThrowsSyntaxErrorException
  - [ ] Parse_WhenUnsupportedCommand_ThrowsNotImplementedException
  - [ ] Parse_WhenMissingSemicolon_SucceedsOrThrowsBasedOnDialect
  - [ ] Parse_ComplexJoinAndGroupBy_ConstructsCorrectTree
  - [ ] Parse_NestedSubqueries_HandlesDepthLimits
  - [ ] Parse_WhenMalformedDateLiteral_ThrowsException

#### ⏳ `Lexer`
  - [ ] Tokenize_WhenValidString_ReturnsListOfTokens
  - [ ] Tokenize_IgnoresWhitespaceAndComments
  - [ ] Tokenize_WhenUnclosedStringLiteral_ThrowsLexerException
  - [ ] Tokenize_IdentifiesOperatorsAndPunctuationCorrectly
  - [ ] Tokenize_HandlesEscapedCharactersInStrings

#### ⏳ `AST`
  - [ ] Init_SetsRootNode
  - [ ] Traverse_VisitsAllNodesInCorrectOrder
  - [ ] ToSQL_ReconstructsSQLStringFromTree
  - [ ] Clone_CreatesDeepCopyOfTree
  - [ ] CountNodes_ReturnsTotalSizeOfTree

#### ⏳ `QueryOptimizer`
  - [ ] Optimize_WhenGivenLogicalPlan_TransformsToPhysicalPlan
  - [ ] Optimize_AppliesFilterPushdownRule
  - [ ] Optimize_AppliesJoinReorderingForEfficiency
  - [ ] Optimize_ChoosesIndexScanOverSeqScanWhenSelective
  - [ ] Optimize_EliminatesDeadCodeOrAlwaysFalseConditions
  - [ ] Optimize_FlattensUnnecessarySubqueries
  - [ ] Optimize_WhenStatsMissing_DefaultsToHeuristicRules

#### ⏳ `CostModel`
  - [ ] EstimateCost_CalculatesIOAndCPUCost
  - [ ] EstimateCost_WhenUsingIndex_ReturnsLowerCostThanSeqScan
  - [ ] EstimateCost_ForNestedLoopJoin_IsHigherThanHashJoinForLargeTables
  - [ ] UpdateStatistics_AdjustsInternalWeightsBasedOnFeedback
  - [ ] EstimateMemoryUsage_ForSortOperator_ReturnsExpectedBytes

#### ⏳ `StatisticsManager`
  - [ ] Collect_UpdatesRowCountsAndCardinality
  - [ ] GetStatistics_WhenCalled_ReturnsAccurateMetadata
  - [ ] EstimateSelectivity_ReturnsPercentageOfRowsMatchingFilter
  - [ ] BuildHistogram_ForSkewedDataDistribution
  - [ ] InvalidateStats_WhenTableModifiedSignificantly

#### ⏳ `LogicalPlan`
  - [ ] Init_CreatesEmptyOperatorTree
  - [ ] AddOperator_AppendsToPlan
  - [ ] Validate_EnsuresReferencesExistInCatalog
  - [ ] PrintTree_OutputsFormattedStringForDebugging
  - [ ] GetLeaves_ReturnsBaseTableScans

#### ⏳ `LogicalOperator`
  - [ ] Instantiation_OfAbstractClass_FailsWithTypeError

#### ⏳ `PhysicalPlan`
  - [ ] Init_CreatesEmptyOperatorTree
  - [ ] ValidatePipeline_EnsuresOperatorCompatibility
  - [ ] EstimateTotalCost_SumsCostOfAllOperators
  - [ ] GetRoot_ReturnsTopOperator
  - [ ] Clone_CreatesIsolatedExecutionInstance

#### ⏳ `PhysicalOperator`
  - [ ] Instantiation_OfAbstractClass_FailsWithTypeError

#### ⏳ `QueryExecutor`
  - [ ] ExecutePlan_WhenValidPhysicalPlan_IteratesAndYieldsResults
  - [ ] ExecutePlan_WhenMemoryExceeded_SpillsToDiskOrThrows
  - [ ] ExecutePlan_WhenCanceledByUser_AbortsImmediately
  - [ ] StreamResults_YieldsBatchesInsteadOfLoadingAllIntoMemory
  - [ ] Initialize_AllocatesRequiredTempSpace
  - [ ] Close_ReleasesAllInternalIterators

### Priority 4: 4. Transaction Management
#### ⏳ `TransactionManager`
  - [ ] BeginTransaction_CreatesAndRegistersNewActiveTransaction
  - [ ] Commit_WhenSuccessful_WritesToLogAndChangesState
  - [ ] Rollback_WhenCalled_RevertsAllModifications
  - [ ] Commit_WhenValidationFails_ForcesRollback
  - [ ] GetActiveTransactions_ReturnsListOfCurrentlyRunningTx
  - [ ] SuspendTransaction_TemporarilyHaltsExecution
  - [ ] ResumeTransaction_ContinuesSuspendedExecution
  - [ ] ForceRollbackAll_UsedDuringServerShutdown

#### ⏳ `Transaction`
  - [ ] Init_GeneratesUniqueTransactionId
  - [ ] SetIsolationLevel_UpdatesTransactionProperties
  - [ ] AddLock_TracksLocksHeldByThisTransaction
  - [ ] ReleaseAllLocks_CalledDuringCommitOrRollback
  - [ ] SetSavepoint_CreatesPartialRollbackMarker
  - [ ] RollbackToSavepoint_RevertsChangesAfterMarker

#### ⏳ `IsolationLevel`
  - [ ] EnumValues_IncludeReadCommittedAndSerializable

#### ⏳ `TransactionState`
  - [ ] EnumValues_IncludeActiveCommittedAborted

#### ⏳ `LockManager`
  - [ ] AcquireLock_WhenResourceFree_GrantsLockInstantly
  - [ ] AcquireLock_WhenResourceLocked_BlocksOrThrowsTimeout
  - [ ] ReleaseLock_WhenHoldingLock_FreesResourceAndWakesWaiters
  - [ ] AcquireLock_WhenSharedLockExists_GrantsAnotherSharedLock
  - [ ] AcquireLock_WhenSharedLockExists_BlocksExclusiveLock
  - [ ] UpgradeLock_ConvertsSharedToExclusiveIfPossible
  - [ ] DowngradeLock_ConvertsExclusiveToShared
  - [ ] ReleaseLock_WhenNotHoldingLock_ThrowsException

#### ⏳ `LockTable`
  - [ ] GetLocks_ReturnsCurrentLockInformation
  - [ ] AddLock_RegistersNewLockForResource
  - [ ] RemoveLock_DeletesRegistration
  - [ ] Clear_RemovesAllLocksDuringSystemReset
  - [ ] CountLocks_ForSpecificTransactionId

#### ⏳ `DeadlockDetector`
  - [ ] DetectAndResolve_WhenCycleFound_AbortsVictimTransaction
  - [ ] DetectAndResolve_WhenNoCycleFound_DoesNothing
  - [ ] BuildWaitForGraph_CorrectlyMapsDependencies
  - [ ] ChooseVictim_SelectsTransactionWithLeastWorkDone
  - [ ] SetTimeout_ControlsBackgroundDetectionInterval

#### ⏳ `MVCCManager`
  - [ ] CreateVersion_AppendsNewRecordVersionToChain
  - [ ] GarbageCollect_RemovesVersionsInvisibleToAllActiveTransactions
  - [ ] ReadVersion_ReturnsCorrectDataBasedOnTxSnapshot
  - [ ] DetectWriteConflict_WhenTwoTxUpdateSameRecord_ThrowsException
  - [ ] ReadVersion_WhenNoVisibleVersion_ReturnsNull

### Priority 5: 7. Security & Access Control
#### ⏳ `SecurityManager`
  - [ ] Authenticate_WhenValidCredentials_ReturnsSessionToken
  - [ ] Authenticate_WhenInvalidCredentials_ThrowsAuthException
  - [ ] Authorize_WhenUserHasRequiredRole_Succeeds
  - [ ] Authorize_WhenUserLacksPermission_ThrowsAccessException
  - [ ] RevokeToken_InvalidatesSessionImmediately
  - [ ] HashPassword_UsesStrongCryptography
  - [ ] Authenticate_WhenAccountLocked_ThrowsLockedException
  - [ ] CleanupTokens_RemovesExpiredSessions

#### ⏳ `User`
  - [ ] Init_SetsUsernameAndHashedPassword
  - [ ] AddRole_AssignsNewRoleToUser
  - [ ] RemoveRole_TakesAwayPermissions
  - [ ] UpdatePassword_HashesAndSavesNewPassword
  - [ ] LockAccount_PreventsLoginAfterFailedAttempts
  - [ ] IsLocked_ReturnsStatus
  - [ ] HasRole_ReturnsTrueIfAssigned

#### ⏳ `Role`
  - [ ] Init_SetsRoleName
  - [ ] AddPermission_GrantsPermissionToRole
  - [ ] RemovePermission_RevokesAccess
  - [ ] HasPermission_ReturnsTrueIfMatchFound
  - [ ] GetAllPermissions_ReturnsCombinedList
  - [ ] InheritRole_AppliesParentPermissionsToChildRole

#### ⏳ `Permission`
  - [ ] Init_SetsResourceAndActionType
  - [ ] Matches_WhenActionAndResourceAlign_ReturnsTrue
  - [ ] Matches_WhenWildcardResource_ReturnsTrueForAll
  - [ ] ToString_FormatsPermissionForLogging
  - [ ] Matches_WhenActionIsDeny_OverridesGrant

### Priority 6: 5. Storage Engine
#### ⏳ `StorageEngine`
  - [ ] ReadPage_WhenPageNotInBuffer_LoadsFromDisk
  - [ ] WritePage_WhenPageIsDirty_FlushesToDisk
  - [ ] AllocatePage_CreatesNewPageAndReturnsId
  - [ ] DeallocatePage_FreesPageSpace
  - [ ] Sync_ForcesAllDirtyPagesToDisk
  - [ ] FormatDrive_InitializesDataDirectoryStructure

#### ⏳ `BufferPool`
  - [ ] PinPage_IncrementsPinCountAndPreventsEviction
  - [ ] UnpinPage_DecrementsPinCount
  - [ ] FlushPage_ForcesDirtyPageToDisk
  - [ ] FetchPage_WhenPoolFull_EvictsUnpinnedPage
  - [ ] FetchPage_WhenAllPagesPinned_ThrowsBufferFullException
  - [ ] GetHitRate_ReturnsCacheHitRatioMetrics
  - [ ] Clear_EvictsAllUnpinnedPages
  - [ ] UnpinPage_WhenCountIsZero_ThrowsException

#### ⏳ `PageReplacementAlgorithm`
  - [ ] Instantiation_OfInterface_FailsWithTypeError

#### ⏳ `Page`
  - [ ] Init_SetsPageIdAndClearsDirtyFlag
  - [ ] MarkDirty_SetsDirtyFlagToTrue
  - [ ] ReadTuple_ReturnsDataAtOffset
  - [ ] WriteTuple_SavesDataAndUpdatesFreeSpace
  - [ ] HasSpace_ReturnsTrueIfTupleFits
  - [ ] Compact_ReorganizesTuplesToRemoveFragmentation
  - [ ] DeleteTuple_MarksSlotAsEmpty

#### ⏳ `FileManager`
  - [ ] AllocateSpace_CreatesNewBlockAndReturnsId
  - [ ] DeallocateSpace_MarksBlockAsFree
  - [ ] ExtendFile_IncreasesFileSizeWhenFull
  - [ ] CloseAll_ReleasesFileHandles
  - [ ] GetFileSize_ReturnsSizeInBytes
  - [ ] CheckSpace_ReturnsAvailableBlocks

#### ⏳ `DataFile`
  - [ ] Init_OpensFileStreamForDataBlocks
  - [ ] ReadBlock_LoadsBytesFromDisk
  - [ ] WriteBlock_SavesBytesToDisk
  - [ ] DeleteFile_RemovesFromOS
  - [ ] Init_WhenFileLockedByOS_ThrowsIOException

#### ⏳ `IndexFile`
  - [ ] Init_OpensFileStreamForIndexBlocks
  - [ ] WriteBlock_SavesBytesToDisk
  - [ ] ReadBlock_LoadsBytesFromDisk
  - [ ] Rebuild_CompactsIndexData
  - [ ] VerifyChecksum_DetectsCorruption

### Priority 7: 6. Backup & Durability
#### ⏳ `RecoveryManager`
  - [ ] Recover_WhenSystemCrashes_ReplaysWALToRestoreState
  - [ ] Recover_WhenUndoNeeded_RollsBackUncommittedTransactions
  - [ ] AnalyzePhase_IdentifiesDirtyPagesAndActiveTx
  - [ ] RedoPhase_ReappliesChangesFromLog
  - [ ] UndoPhase_RevertsChangesOfAbortedTx
  - [ ] Recover_WhenWALFileCorrupt_ThrowsFatalException

#### ⏳ `CheckpointManager`
  - [ ] TakeCheckpoint_FlushesAllDirtyPages
  - [ ] TakeCheckpoint_WritesCheckpointRecordToLog
  - [ ] AutoCheckpoint_TriggersWhenLogReachesSizeLimit
  - [ ] AutoCheckpoint_TriggersWhenTimeIntervalElapsed
  - [ ] GetLastCheckpointLSN_ReadsFromMasterRecord

#### ⏳ `WALManager`
  - [ ] AppendLog_AddsRecordToMemoryBuffer
  - [ ] Flush_WritesBufferToDiskSynchronously
  - [ ] AppendLog_WhenBufferFull_TriggersAutomaticFlush
  - [ ] ReadLog_ReturnsRecordByLSN
  - [ ] TruncateLog_DeletesLogsOlderThanCheckpoint
  - [ ] Flush_WhenDiskFull_ThrowsStorageException
  - [ ] SwitchLogFile_CreatesNewSegmentWhenMaxFileSizeReached

#### ⏳ `LogRecord`
  - [ ] Init_SetsLsnTypeAndPayloadData
  - [ ] Serialize_ConvertsRecordToByteArray
  - [ ] Deserialize_ReconstructsRecordFromBytes
  - [ ] GetTransactionId_ReturnsAssociatedTx
  - [ ] GetUndoInfo_ReturnsBeforeImageForRollback

## ✅ Completed Classes (Done)

The following classes have had their sequence diagrams mapped completely to their python Unit Test implementations:

### 1. Core Server & Connections
#### ✅ `DatabaseServer`
  - [x] Start_WhenConfigValid_InitializesAllSubsystems
  - [x] Start_WhenAlreadyRunning_ThrowsIllegalStateException
  - [x] Stop_WhenRunning_ShutsDownGracefully
  - [x] Stop_WhenAlreadyStopped_DoesNothing
  - [x] Status_ReturnsCurrentOperationalState
  - [x] Start_WhenPortAlreadyInUse_ThrowsBindException
  - [x] Stop_WhenActiveTransactionsExist_WaitsForCompletionOrTimeout
  - [x] Restart_GracefullyStopsAndStartsSystem
  - [x] Init_WithMissingConfigFilePath_ThrowsConfigurationException
  - [x] HealthCheck_ReturnsTrueIfAllSubsystemsAreRunning

#### ✅ `Database`
  - [x] Init_SetsDatabaseNameCorrectly
  - [x] Open_WhenValidMetadata_LoadsDatabaseContext
  - [x] Open_WhenCorruptedMetadata_ThrowsCorruptionException
  - [x] Close_FlushesUnsavedChangesAndReleasesLocks
  - [x] GetSchema_WhenSchemaExists_ReturnsSchema
  - [x] CreateSchema_WhenNameValid_AddsToDatabase
  - [x] Close_WhenAlreadyClosed_DoesNothing
  - [x] Open_WhenMissingDataFiles_ThrowsFileNotFoundException

### 2. Database Object Management
#### ✅ `Schema`
  - [x] Init_SetsSchemaName
  - [x] CreateTable_WhenValidTable_RegistersInSchema
  - [x] CreateTable_WhenTableNameExists_ThrowsException
  - [x] DropTable_WhenExists_RemovesFromSchema
  - [x] DropTable_WhenNotExists_ThrowsException
  - [x] GetTable_WhenExists_ReturnsTable
  - [x] ListTables_ReturnsAllRegisteredTables
  - [x] Validate_EnsuresSchemaNameIsAlphanumeric

#### ✅ `Table`
  - [x] Insert_WhenValidRowAndConstraintsMet_AppendsRow
  - [x] Insert_WhenPrimaryKeyViolated_ThrowsConstraintException
  - [x] Update_WhenRowExists_ModifiesValues
  - [x] Update_WhenRowNotExists_ReturnsZeroAffectedRows
  - [x] Delete_WhenRowExists_RemovesRow
  - [x] Insert_WhenForeignKeyViolated_ThrowsException
  - [x] Insert_WhenCheckConstraintViolated_ThrowsException
  - [x] Truncate_RemovesAllRowsRapidly
  - [x] AddColumn_AppendsColumnDefinitionToSchema
  - [x] DropColumn_RemovesColumnAndData
  - [x] GetRowCount_ReturnsAccurateCount
  - [x] RenameColumn_WhenExists_UpdatesMetadataAndViews

#### ✅ `Column`
  - [x] Init_SetsNameAndNullableFlags
  - [x] ValidateType_WhenDataMatchesColumnType_Succeeds
  - [x] ValidateType_WhenDataIsStringForIntColumn_ThrowsTypeException
  - [x] ValidateNullable_WhenNullPassedToNotNullColumn_ThrowsException
  - [x] SetDefaultValue_StoresDefaultExpression
  - [x] ChangeType_WhenCompatible_Succeeds
  - [x] ChangeType_WhenIncompatible_ThrowsException

#### ✅ `Row`
  - [x] Init_GeneratesRowIdAndInitializesValueList
  - [x] GetValue_WhenIndexValid_ReturnsData
  - [x] GetValue_WhenIndexOutOfBounds_ThrowsIndexException
  - [x] SetValue_UpdatesDataAtIndex
  - [x] Serialize_ConvertsToByteArray
  - [x] Deserialize_ReadsFromByteArray
  - [x] GetSize_ReturnsByteSizeOfAllValues

#### ✅ `DataType`
  - [x] EnumValues_IncludeIntVarcharDateBoolean
  - [x] ParseString_WhenValidFormat_ReturnsDataTypeInstance
  - [x] ParseString_WhenInvalidFormat_ThrowsParseException
  - [x] GetSize_ReturnsByteSizeForFixedTypes
  - [x] IsVariableLength_ReturnsTrueForVarchar

#### ✅ `Constraint`
  - [x] Instantiation_OfAbstractClass_FailsWithTypeError

#### ✅ `PrimaryKey`
  - [x] Validate_WhenValueIsUniqueAndNotNull_Succeeds
  - [x] Validate_WhenValueIsNull_ThrowsNullException
  - [x] Validate_WhenValueIsDuplicate_ThrowsDuplicateKeyException
  - [x] Validate_WithCompositeKey_ChecksAllColumns
  - [x] Drop_RemovesIndexFromStorage

#### ✅ `ForeignKey`
  - [x] Validate_WhenReferencedRowExists_Succeeds
  - [x] Validate_WhenReferencedRowDoesNotExist_ThrowsForeignKeyException
  - [x] Init_SetsReferenceTableCorrectly
  - [x] OnDeleteCascade_RemovesChildRowsWhenParentDeleted
  - [x] OnDeleteRestrict_ThrowsExceptionWhenParentDeleted
  - [x] OnUpdateCascade_ModifiesChildRowsWhenParentKeyChanges

#### ✅ `UniqueConstraint`
  - [x] Validate_WhenValueIsGloballyUnique_Succeeds
  - [x] Validate_WhenValueExistsInAnotherRow_ThrowsException
  - [x] Validate_WhenValueIsNull_SucceedsIfNullable

#### ✅ `CheckConstraint`
  - [x] Validate_WhenExpressionEvaluatesToTrue_Succeeds
  - [x] Validate_WhenExpressionEvaluatesToFalse_ThrowsCheckException
  - [x] Validate_WhenExpressionUsesInvalidColumn_ThrowsException
