# Complete DBMS API Endpoint Documentation

---

## 1. Database
Manages database lifecycle operations including creation, deletion, state transition, and physical storage recovery.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/databases` | `CreateDatabaseAsync` | `None` | `None` | `None` | `CreateDatabaseRequest` | `201 Created`<br>`DatabaseDetail` |
| **GET** | `/databases` | `GetDatabasesAsync` | `None` | `name, state, storageEngine, owner, createdFrom, createdTo, sort` | `page, pageSize` | `None` | `200 OK`<br>`DatabaseList` |
| **GET** | `/databases/{dbName}` | `GetDatabaseAsync` | `dbName` | `includeSchemas, includeStatistics` | `None` | `None` | `200 OK`<br>`DatabaseDetail` |
| **DELETE** | `/databases/{dbName}` | `DropDatabaseAsync` | `dbName` | `force, deleteFiles, backupBeforeDrop` | `None` | `None` | `200 OK`<br>`SimpleMessage` |
| **POST** | `/databases/{dbName}/open` | `OpenDatabaseAsync` | `dbName` | `wait, timeoutSeconds` | `None` | `Optional body` | `200 OK`<br>`DatabaseDetail` |
| **POST** | `/databases/{dbName}/close` | `CloseDatabaseAsync` | `dbName` | `force, wait, timeoutSeconds` | `None` | `Optional body` | `200 OK`<br>`DatabaseDetail` |
| **POST** | `/databases/{dbName}/readonly` | `SetReadOnlyAsync` | `dbName` | `wait, timeoutSeconds` | `None` | `SetDatabaseReadOnlyRequest` | `200 OK`<br>`DatabaseDetail` |
| **POST** | `/databases/{dbName}/recovery` | `StartRecoveryAsync` | `dbName` | `wait, timeoutSeconds` | `None` | `StartRecoveryRequest` | `200 OK`<br>`SimpleMessage` |

---

## 2. Schema
Provides namespace isolation for database tables, views, and programmatic routines.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/databases/{dbName}/schemas` | `CreateSchemaAsync` | `dbName` | `None` | `None` | `CreateSchemaRequest` | `201 Created`<br>`SchemaDetail` |
| **GET** | `/databases/{dbName}/schemas` | `GetSchemasAsync` | `dbName` | `name, owner, sort` | `page, pageSize` | `None` | `200 OK`<br>`SchemaList` |
| **GET** | `/databases/{dbName}/schemas/{schemaName}` | `GetSchemaAsync` | `dbName, schemaName` | `includeObjects, includeStatistics` | `None` | `None` | `200 OK`<br>`SchemaDetail` |
| **PUT** | `/databases/{dbName}/schemas/{schemaName}` | `UpdateSchemaAsync` | `dbName, schemaName` | `None` | `None` | `UpdateSchemaRequest` | `200 OK`<br>`SchemaDetail` |
| **DELETE** | `/databases/{dbName}/schemas/{schemaName}` | `DropSchemaAsync` | `dbName, schemaName` | `cascade, force` | `None` | `None` | `200 OK`<br>`SimpleMessage` |

---

## 3. Table
Handles the creation, inspection, editing, and dropping of physical table structures.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/schemas/{schemaName}/tables` | `CreateTableAsync` | `schemaName` | `None` | `None` | `CreateTableRequest` | `201 Created`<br>`TableDetail` |
| **GET** | `/schemas/{schemaName}/tables` | `GetTablesAsync` | `schemaName` | `name, sort` | `page, pageSize` | `None` | `200 OK`<br>`TableList` |
| **GET** | `/schemas/{schemaName}/tables/{tableName}` | `GetTableAsync` | `schemaName, tableName` | `includeColumns, includeIndexes` | `None` | `None` | `200 OK`<br>`TableDetail` |
| **PUT** | `/schemas/{schemaName}/tables/{tableName}` | `UpdateTableAsync` | `schemaName, tableName` | `None` | `None` | `UpdateTableRequest` | `200 OK`<br>`TableDetail` |
| **DELETE** | `/schemas/{schemaName}/tables/{tableName}` | `DropTableAsync` | `schemaName, tableName` | `cascade, force` | `None` | `None` | `200 OK`<br>`SimpleMessage` |

---

## 4. Column
Manages individual column attributes, data types, and logical metadata.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/tables/{tableName}/columns` | `AddColumnAsync` | `tableName` | `None` | `None` | `AddColumnRequest` | `201 Created`<br>`ColumnDetail` |
| **GET** | `/tables/{tableName}/columns` | `GetColumnsAsync` | `tableName` | `type, sort` | `page, pageSize` | `None` | `200 OK`<br>`ColumnList` |
| **PUT** | `/tables/{tableName}/columns/{columnName}` | `UpdateColumnAsync` | `tableName, columnName` | `None` | `None` | `UpdateColumnRequest` | `200 OK`<br>`ColumnDetail` |
| **DELETE** | `/tables/{tableName}/columns/{columnName}` | `DropColumnAsync` | `tableName, columnName` | `force` | `None` | `None` | `200 OK`<br>`SimpleMessage` |

