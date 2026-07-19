# 📦 Summary of New Properties & Methods

Below is the comprehensive list of all **Properties** and **Methods** that have been added to the 61 Classes to support the practical scenarios of the 354 Unit Tests.

**Quick Statistics:**
- Total new Properties: **84**
- Total new Methods: **222**

---

## 📂 Subsystem: BackupDurability

### 🔹 Class: `CheckpointManager`
**Properties:**
- `bufferPool`
**Methods:**
- `autoCheckpoint()`
- `getLastCheckpointLSN()`
- `takeCheckpoint()`

### 🔹 Class: `LogRecord`
**Properties:**
- `lsn`
- `payload`
- `type`
**Methods:**
- `deserialize()`
- `getTransactionId()`
- `getUndoInfo()`
- `serialize()`

### 🔹 Class: `RecoveryManager`
**Properties:**
- `walManager`
**Methods:**
- `analyzePhase()`
- `recover()`
- `redoPhase()`
- `undoPhase()`

### 🔹 Class: `WALManager`
**Properties:**
- `BUFFER_LIMIT (Int)`
- `logBuffer (List)`
**Methods:**
- `appendLog()`
- `flush()`
- `readLog()`
- `switchLogFile()`
- `truncateLog()`

## 📂 Subsystem: Core

### 🔹 Class: `CatalogManager`
**Properties:**
- `catalogDict (Dict)`
**Methods:**
- `findObject()`
- `flushCatalog()`
- `loadCatalog()`
- `registerObject()`
- `removeObject()`
- `updateObject()`

### 🔹 Class: `ClientSession`
**Properties:**
- `TIMEOUT (Int)`
- `connectTime (DateTime)`
- `sessionVariables (Dict)`
**Methods:**
- `execute()`
- `getSessionVariable()`
- `ping()`
- `setSessionVariable()`

### 🔹 Class: `ConnectionManager`
**Properties:**
- `MAX_LIMIT (Int)`
- `activeConnections (List)`
- `isPaused (Bool)`
**Methods:**
- `acceptConnection()`
- `broadcastMessage()`
- `cleanup()`
- `closeConnection()`
- `getActiveSessions()`
- `killSession()`

### 🔹 Class: `Database`
**Properties:**
- `contextData`
- `schemaDict (Dict)`
**Methods:**
- `close()`
- `createSchema()`
- `getSchema()`
- `open()`

### 🔹 Class: `DatabaseManager`
**Methods:**
- `createDatabase()`
- `dropDatabase()`
- `getDatabase()`
- `listDatabases()`
- `renameDatabase()`

### 🔹 Class: `DatabaseServer`
**Properties:**
- `catalogManager`
- `config (Configuration)`
- `connectionManager`
- `databaseManager`
**Methods:**
- `healthCheck()`
- `restart()`
- `status()`

## 📂 Subsystem: DatabaseObjectManagement

### 🔹 Class: `BitmapIndex`
**Properties:**
- `bitmaps (Dict)`
**Methods:**
- `bitwiseAND()`
- `bitwiseOR()`
- `compress()`
- `deleteKey()`
- `insertKey()`
- `search()`

### 🔹 Class: `BTreeIndex`
**Properties:**
- `rootNode`
**Methods:**
- `bulkLoad()`
- `deleteKey()`
- `insertKey()`
- `mergeNodes()`
- `rangeSearch()`
- `search()`
- `splitNode()`

### 🔹 Class: `CheckConstraint`
**Properties:**
- `expression (String)`
**Methods:**
- `validate()`

### 🔹 Class: `Column`
**Properties:**
- `dataType`
- `defaultValue`
- `isNullable (Bool)`
**Methods:**
- `changeType()`
- `setDefaultValue()`
- `validateNullable()`
- `validateType()`

### 🔹 Class: `DataType`
**Methods:**
- `getSize()`
- `isVariableLength()`
- `parseString()`

### 🔹 Class: `ForeignKey`
**Properties:**
- `onDeleteAction`
- `referenceColumn`
- `referenceTable`
**Methods:**
- `onDeleteCascade()`
- `onDeleteRestrict()`
- `onUpdateCascade()`
- `validate()`

