# DBMS REST API Specification Document


---

## 1. Subsystem 1: Database Object Management
Manages database creation, schemas, tables, columns, constraints, indexes, views, and stored procedures.

| HTTP Method | Endpoint | Query Params | Request Body | Success Response (Code & Payload) | Error Response (Code & Payload) | Description / Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/api/v1/databases` | `None` | `{"name": "SalesDB", "owner": "admin"}` | `201 Created`<br>`{"name": "SalesDB", "status": "closed"}` | `400 Bad Request`<br>`{"detail": "Database already exists"}` | Create a new physical database catalog directory. |
| **GET** | `/api/v1/databases` | `None` | `None` | `200 OK`<br>`[{"name": "ProductionDB", "status": "open"}]` | `500 Server Error`<br>`{"detail": "Disk read failure"}` | List metadata of all registered databases. |
| **GET** | `/api/v1/databases/{db}` | `None` | `None` | `200 OK`<br>`{"name": "TestDB", "status": "closed"}` | `404 Not Found`<br>`{"detail": "Database TestDB not found"}` | Fetch details of a specific database instance. |
| **DELETE** | `/api/v1/databases/{db}` | `None` | `None` | `200 OK`<br>`{"message": "Database deleted"}` | `404 Not Found`<br>`{"detail": "Database not found"}` | Delete a database instance and release files. |
| **POST** | `/api/v1/databases/{db}/open` | `None` | `None` | `200 OK`<br>`{"name": "db", "status": "open"}` | `404 Not Found`<br>`{"detail": "Database not found"}` | Initialize connection and load memory blocks. |
| **POST** | `/api/v1/databases/{db}/close` | `None` | `None` | `200 OK`<br>`{"name": "db", "status": "closed"}` | `404 Not Found`<br>`{"detail": "Database not found"}` | Safely flush and close database descriptors. |
| **POST** | `/api/v1/databases/{db}/readonly` | `None` | `None` | `200 OK`<br>`{"name": "db", "status": "readonly"}` | `404 Not Found`<br>`{"detail": "Database not found"}` | Lock database into read-only mode. |
| **POST** | `/api/v1/databases/{db}/schemas` | `None` | `{"name": "public"}` | `201 Created`<br>`{"name": "public"}` | `400 Bad Request`<br>`{"detail": "Schema exists"}` | Create a new logical schema namespace. |
| **GET** | `/api/v1/databases/{db}/schemas` | `None` | `None` | `200 OK`<br>`[{"name": "public"}]` | `404 Not Found`<br>`{"detail": "Database not found"}` | List all schemas under the database namespace. |
| **GET** | `/api/v1/databases/{db}/schemas/{schema}`| `None` | `None` | `200 OK`<br>`{"name": "public"}` | `404 Not Found`<br>`{"detail": "Schema not found"}` | Fetch schema details. |
| **PUT** | `/api/v1/databases/{db}/schemas/{schema}`| `None` | `{"name": "public_new"}` | `200 OK`<br>`{"name": "public_new"}` | `404 Not Found`<br>`{"detail": "Schema not found"}` | Update schema namespace properties. |
| **DELETE** | `/api/v1/databases/{db}/schemas/{schema}`| `None` | `None` | `200 OK`<br>`{"message": "Deleted"}` | `404 Not Found`<br>`{"detail": "Schema not found"}` | Drop schema namespace and all child tables. |
| **POST** | `/api/v1/schemas/{schema}/tables` | `None` | `{"name": "Users", "columns": ["id"]}`| `201 Created`<br>`{"name": "Users"}` | `400 Bad Request`<br>`{"detail": "Table exists"}` | Create a new physical table file under schema. |
| **GET** | `/api/v1/schemas/{schema}/tables` | `None` | `None` | `200 OK`<br>`[{"name": "Users"}]` | `404 Not Found`<br>`{"detail": "Schema not found"}` | List all tables under the target schema. |
| **GET** | `/api/v1/schemas/{schema}/tables/{table}`| `None` | `None` | `200 OK`<br>`{"name": "Users"}` | `404 Not Found`<br>`{"detail": "Table not found"}` | Fetch table column configurations. |
| **PUT** | `/api/v1/schemas/{schema}/tables/{table}`| `None` | `{"description": "T"}` | `200 OK`<br>`{"name": "Users"}` | `404 Not Found`<br>`{"detail": "Table not found"}` | Update table metadata. |
| **DELETE** | `/api/v1/schemas/{schema}/tables/{table}`| `None` | `None` | `200 OK`<br>`{"message": "Dropped"}` | `404 Not Found`<br>`{"detail": "Table not found"}` | Drop table file and free allocated pages. |
| **POST** | `/api/v1/tables/{table}/columns` | `None` | `{"name": "age", "type": "INT"}` | `201 Created`<br>`{"name": "age"}` | `400 Bad Request`<br>`{"detail": "Column exists"}` | Add a column to table schema dynamically. |
| **GET** | `/api/v1/tables/{table}/columns` | `None` | `None` | `200 OK`<br>`[{"name": "age", "type": "INT"}]`| `404 Not Found`<br>`{"detail": "Table not found"}` | Get column metadata from catalog. |
| **PUT** | `/api/v1/tables/{table}/columns/{column}`| `None` | `{"type": "BIGINT"}` | `200 OK`<br>`{"name": "age"}` | `404 Not Found`<br>`{"detail": "Column not found"}` | Alter column datatype definition. |
| **DELETE** | `/api/v1/tables/{table}/columns/{column}`| `None` | `None` | `200 OK`<br>`{"message": "Deleted"}` | `404 Not Found`<br>`{"detail": "Column not found"}` | Drop column from table definition. |
| **POST** | `/api/v1/constraints/check` | `None` | `{"expr": "age > 18"}` | `201 Created`<br>`{"id": "c1"}` | `400 Bad Request`<br>`{"detail": "Syntax error"}` | Register a Check Constraint on a table. |
| **POST** | `/api/v1/constraints/primarykey` | `None` | `{"column": "id"}` | `201 Created`<br>`{"id": "pk"}` | `400 Bad Request`<br>`{"detail": "Invalid column"}` | Define Primary Key constraint and B-Tree index. |
| **POST** | `/api/v1/constraints/unique` | `None` | `{"column": "email"}` | `201 Created`<br>`{"id": "u1"}` | `400 Bad Request`<br>`{"detail": "Invalid column"}` | Enforce Uniqueness constraint on target column. |
| **POST** | `/api/v1/constraints/foreignkey` | `None` | `{"column": "fk", "ref": "parent.id"}`| `201 Created`<br>`{"id": "fk"}` | `400 Bad Request`<br>`{"detail": "Ref error"}` | Link tables to enforce referential integrity. |
| **PUT** | `/api/v1/constraints/{id}` | `None` | `{"expr": "age > 21"}` | `200 OK`<br>`{"id": "c1"}` | `404 Not Found`<br>`{"detail": "Constraint not found"}` | Update constraint rule conditions. |
| **DELETE** | `/api/v1/constraints/{id}` | `None` | `None` | `200 OK`<br>`{"message": "Deleted"}` | `404 Not Found`<br>`{"detail": "Constraint not found"}` | Remove constraint validation logic. |
| **POST** | `/api/v1/tables/{table}/indexes` | `None` | `{"name": "idx_col", "type": "BTREE"}`| `201 Created` | `400 Bad Request`<br>`{"detail": "Index exists"}` | Build index dynamically using Factory Method. |
| **GET** | `/api/v1/tables/{table}/indexes` | `None` | `None` | `200 OK`<br>`[{"name": "idx_col"}]` | `404 Not Found`<br>`{"detail": "Table not found"}` | List all indexes configured on the table. |
| **DELETE** | `/api/v1/tables/{table}/indexes/{index}`| `None` | `None` | `200 OK`<br>`{"message": "Dropped"}` | `404 Not Found`<br>`{"detail": "Index not found"}` | Drop index and release index file blocks. |
| **POST** | `/api/v1/tables/{table}/indexes/search` | `None` | `{"key": "val"}` | `200 OK`<br>`{"row_ids": [1, 5]}` | `400 Bad Request`<br>`{"detail": "Invalid key type"}` | Perform point query search using index. |
| **POST** | `/api/v1/tables/{table}/indexes/range-search`| `None` | `{"min": 10, "max": 20}`| `200 OK`<br>`{"row_ids": [2, 3]}` | `400 Bad Request`<br>`{"detail": "Invalid range"}` | Perform range query scan on B-Tree leaf nodes. |
| **POST** | `/api/v1/views` | `None` | `{"name": "v1", "query": "SELECT *"}`| `201 Created`<br>`{"name": "v1"}` | `400 Bad Request`<br>`{"detail": "SQL error"}` | Create view and observe source updates. |
| **GET** | `/api/v1/views` | `None` | `None` | `200 OK`<br>`[{"name": "v1"}]` | `500 Server Error` | List all catalog view templates. |
| **PUT** | `/api/v1/views/{name}` | `None` | `{"query": "SELECT id"}`| `200 OK`<br>`{"name": "v1"}` | `404 Not Found`<br>`{"detail": "View not found"}` | Update view query selection logic. |
| **DELETE** | `/api/v1/views/{name}` | `None` | `None` | `200 OK`<br>`{"message": "Dropped"}` | `404 Not Found`<br>`{"detail": "View not found"}` | Drop view definition from metadata. |
| **POST** | `/api/v1/procedures` | `None` | `{"name": "p1", "body": "BEGIN..."}` | `201 Created` | `400 Bad Request`<br>`{"detail": "Syntax error"}` | Save Stored Procedure in System Catalog. |
| **PUT** | `/api/v1/procedures/{name}` | `None` | `{"body": "NEW..."}` | `200 OK` | `404 Not Found`<br>`{"detail": "Not found"}` | Update Stored Procedure execution instructions. |
| **DELETE** | `/api/v1/procedures/{name}` | `None` | `None` | `200 OK` | `404 Not Found`<br>`{"detail": "Not found"}` | Drop Stored Procedure from System Catalog. |

---

## 2. Subsystem 2: Query Processor & SQL Compiler
Validates, compiles, optimizes, and executes incoming database queries.

| HTTP Method | Endpoint | Query Params | Request Body | Success Response (Code & Payload) | Error Response (Code & Payload) | Description / Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/api/v1/query/parse` | `None` | `{"sql": "SELECT * FROM T"}`| `200 OK`<br>`{"ast": "ASTNode"}` | `400 Bad Request`<br>`{"detail": "Syntax error"}` | Compile SQL into Abstract Syntax Tree. |
| **POST** | `/api/v1/query/analyze` | `None` | `{"ast": "ASTNode"}` | `200 OK`<br>`{"status": "valid"}` | `400 Bad Request`<br>`{"detail": "Semantic error"}` | Perform query validation and type checks. |
| **POST** | `/api/v1/query/optimize` | `None` | `{"ast": "ASTNode"}` | `200 OK`<br>`{"plan": "OptimizedPlan"}` | `500 Server Error`<br>`{"detail": "Optimization failed"}`| Parse AST and output cost-based Query Plan. |
| **POST** | `/api/v1/query/execute` | `None` | `{"plan": "Plan"}` | `200 OK`<br>`{"results": [...]}` | `400 Bad Request`<br>`{"detail": "Execution failed"}` | Execute algebraic plan via Volcano executor. |
| **POST** | `/api/v1/procedures/{name}/execute` | `None` | `{"args": []}` | `200 OK`<br>`{"results": []}` | `400 Bad Request`<br>`{"detail": "Execution failed"}` | Compile and run Stored Procedure logic. |