---

## 5. Row
Performs CRUD operations directly on the heap-allocated database data records.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/tables/{tableName}/rows` | `InsertRowAsync` | `tableName` | `None` | `None` | `InsertRowRequest` | `201 Created`<br>`RowDetail` |
| **GET** | `/tables/{tableName}/rows` | `GetRowsAsync` | `tableName` | `filterExpression, sort` | `page, pageSize` | `None` | `200 OK`<br>`RowList` |
| **GET** | `/tables/{tableName}/rows/{rowId}` | `GetRowAsync` | `tableName, rowId` | `None` | `None` | `None` | `200 OK`<br>`RowDetail` |
| **PUT** | `/tables/{tableName}/rows/{rowId}` | `UpdateRowAsync` | `tableName, rowId` | `None` | `None` | `UpdateRowRequest` | `200 OK`<br>`RowDetail` |
| **DELETE** | `/tables/{tableName}/rows/{rowId}` | `DeleteRowAsync` | `tableName, rowId` | `None` | `None` | `None` | `200 OK`<br>`SimpleMessage` |

---

## 6. Constraints
Enforces check, unique, primary key, and foreign key referential database boundaries.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/constraints/check` | `CreateCheckConstraintAsync` | `None` | `None` | `None` | `CheckConstraintRequest` | `201 Created`<br>`ConstraintDetail` |
| **POST** | `/constraints/primarykey` | `CreatePrimaryKeyAsync` | `None` | `None` | `None` | `PrimaryKeyRequest` | `201 Created`<br>`ConstraintDetail` |
| **POST** | `/constraints/unique` | `CreateUniqueConstraintAsync`| `None` | `None` | `None` | `UniqueConstraintRequest` | `201 Created`<br>`ConstraintDetail` |
| **POST** | `/constraints/foreignkey` | `CreateForeignKeyAsync` | `None` | `None` | `None` | `ForeignKeyRequest` | `201 Created`<br>`ConstraintDetail` |
| **PUT** | `/constraints/{constraintId}` | `UpdateConstraintAsync` | `constraintId` | `None` | `None` | `UpdateConstraintRequest` | `200 OK`<br>`ConstraintDetail` |
| **DELETE** | `/constraints/{constraintId}` | `DropConstraintAsync` | `constraintId` | `force` | `None` | `None` | `200 OK`<br>`SimpleMessage` |

---

## 7. Indexes
Deals with index table structure creation, deletions, point lookups, and range scans.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/tables/{tableName}/indexes` | `CreateIndexAsync` | `tableName` | `None` | `None` | `CreateIndexRequest` | `201 Created`<br>`IndexDetail` |
| **GET** | `/tables/{tableName}/indexes` | `GetIndexesAsync` | `tableName` | `type, sort` | `page, pageSize` | `None` | `200 OK`<br>`IndexList` |
| **DELETE** | `/tables/{tableName}/indexes/{indexName}` | `DropIndexAsync` | `tableName, indexName` | `None` | `None` | `None` | `200 OK`<br>`SimpleMessage` |
| **POST** | `/tables/{tableName}/indexes/search` | `IndexSearchAsync` | `tableName` | `None` | `None` | `IndexSearchRequest` | `200 OK`<br>`IndexSearchResponse`|
| **POST** | `/tables/{tableName}/indexes/range-search`| `IndexRangeSearchAsync` | `tableName` | `None` | `None` | `IndexRangeSearchRequest`| `200 OK`<br>`IndexSearchResponse`|

---

## 8. Partition
Enables horizontal scaling of tables into individual partitioned block segments.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/partitions` | `CreatePartitionAsync` | `None` | `None` | `None` | `CreatePartitionRequest` | `201 Created`<br>`PartitionDetail` |
| **GET** | `/partitions` | `GetPartitionsAsync` | `None` | `tableName, sort` | `page, pageSize` | `None` | `200 OK`<br>`PartitionList` |
| **PUT** | `/partitions/{partitionId}` | `UpdatePartitionAsync` | `partitionId` | `None` | `None` | `UpdatePartitionRequest` | `200 OK`<br>`PartitionDetail` |
| **DELETE** | `/partitions/{partitionId}` | `DropPartitionAsync` | `partitionId` | `merge` | `None` | `None` | `200 OK`<br>`SimpleMessage` |