### 🔹 Class: `Function`
**Properties:**
- `arguments (List)`
**Methods:**
- `evaluate()`
- `isDeterministic()`

### 🔹 Class: `HashIndex`
**Properties:**
- `hashTable (Dict)`
**Methods:**
- `computeHash()`
- `deleteKey()`
- `handleCollision()`
- `insertKey()`
- `resize()`
- `search()`

### 🔹 Class: `Partition`
**Properties:**
- `maxValue`
- `minValue`
- `partitionKey`
**Methods:**
- `checkBoundary()`
- `merge()`
- `split()`

### 🔹 Class: `PrimaryKey`
**Properties:**
- `columns (List)`
**Methods:**
- `drop()`
- `validate()`

### 🔹 Class: `Row`
**Properties:**
- `rowId (UUID)`
- `values (List)`
**Methods:**
- `deserialize()`
- `getSize()`
- `getValue()`
- `serialize()`
- `setValue()`

### 🔹 Class: `Schema`
**Properties:**
- `tables (Dict)`
**Methods:**
- `createTable()`
- `dropTable()`
- `getTable()`
- `listTables()`
- `validate()`

### 🔹 Class: `Sequence`
**Properties:**
- `currentValue (Int)`
- `maxValue (Int)`
- `step (Int)`
**Methods:**
- `currentValue()`
- `nextValue()`
- `reset()`

### 🔹 Class: `StoredProcedure`
**Properties:**
- `parameters (List)`
**Methods:**
- `compile()`
- `drop()`
- `execute()`

### 🔹 Class: `Table`
**Properties:**
- `columns (List)`
- `rows (List)`
**Methods:**
- `addColumn()`
- `delete()`
- `dropColumn()`
- `getRowCount()`
- `insert()`
- `renameColumn()`
- `truncate()`
- `update()`

### 🔹 Class: `Trigger`
**Properties:**
- `action`
- `eventCondition`
- `isActive (Bool)`
**Methods:**
- `disable()`
- `enable()`
- `fire()`
- `validate()`

### 🔹 Class: `UniqueConstraint`
**Methods:**
- `validate()`

### 🔹 Class: `View`
**Properties:**
- `materializedData (Cache)`
- `queryDefinition (String)`
**Methods:**
- `compileView()`
- `materialize()`
- `refresh()`

## 📂 Subsystem: QueryProcessor

### 🔹 Class: `AST`
**Properties:**
- `rootNode`
**Methods:**
- `clone()`
- `countNodes()`
- `toSQL()`
- `traverse()`

### 🔹 Class: `CostModel`
**Methods:**
- `estimateCost()`
- `estimateMemoryUsage()`
- `updateStatistics()`

### 🔹 Class: `Lexer`
**Methods:**
- `tokenize()`

### 🔹 Class: `LogicalPlan`
**Properties:**
- `operators (List)`
**Methods:**
- `addOperator()`
- `getLeaves()`
- `printTree()`
- `validate()`

### 🔹 Class: `PhysicalPlan`
**Properties:**
- `operators (List)`
**Methods:**
- `clone()`
- `estimateTotalCost()`
- `getRoot()`
- `validatePipeline()`

### 🔹 Class: `QueryExecutor`
**Properties:**
- `memoryLimit (Int)`
**Methods:**
- `close()`
- `executePlan()`
- `initialize()`
- `streamResults()`

### 🔹 Class: `QueryOptimizer`
**Methods:**
- `optimize()`

### 🔹 Class: `QueryProcessor`
**Methods:**
- `explain()`
- `prepareStatement()`
- `processQuery()`

### 🔹 Class: `SQLParser`
**Methods:**
- `parse()`

### 🔹 Class: `StatisticsManager`
**Properties:**
- `cardinalities (Dict)`
- `rowCounts (Dict)`
**Methods:**
- `buildHistogram()`
- `collect()`
- `estimateSelectivity()`
- `getStatistics()`
- `invalidateStats()`