---

## 3. Subsystem 3: Storage Engine Management
Controls page reading, layout mapping, dirty cache tracking, and engine type switches.

| HTTP Method | Endpoint | Query Params | Request Body | Success Response (Code & Payload) | Error Response (Code & Payload) | Description / Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/api/v1/storage/pages` | `None` | `None` | `200 OK`<br>`[{"page_id": 1, "dirty": false}]`| `500 Server Error` | Inspect physical database page headers. |
| **GET** | `/api/v1/storage/pages/{id}` | `None` | `None` | `200 OK`<br>`{"page_id": 1, "bytes": "..."}` | `404 Not Found`<br>`{"detail": "Page not found"}` | Read raw byte payload of a database page block. |
| **PUT** | `/api/v1/storage/pages/{id}` | `None` | `{"bytes": "..."}` | `200 OK` | `400 Bad Request`<br>`{"detail": "Invalid page format"}` | Direct low-level storage write operation. |
| **POST** | `/api/v1/storage/flush` | `None` | `None` | `200 OK`<br>`{"message": "Pages flushed"}` | `500 Server Error`<br>`{"detail": "I/O write error"}` | Force flush all dirty buffer pages to disk. |
| **POST** | `/api/v1/storage/evict` | `None` | `None` | `200 OK` | `500 Server Error`<br>`{"detail": "No frames free"}` | Evict page using LRU/Clock-sweep strategy. |
| **POST** | `/api/v1/storage/engine/inmemory` | `None` | `None` | `200 OK` | `500 Server Error` | Switch database runtime to fully in-memory engine. |
| **POST** | `/api/v1/storage/engine/disk` | `None` | `None` | `200 OK` | `500 Server Error` | Switch database runtime to persistent disk storage. |

---

## 4. Subsystem 4: Buffer Pool Management
Handles frame allocation, page fetching/pinning, and buffer frame flushing.

| HTTP Method | Endpoint | Query Params | Request Body | Success Response (Code & Payload) | Error Response (Code & Payload) | Description / Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/api/v1/bufferpool/frames` | `None` | `None` | `200 OK`<br>`[{"frame_id": 1}]` | `500 Server Error` | Inspect buffer pool frame structures. |
| **POST** | `/api/v1/bufferpool/fetch` | `None` | `{"page_id": 5}` | `200 OK`<br>`{"frame_id": 2}` | `500 Server Error`<br>`{"detail": "Buffer pool full"}` | Pin page in buffer pool memory frame. |
| **POST** | `/api/v1/bufferpool/unpin` | `None` | `{"page_id": 5}` | `200 OK` | `404 Not Found`<br>`{"detail": "Page not pinned"}` | Unpin page frame, allowing eviction sweep. |
| **POST** | `/api/v1/bufferpool/flush-dirty` | `None` | `None` | `200 OK` | `500 Server Error`<br>`{"detail": "Disk write error"}` | Flush all dirty frames asynchronously to disk. |