---

## 9. Views
Maintains relational virtual schema tables computed from saved subqueries.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/views` | `CreateViewAsync` | `None` | `None` | `None` | `CreateViewRequest` | `201 Created`<br>`ViewDetail` |
| **GET** | `/views` | `GetViewsAsync` | `None` | `name, sort` | `page, pageSize` | `None` | `200 OK`<br>`ViewList` |
| **PUT** | `/views/{viewName}` | `UpdateViewAsync` | `viewName` | `None` | `None` | `UpdateViewRequest` | `200 OK`<br>`ViewDetail` |
| **DELETE** | `/views/{viewName}` | `DropViewAsync` | `viewName` | `force` | `None` | `None` | `200 OK`<br>`SimpleMessage` |

---

## 10. Stored Procedures
Manages storage, updating, compiling, and executing user programmatic procedures.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/procedures` | `CreateProcedureAsync` | `None` | `None` | `None` | `CreateProcedureRequest` | `201 Created`<br>`ProcedureDetail` |
| **POST** | `/procedures/{procedureName}/execute` | `ExecuteProcedureAsync` | `procedureName` | `None` | `None` | `ExecuteProcedureRequest` | `200 OK`<br>`ProcedureResponse`|
| **PUT** | `/procedures/{procedureName}` | `UpdateProcedureAsync` | `procedureName` | `None` | `None` | `UpdateProcedureRequest` | `200 OK`<br>`ProcedureDetail` |
| **DELETE** | `/procedures/{procedureName}` | `DropProcedureAsync` | `procedureName` | `force` | `None` | `None` | `200 OK`<br>`SimpleMessage` |

---

## 11. Transaction
Exposes controls for begin, commit, rollback, and checking active transactions.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/transactions/begin` | `BeginTransactionAsync` | `None` | `isolationLevel` | `None` | `None` | `200 OK`<br>`TransactionDetail`|
| **POST** | `/transactions/commit` | `CommitTransactionAsync` | `None` | `None` | `None` | `None` | `200 OK`<br>`SimpleMessage` |
| **POST** | `/transactions/rollback` | `RollbackTransactionAsync`| `None` | `None` | `None` | `None` | `200 OK`<br>`SimpleMessage` |
| **GET** | `/transactions/active` | `GetActiveTransactionsAsync`| `None` | `sort` | `page, pageSize` | `None` | `200 OK`<br>`ActiveTxnList` |

---

## 12. Lock Manager
Manages acquisition and release of table and page row concurrency locks.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/locks/acquire` | `AcquireLockAsync` | `None` | `wait, timeoutSeconds` | `None` | `AcquireLockRequest` | `200 OK`<br>`LockDetail` |
| **POST** | `/locks/release` | `ReleaseLockAsync` | `None` | `None` | `None` | `ReleaseLockRequest` | `200 OK`<br>`SimpleMessage` |
| **GET** | `/locks` | `GetActiveLocksAsync` | `None` | `txId, resourceId, sort` | `page, pageSize` | `None` | `200 OK`<br>`ActiveLocksList` |

---