## 📂 Subsystem: SecurityAccessControl

### 🔹 Class: `Permission`
**Properties:**
- `actionType`
- `resource`
**Methods:**
- `matches()`
- `toString()`

### 🔹 Class: `Role`
**Properties:**
- `permissions (List)`
**Methods:**
- `addPermission()`
- `getAllPermissions()`
- `hasPermission()`
- `inheritRole()`
- `removePermission()`

### 🔹 Class: `SecurityManager`
**Properties:**
- `activeTokens (Set)`
- `usersDict (Dict)`
**Methods:**
- `authenticate()`
- `authorize()`
- `cleanupTokens()`
- `hashPassword()`
- `revokeToken()`

### 🔹 Class: `User`
**Properties:**
- `isLocked (Bool)`
- `roles (List)`
**Methods:**
- `addRole()`
- `hasRole()`
- `isLocked()`
- `lockAccount()`
- `removeRole()`
- `updatePassword()`

## 📂 Subsystem: StorageEngine

### 🔹 Class: `BufferPool`
**Properties:**
- `maxSize (Int)`
- `pages (Dict)`
- `replacementAlgorithm`
**Methods:**
- `clear()`
- `fetchPage()`
- `flushPage()`
- `getHitRate()`
- `pinPage()`
- `unpinPage()`

### 🔹 Class: `DataFile`
**Properties:**
- `fileStream`
**Methods:**
- `deleteFile()`
- `readBlock()`
- `writeBlock()`

### 🔹 Class: `FileManager`
**Properties:**
- `freeBlocks (List)`
**Methods:**
- `allocateSpace()`
- `checkSpace()`
- `closeAll()`
- `deallocateSpace()`
- `extendFile()`
- `getFileSize()`

### 🔹 Class: `IndexFile`
**Properties:**
- `fileStream`
**Methods:**
- `readBlock()`
- `rebuild()`
- `verifyChecksum()`
- `writeBlock()`

### 🔹 Class: `Page`
**Properties:**
- `isDirty (Bool)`
- `pageId`
- `pinCount (Int)`
**Methods:**
- `compact()`
- `deleteTuple()`
- `hasSpace()`
- `markDirty()`
- `readTuple()`
- `writeTuple()`

### 🔹 Class: `StorageEngine`
**Methods:**
- `allocatePage()`
- `deallocatePage()`
- `formatDrive()`
- `readPage()`
- `sync()`
- `writePage()`

## 📂 Subsystem: TransactionManagement

### 🔹 Class: `DeadlockDetector`
**Properties:**
- `timeout (Int)`
- `waitForGraph`
**Methods:**
- `buildWaitForGraph()`
- `chooseVictim()`
- `detectAndResolve()`
- `setTimeout()`

### 🔹 Class: `LockManager`
**Properties:**
- `deadlockDetector`
- `lockTable`
**Methods:**
- `acquireLock()`
- `downgradeLock()`
- `releaseLock()`
- `upgradeLock()`

### 🔹 Class: `LockTable`
**Properties:**
- `locks (Dict)`
**Methods:**
- `addLock()`
- `clear()`
- `countLocks()`
- `getLocks()`
- `removeLock()`

### 🔹 Class: `MVCCManager`
**Properties:**
- `versionChain (List)`
**Methods:**
- `createVersion()`
- `detectWriteConflict()`
- `garbageCollect()`
- `readVersion()`

### 🔹 Class: `Transaction`
**Properties:**
- `heldLocks (List)`
- `isolationLevel`
- `savepoints (List)`
- `state`
- `transactionId`
**Methods:**
- `addLock()`
- `releaseAllLocks()`
- `rollbackToSavepoint()`
- `setIsolationLevel()`
- `setSavepoint()`

### 🔹 Class: `TransactionManager`
**Properties:**
- `activeTransactions (Dict)`
- `walManager`
**Methods:**
- `beginTransaction()`
- `commit()`
- `forceRollbackAll()`
- `getActiveTransactions()`
- `resumeTransaction()`
- `rollback()`
- `suspendTransaction()`