---

## 5. Subsystem 5: File persistence Management
Allocates physical files, descriptors, and handles raw byte offsets writes and reads.

| HTTP Method | Endpoint | Query Params | Request Body | Success Response (Code & Payload) | Error Response (Code & Payload) | Description / Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/api/v1/files/create` | `None` | `{"filename": "t.db"}` | `201 Created` | `400 Bad Request`<br>`{"detail": "File exists"}` | Create physical storage block file on filesystem. |
| **POST** | `/api/v1/files/open` | `None` | `{"filename": "t.db"}` | `200 OK` | `404 Not Found`<br>`{"detail": "File not found"}` | Allocate system file descriptor for page writes. |
| **GET** | `/api/v1/files/read` | `None` | `{"offset": 0, "size": 4096}`| `200 OK`<br>`{"bytes": "..."}` | `400 Bad Request`<br>`{"detail": "Out of bounds"}` | Read raw bytes directly from database file. |
| **PUT** | `/api/v1/files/write` | `None` | `{"offset": 0, "bytes": "..."}`| `200 OK` | `400 Bad Request`<br>`{"detail": "Write failed"}` | Write raw bytes directly to database file. |
| **DELETE** | `/api/v1/files/close` | `None` | `{"filename": "t.db"}` | `200 OK` | `404 Not Found`<br>`{"detail": "File descriptor not open"}`| Deallocate physical file descriptor. |

---

## 6. Subsystem 6: Concurrency & Transaction Management
Enforces transaction boundaries, MVCC version tracking, and lock manager controls.

| HTTP Method | Endpoint | Query Params | Request Body | Success Response (Code & Payload) | Error Response (Code & Payload) | Description / Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/api/v1/transactions/begin` | `None` | `None` | `200 OK`<br>`{"tx_id": 101, "status": "active"}`| `500 Server Error`<br>`{"detail": "Tx allocation failed"}`| Begin a transaction and lock state. |
| **POST** | `/api/v1/transactions/commit` | `None` | `None` | `200 OK`<br>`{"status": "committed"}` | `400 Bad Request`<br>`{"detail": "Tx conflicts"}` | Commit transaction changes, logging WAL flush. |
| **POST** | `/api/v1/transactions/rollback` | `None` | `None` | `200 OK`<br>`{"status": "rolled_back"}` | `404 Not Found`<br>`{"detail": "No active Tx"}` | Rollback mutations via Undo Command stack. |
| **GET** | `/api/v1/transactions/active` | `None` | `None` | `200 OK`<br>`[101, 102]` | `500 Server Error` | Get transaction telemetry active registry. |
| **GET** | `/api/v1/mvcc/snapshots` | `None` | `None` | `200 OK`<br>`[{"tx_id": 101}]` | `500 Server Error` | Get list of active MVCC read snapshots. |
| **GET** | `/api/v1/mvcc/versions` | `None` | `{"row_id": 1}` | `200 OK`<br>`[{"tx_id": 101, "data": "v1"}]`| `404 Not Found`<br>`{"detail": "Row not found"}` | Retrieve version history of a specific row. |
| **POST** | `/api/v1/locks/acquire` | `None` | `{"table": "T", "mode": "exclusive"}`| `200 OK`<br>`{"lock_status": "acquired"}`| `409 Conflict`<br>`{"detail": "Deadlock detected"}`| Request table lock from the Lock Manager. |
| **POST** | `/api/v1/locks/release` | `None` | `{"table": "T"}` | `200 OK`<br>`{"lock_status": "released"}`| `400 Bad Request`<br>`{"detail": "Lock not held"}` | Release held lock. |
| **GET** | `/api/v1/locks` | `None` | `None` | `200 OK`<br>`[{"table": "T", "tx_id": 101}]`| `500 Server Error` | Get currently active lock registrations. |