## 13. Storage Engine
Controls direct read/write of physical block pages and eviction sweeps.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/storage/pages` | `GetStoragePagesAsync` | `None` | `dirty, sort` | `page, pageSize` | `None` | `200 OK`<br>`StoragePageList` |
| **GET** | `/storage/pages/{pageId}` | `GetStoragePageDetailAsync` | `pageId` | `None` | `None` | `None` | `200 OK`<br>`StoragePageDetail` |
| **PUT** | `/storage/pages/{pageId}` | `UpdateStoragePageAsync` | `pageId` | `None` | `None` | `UpdateStoragePageRequest`| `200 OK`<br>`StoragePageDetail` |
| **POST** | `/storage/flush` | `FlushPagesToDiskAsync` | `None` | `wait` | `None` | `None` | `200 OK`<br>`SimpleMessage` |
| **POST** | `/storage/evict` | `EvictStoragePageAsync` | `None` | `policy` | `None` | `None` | `200 OK`<br>`SimpleMessage` |
| **POST** | `/storage/engine/inmemory` | `SwitchToInMemoryAsync` | `None` | `None` | `None` | `None` | `200 OK`<br>`SimpleMessage` |
| **POST** | `/storage/engine/disk` | `SwitchToDiskAsync` | `None` | `None` | `None` | `None` | `200 OK`<br>`SimpleMessage` |

---

## 14. Buffer Pool
Manages memory pool cache frames and mapping page frames.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/bufferpool/frames` | `GetBufferPoolFramesAsync` | `None` | `state, sort` | `page, pageSize` | `None` | `200 OK`<br>`BufferFramesList` |
| **POST** | `/bufferpool/fetch` | `FetchBufferPageAsync` | `None` | `pageId` | `None` | `None` | `200 OK`<br>`BufferFrameDetail` |
| **POST** | `/bufferpool/unpin` | `UnpinBufferPageAsync` | `None` | `pageId, dirty` | `None` | `None` | `200 OK`<br>`SimpleMessage` |
| **POST** | `/bufferpool/flush-dirty` | `FlushDirtyFramesAsync` | `None` | `wait` | `None` | `None` | `200 OK`<br>`SimpleMessage` |

---

## 15. File Manager
Handles low-level operations on concrete database files and folders.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/files/create` | `CreateDatabaseFileAsync` | `None` | `None` | `None` | `CreateFileRequest` | `201 Created`<br>`FileDetail` |
| **POST** | `/files/open` | `OpenDatabaseFileAsync` | `None` | `None` | `None` | `OpenFileRequest` | `200 OK`<br>`FileDescriptor` |
| **GET** | `/files/read` | `ReadBytesFromFileAsync` | `None` | `offset, size` | `None` | `None` | `200 OK`<br>`FileBytesResponse` |
| **PUT** | `/files/write` | `WriteBytesToFileAsync` | `None` | `offset` | `None` | `WriteBytesRequest` | `200 OK`<br>`SimpleMessage` |
| **DELETE** | `/files/close` | `CloseDatabaseFileAsync` | `None` | `force` | `None` | `None` | `200 OK`<br>`SimpleMessage` |

---

## 16. Recovery
Responsible for Write-Ahead Logging (WAL) parsing and crash-backups.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/recovery/backup` | `CreateBackupAsync` | `None` | `compression, wait` | `None` | `CreateBackupRequest` | `201 Created`<br>`BackupDetail` |
| **POST** | `/recovery/restore` | `RestoreFromBackupAsync` | `None` | `wait` | `None` | `RestoreBackupRequest` | `200 OK`<br>`SimpleMessage` |
| **POST** | `/recovery/recover` | `PerformCrashRecoveryAsync` | `None` | `targetLsn` | `None` | `None` | `200 OK`<br>`SimpleMessage` |
| **GET** | `/recovery/wal` | `GetWalEntriesAsync` | `None` | `startLsn, endLsn, sort`| `page, pageSize` | `None` | `200 OK`<br>`WalList` |

---

## 17. Security
Provides authentication and controls user administration roles and permissions.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/security/login` | `AuthenticateUserAsync` | `None` | `None` | `None` | `UserLoginRequest` | `200 OK`<br>`TokenResponse` |
| **POST** | `/security/logout` | `LogoutUserAsync` | `None` | `None` | `None` | `None` | `200 OK`<br>`SimpleMessage` |
| **POST** | `/security/users` | `CreateUserAccountAsync` | `None` | `None` | `None` | `CreateUserRequest` | `201 Created`<br>`UserDetail` |
| **POST** | `/security/roles` | `CreateSecurityRoleAsync` | `None` | `None` | `None` | `CreateRoleRequest` | `201 Created`<br>`RoleDetail` |
| **POST** | `/security/permissions`| `GrantPermissionsAsync` | `None` | `None` | `None` | `GrantPermissionRequest`| `200 OK`<br>`SimpleMessage` |

---

## 18. Catalog
Exposes catalog system directories and statistical analytics parameters.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/catalog/objects` | `GetCatalogObjectsAsync` | `None` | `type, name, sort` | `page, pageSize` | `None` | `200 OK`<br>`CatalogObjectList` |
| **GET** | `/catalog/statistics` | `GetCatalogStatisticsAsync` | `None` | `tableName` | `None` | `None` | `200 OK`<br>`CatalogStatsDetail` |
| **POST** | `/catalog/statistics/update`| `UpdateCatalogStatsAsync`| `None` | `tableName, wait` | `None` | `None` | `200 OK`<br>`SimpleMessage` |

---

## 19. Monitoring
Monitors memory pool caching performance counters and active configurations.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/monitoring/metrics` | `GetSystemMetricsAsync` | `None` | `category` | `None` | `None` | `200 OK`<br>`SystemMetricsDetail` |
| **GET** | `/monitoring/performance` | `GetQueryPerformanceReportAsync`| `None` | `slowQueryThresholdMs`| `None` | `None` | `200 OK`<br>`PerformanceReport` |
| **GET** | `/monitoring/bufferpool` | `GetBufferPoolUsageReportAsync`| `None` | `None` | `None` | `None` | `200 OK`<br>`BufferPoolReport` |
| **GET** | `/monitoring/transactions`| `GetTransactionUsageReportAsync`| `None` | `None` | `None` | `None` | `200 OK`<br>`TransactionReport` |

---

## 20. Diagnostics
Provides access to server error stack logs and engine tracking logs.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/diagnostics/errors` | `GetSystemErrorsAsync` | `None` | `severity, sort` | `page, pageSize` | `None` | `200 OK`<br>`ErrorLogsList` |
| **GET** | `/diagnostics/logs` | `GetDiagnosticsLogsAsync` | `None` | `level, limit` | `None` | `None` | `200 OK`<br>`LogsListResponse` |

---

## 21. Replication
Coordinates secondary databases data replication and cluster node synchronization.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/replication/nodes` | `GetReplicationNodesAsync` | `None` | `status` | `None` | `None` | `200 OK`<br>`ReplicationNodesList`|
| **POST** | `/replication/sync` | `SyncReplicaDataAsync` | `None` | `wait` | `None` | `None` | `200 OK`<br>`SimpleMessage` |
| **POST** | `/replication/nodes/add` | `AddReplicationNodeAsync` | `None` | `None` | `None` | `AddReplicationNodeRequest`| `201 Created`<br>`NodeDetail` |
| **DELETE** | `/replication/nodes/remove/{nodeId}`| `RemoveReplicationNodeAsync`| `nodeId` | `force` | `None` | `None` | `200 OK`<br>`SimpleMessage` |

---

## 22. Network
Monitors connection socket statuses and manages remote client sessions.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/network/status` | `GetNetworkStatusAsync` | `None` | `None` | `None` | `None` | `200 OK`<br>`NetworkStatusDetail` |
| **GET** | `/network/connections` | `GetActiveConnectionsAsync` | `None` | `ipAddress, sort` | `page, pageSize` | `None` | `200 OK`<br>`ConnectionList` |
| **POST** | `/network/disconnect` | `DisconnectClientSessionAsync`| `None` | `None` | `None` | `DisconnectSessionRequest`| `200 OK`<br>`SimpleMessage` |

---

## 23. Query Processor
Handles query token compilation parsing, optimizer cost mapping, and VM execution.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/query/parse` | `ParseSqlQueryAsync` | `None` | `None` | `None` | `QueryParseRequest` | `200 OK`<br>`QueryAstResponse` |
| **POST** | `/query/analyze` | `AnalyzeQueryAstAsync` | `None` | `None` | `None` | `QueryAnalyzeRequest` | `200 OK`<br>`QueryAnalyzeResponse` |
| **POST** | `/query/optimize` | `OptimizeExecutionPlanAsync` | `None` | `None` | `None` | `QueryOptimizeRequest` | `200 OK`<br>`OptimizedPlanResponse`|
| **POST** | `/query/execute` | `ExecuteQueryPlanAsync` | `None` | `explain, analyze` | `None` | `QueryExecuteRequest` | `200 OK`<br>`QueryExecuteResponse` |

---

## 24. Configuration
Reloads parameter settings and views dynamic system settings.

| Method | Endpoint | Application operation | Path parameters | Query / filters | Pagination | Request body | Response |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/config` | `GetSystemConfigurationAsync`| `None` | `section` | `None` | `None` | `200 OK`<br>`SystemConfigDetail` |
| **PUT** | `/config` | `UpdateConfigurationAsync` | `None` | `None` | `None` | `UpdateConfigRequest` | `200 OK`<br>`SystemConfigDetail` |