---

## 7. Subsystem 7: Backup, Recovery, & Replication
Assures crash durability using Write-Ahead Logging, backups, and master-replica synchronization.

| HTTP Method | Endpoint | Query Params | Request Body | Success Response (Code & Payload) | Error Response (Code & Payload) | Description / Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **POST** | `/api/v1/recovery/backup` | `None` | `{"dest": "backup.sql"}`| `201 Created` | `500 Server Error`<br>`{"detail": "Backup failed"}` | Create logical database backup file. |
| **POST** | `/api/v1/recovery/restore` | `None` | `{"src": "backup.sql"}` | `200 OK` | `400 Bad Request`<br>`{"detail": "Invalid backup file"}`| Restore database catalog and rows from backup. |
| **POST** | `/api/v1/recovery/recover` | `None` | `None` | `200 OK` | `500 Server Error`<br>`{"detail": "Log corrupt"}` | Execute WAL crash recovery process. |
| **GET** | `/api/v1/recovery/wal` | `None` | `None` | `200 OK`<br>`[{"lsn": 100, "op": "INSERT"}]` | `500 Server Error` | Read WAL (Write-Ahead Log) raw records. |
| **GET** | `/api/v1/replication/nodes` | `None` | `None` | `200 OK`<br>`["node_primary", "node_replica"]`| `500 Server Error` | List primary and read-replica replication nodes. |
| **POST** | `/api/v1/replication/sync` | `None` | `None` | `200 OK` | `500 Server Error`<br>`{"detail": "Sync timed out"}` | Trigger synchronous physical replica commit. |
| **POST** | `/api/v1/replication/nodes/add` | `None` | `{"node": "replica_2"}` | `201 Created` | `400 Bad Request`<br>`{"detail": "Node exists"}` | Register new replication follower node. |
| **DELETE** | `/api/v1/replication/nodes/remove/{node}`| `None` | `None` | `200 OK` | `404 Not Found`<br>`{"detail": "Node not found"}` | De-register replication follower node. |

---

## 8. Subsystem 8: Administration, Security, & Telemetry
Handles connection socket statuses, configuration reloading, security permissions, metadata statistics, and diagnostics logging.

| HTTP Method | Endpoint | Query Params | Request Body | Success Response (Code & Payload) | Error Response (Code & Payload) | Description / Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **GET** | `/api/v1/network/status` | `None` | `None` | `200 OK`<br>`{"status": "connected"}` | `500 Server Error` | Inspect network socket listener connection health. |
| **GET** | `/api/v1/network/connections` | `None` | `None` | `200 OK`<br>`[{"client_ip": "127.0.0.1"}]`| `500 Server Error` | List active remote connection IPs. |
| **POST** | `/api/v1/network/disconnect` | `None` | `{"client_ip": "127.0.0.1"}`| `200 OK` | `404 Not Found` | Terminate and disconnect client remote connection. |
| **GET** | `/api/v1/config` | `None` | `None` | `200 OK`<br>`{"buffer_pool_size": 4096}` | `500 Server Error` | Get global config options. |
| **PUT** | `/api/v1/config` | `None` | `{"max_connections": 150}` | `200 OK` | `400 Bad Request` | Dynamic reload of engine config parameters. |
| **POST** | `/api/v1/security/login` | `None` | `{"user": "u", "pass": "p"}` | `200 OK`<br>`{"token": "xyz"}` | `401 Unauthorized`<br>`{"detail": "Invalid credentials"}`| Authenticate and fetch session token. |
| **POST** | `/api/v1/security/logout` | `None` | `None` | `200 OK` | `401 Unauthorized` | Revoke session token and terminate connection. |
| **POST** | `/api/v1/security/users` | `None` | `{"username": "dev"}` | `201 Created` | `400 Bad Request` | Create new database user account. |
| **POST** | `/api/v1/security/roles` | `None` | `{"role": "db_owner"}` | `201 Created` | `400 Bad Request` | Create new permission role container. |
| **POST** | `/api/v1/security/permissions`| `None` | `{"role": "r", "resource": "t"}` | `200 OK` | `403 Forbidden` | Set row-level or table-level permissions. |
| **GET** | `/api/v1/catalog/objects` | `None` | `None` | `200 OK`<br>`[{"name": "Users", "type": "Table"}]`| `500 Server Error` | List catalog metadata entries. |
| **GET** | `/api/v1/catalog/statistics` | `None` | `None` | `200 OK`<br>`{"avg_row_width": 24}` | `500 Server Error` | Read catalog optimization statistical data. |
| **POST** | `/api/v1/catalog/statistics/update`| `None` | `None` | `200 OK` | `500 Server Error` | Re-run catalog column distribution stats builder. |
| **GET** | `/api/v1/monitoring/metrics` | `None` | `None` | `200 OK`<br>`{"cpu_percent": 1.5}` | `500 Server Error` | Get CPU and performance metrics. |
| **GET** | `/api/v1/monitoring/performance` | `None` | `None` | `200 OK` | `500 Server Error` | Fetch execution latency breakdown report. |
| **GET** | `/api/v1/monitoring/bufferpool` | `None` | `None` | `200 OK` | `500 Server Error` | Fetch buffer pool hit ratio metrics. |
| **GET** | `/api/v1/monitoring/transactions`| `None` | `None` | `200 OK` | `500 Server Error` | Fetch transaction statistics. |
| **GET** | `/api/v1/diagnostics/errors` | `None` | `None` | `200 OK`<br>`[{"time": "...", "err": "..."}]`| `500 Server Error` | Inspect database server diagnostic error dumps. |
| **GET** | `/api/v1/diagnostics/logs` | `None` | `None` | `200 OK`<br>`["[INFO] Server started"]`| `500 Server Error` | Stream diagnostic logs from engine thread. |
