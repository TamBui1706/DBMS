# Comprehensive Guide & Implementation of S.O.L.I.D Principles in DBMS Engine Architecture

This document provides a detailed theoretical overview, anti-pattern analysis (Bad Code), refactored architectural patterns (Good Code), and **100% executable Python code** demonstrating how to apply the 5 **SOLID** object-oriented design principles to internal Database Management System (DBMS) architecture.

---

## 📋 Table of Contents
1. [S - Single Responsibility Principle (SRP)](#1-s---single-responsibility-principle-srp)
2. [O - Open/Closed Principle (OCP)](#2-o---openclosed-principle-ocp)
3. [L - Liskov Substitution Principle (LSP)](#3-l---liskov-substitution-principle-lsp)
4. [I - Interface Segregation Principle (ISP)](#4-i---interface-segregation-principle-isp)
5. [D - Dependency Inversion Principle (DIP)](#5-d---dependency-inversion-principle-dip)
6. [Integrated Master Scenario: 100% SOLID DBMS Architecture](#6-integrated-master-scenario-100-solid-dbms-architecture)

---

## 1. S - Single Responsibility Principle (SRP)
> **Definition:** A class should have one, and only one, reason to change. Each component in a DBMS must encapsulate a single responsibility.

### ❌ Violation of SRP (Bad Code)
A `TableManager` class handles multiple unrelated concerns: row lifecycle management, binary disk serialization (Disk I/O), and Write-Ahead Logging (WAL).

```python
# BAD CODE: SRP Violation
class TableManager:
    def __init__(self, table_name: str, log_file: str):
        self.table_name = table_name
        self.log_file = log_file
        self.rows = []

    def insert_row(self, row_data: dict):
        # Concern 1: Row data management
        self.rows.append(row_data)
        
        # Concern 2: Write-Ahead Logging (File I/O)
        with open(self.log_file, "a") as f:
            f.write(f"INSERT INTO {self.table_name}: {row_data}\n")
            
        # Concern 3: Binary payload serialization & storage
        binary_payload = str(self.rows).encode("utf-8")
        with open(f"{self.table_name}.db", "wb") as f:
            f.write(binary_payload)
```

### ✅ Adhering to SRP (Good Code)
Decompose into 3 decoupled classes, each with a single responsibility:
1. `Table`: Manages memory rows and table metadata.
2. `WalLogger`: Handles Write-Ahead Logging.
3. `DiskStorage`: Manages low-level binary disk persistence.

```python
# GOOD CODE: SRP Compliant
import json

class WalLogger:
    def __init__(self, log_path: str):
        self.log_path = log_path

    def append_log(self, operation: str, table_name: str, payload: dict):
        log_entry = f"[{operation}] {table_name}: {json.dumps(payload)}\n"
        print(f"[WAL Engine] Appending entry to {self.log_path}: {log_entry.strip()}")

class DiskStorage:
    def save_bytes(self, file_name: str, data: bytes):
        print(f"[Disk Engine] Persisted {len(data)} bytes to file: {file_name}")

class Table:
    def __init__(self, name: str, wal_logger: WalLogger, disk_storage: DiskStorage):
        self.name = name
        self.wal_logger = wal_logger
        self.disk_storage = disk_storage
        self.rows = []

    def insert_row(self, row_data: dict):
        # Focus strictly on row insertion domain logic
        self.rows.append(row_data)
        self.wal_logger.append_log("INSERT", self.name, row_data)
        
        # Delegate disk persistence to DiskStorage
        payload = json.dumps(self.rows).encode("utf-8")
        self.disk_storage.save_bytes(f"{self.name}.db", payload)
```

---

## 2. O - Open/Closed Principle (OCP)
> **Definition:** Software entities (classes, modules, functions) should be open for extension, but closed for modification.

### ❌ Violation of OCP (Bad Code)
Adding a new indexing strategy (e.g., `BitmapIndex` or `HashIndex`) forces modification of the core `BadIndexManager` using conditional `if-elif` blocks.

```python
# BAD CODE: OCP Violation
class BadIndexManager:
    def __init__(self, index_type: str):
        self.index_type = index_type

    def search(self, key: str):
        if self.index_type == "BTree":
            print(f"Traversing B-Tree index for key '{key}' with O(log N) depth")
        elif self.index_type == "Hash":
            print(f"Computing hash for key '{key}' with O(1) lookup")
        elif self.index_type == "Bitmap": # Forces editing pre-existing source code!
            print(f"Performing bitwise AND scan on Bitmap vector for key '{key}'")
        else:
            raise ValueError("Unsupported index type!")
```

### ✅ Adhering to OCP (Good Code)
Define an abstract `IndexEngine` base class. Adding new indexing strategies (e.g., `BitmapIndexEngine`) extends the system by inheriting from `IndexEngine` **without altering existing code**.

```python
# GOOD CODE: OCP Compliant
from abc import ABC, abstractmethod
from typing import List, Any

class IndexEngine(ABC):
    @abstractmethod
    def build(self, keys: List[Any]):
        pass

    @abstractmethod
    def search(self, key: Any) -> List[int]:
        pass

class BTreeIndexEngine(IndexEngine):
    def build(self, keys: List[Any]):
        print(f"[BTree] Building hierarchical B-Tree for {len(keys)} keys.")

    def search(self, key: Any) -> List[int]:
        print(f"[BTree] Searching B-Tree index for key '{key}'")
        return [101, 102]

class HashIndexEngine(IndexEngine):
    def build(self, keys: List[Any]):
        print(f"[Hash] Initializing hash bucket table for {len(keys)} keys.")

    def search(self, key: Any) -> List[int]:
        print(f"[Hash] Hash key lookup hash_code({key}) in O(1) time")
        return [105]

# Extending a new index engine WITHOUT MODIFYING EXISTING CODE
class BitmapIndexEngine(IndexEngine):
    def build(self, keys: List[Any]):
        print(f"[Bitmap] Constructing bit-vector for low-cardinality values.")

    def search(self, key: Any) -> List[int]:
        print(f"[Bitmap] Executing bitwise AND scan on bit-vector for key '{key}'")
        return [201, 202, 203]

class IndexService:
    def __init__(self, engine: IndexEngine):
        self.engine = engine

    def execute_search(self, key: Any):
        return self.engine.search(key)
```

---

## 3. L - Liskov Substitution Principle (LSP)
> **Definition:** Subtypes must be substitutable for their base types without altering the correctness of the program.

### ❌ Violation of LSP (Bad Code)
`BadNotNullConstraint` inherits from `BaseConstraint` but breaks the base class contract by raising an unhandled exception on `None` instead of returning a boolean.

```python
# BAD CODE: LSP Violation
class BaseConstraint:
    def validate(self, value: any) -> bool:
        return True

class BadNotNullConstraint(BaseConstraint):
    def validate(self, value: any) -> bool:
        if value is None:
            # LSP Violation: Unexpected exception breaks contract and caller expectations!
            raise RuntimeError("CRITICAL ERROR: Null value strictly forbidden!")
        return True
```

### ✅ Adhering to LSP (Good Code)
The base class `Constraint` defines a Template Method `validate()`. Derived classes (`CheckConstraint`, `PrimaryKeyConstraint`, `NotNullConstraint`) implement `check_logic()` respecting the invariants.

```python
# GOOD CODE: LSP Compliant
from abc import ABC, abstractmethod

class Constraint(ABC):
    def __init__(self, column_name: str, rule_name: str):
        self.column_name = column_name
        self.rule_name = rule_name

    def validate(self, value: any, db_context: dict = None) -> bool:
        # Common pre-validation invariant
        if value is None and not self.is_null_allowed():
            return False
        return self.check_logic(value, db_context)

    @abstractmethod
    def check_logic(self, value: any, db_context: dict) -> bool:
        pass

    def is_null_allowed(self) -> bool:
        return True

class CheckConstraint(Constraint):
    def __init__(self, column_name: str, rule_name: str, min_value: int):
        super().__init__(column_name, rule_name)
        self.min_value = min_value

    def check_logic(self, value: any, db_context: dict) -> bool:
        return value >= self.min_value

class NotNullConstraint(Constraint):
    def is_null_allowed(self) -> bool:
        return False

    def check_logic(self, value: any, db_context: dict) -> bool:
        return value is not None

# Verification function accepts any subtype safely without contract violation
def apply_table_constraints(constraints: list[Constraint], row_data: dict) -> bool:
    for constraint in constraints:
        val = row_data.get(constraint.column_name)
        if not constraint.validate(val):
            print(f"[Validation Failed] Column '{constraint.column_name}' violates rule '{constraint.rule_name}' with value '{val}'")
            return False
    return True
```

---

## 4. I - Interface Segregation Principle (ISP)
> **Definition:** Clients should not be forced to depend upon interfaces that they do not use. Split fat interfaces into smaller, cohesive contracts.

### ❌ Violation of ISP (Bad Code)
A bloated `IMonolithicStorage` forces read-only consumers to implement write, flush, and recovery operations.

```python
# BAD CODE: ISP Violation
from abc import ABC, abstractmethod

class IMonolithicStorage(ABC):
    @abstractmethod
    def read_page(self, page_id: int): pass
    @abstractmethod
    def write_page(self, page_id: int, data: bytes): pass
    @abstractmethod
    def flush_to_disk(self): pass
    @abstractmethod
    def recover_wal(self): pass

# Read-only consumer forced to implement unused operations
class ReadOnlyPageReader(IMonolithicStorage):
    def read_page(self, page_id: int):
        return f"Data of page {page_id}"
    
    def write_page(self, page_id: int, data: bytes):
        raise NotImplementedError("Read-only engine does not support writes!")
        
    def flush_to_disk(self):
        raise NotImplementedError("Flush operation not supported!")
        
    def recover_wal(self):
        raise NotImplementedError("Recovery operation not supported!")
```

### ✅ Adhering to ISP (Good Code)
Segregate storage into specialized interfaces: `IPageReader`, `IPageWriter`, and `IFlushableStorage`.

```python
# GOOD CODE: ISP Compliant
from abc import ABC, abstractmethod

class IPageReader(ABC):
    @abstractmethod
    def read_page(self, page_id: int) -> bytes: pass

class IPageWriter(ABC):
    @abstractmethod
    def write_page(self, page_id: int, data: bytes) -> bool: pass

class IFlushableStorage(ABC):
    @abstractmethod
    def flush(self): pass

# ReadOnlyReader depends solely on IPageReader
class FastPageReader(IPageReader):
    def read_page(self, page_id: int) -> bytes:
        print(f"[Storage Reader] Performing high-speed read on Page #{page_id}")
        return b"PAGE_DATA_BUFFER"

# FullDiskEngine implements all required interfaces
class FullDiskEngine(IPageReader, IPageWriter, IFlushableStorage):
    def read_page(self, page_id: int) -> bytes:
        return b"DISK_PAGE_DATA"

    def write_page(self, page_id: int, data: bytes) -> bool:
        print(f"[Disk Writer] Writing {len(data)} bytes to Page #{page_id}")
        return True

    def flush(self):
        print("[Disk Flush] Synchronizing dirty pages to physical disk.")
```

---

## 5. D - Dependency Inversion Principle (DIP)
> **Definition:** High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details; details should depend on abstractions.

### ❌ Violation of DIP (Bad Code)
High-level `TableService` directly instantiates and depends on concrete low-level `SqliteDiskRepository`.

```python
# BAD CODE: DIP Violation
class SqliteDiskRepository:
    def save_table(self, name: str, data: dict):
        print(f"[SQLite] Saving table '{name}' directly into SQLite database file.")

class BadTableService:
    def __init__(self):
        # Tightly coupled to concrete implementation
        self.repository = SqliteDiskRepository()

    def create_new_table(self, table_name: str, schema_info: dict):
        self.repository.save_table(table_name, schema_info)
```

### ✅ Adhering to DIP (Good Code)
`TableService` depends on the `ITableRepository` abstraction. Concrete implementations (`MemoryTableRepository` or `FileSystemTableRepository`) are injected via Constructor Dependency Injection.

```python
# GOOD CODE: DIP Compliant
from abc import ABC, abstractmethod

# 1. Abstraction
class ITableRepository(ABC):
    @abstractmethod
    def save_table(self, name: str, schema_info: dict) -> bool: pass

    @abstractmethod
    def find_table(self, name: str) -> dict: pass

# 2. Low-level module A
class MemoryTableRepository(ITableRepository):
    def __init__(self):
        self._memory_db = {}

    def save_table(self, name: str, schema_info: dict) -> bool:
        self._memory_db[name] = schema_info
        print(f"[MemoryRepo] Saved table '{name}' in RAM storage.")
        return True

    def find_table(self, name: str) -> dict:
        return self._memory_db.get(name)

# 3. Low-level module B
class FileSystemTableRepository(ITableRepository):
    def save_table(self, name: str, schema_info: dict) -> bool:
        print(f"[FileRepo] Persisted table schema for '{name}' to JSON file.")
        return True

    def find_table(self, name: str) -> dict:
        print(f"[FileRepo] Loaded file for table '{name}' from disk.")
        return {"name": name}

# 4. High-level module depending strictly on abstraction
class TableService:
    def __init__(self, repository: ITableRepository):
        # Constructor Dependency Injection
        self.repository = repository

    def create_table(self, name: str, columns: list[str]):
        schema_info = {"name": name, "columns": columns}
        return self.repository.save_table(name, schema_info)
```

---

## 6. Integrated Master Scenario: 100% SOLID DBMS Architecture

The standalone Python script below demonstrates the full integration of all 5 **S.O.L.I.D** principles in a miniaturized DBMS Engine (handling Table lifecycle, Write-Ahead Logging, Constraint verification, Index building, and Repository storage):

```python
"""
==================================================================
  MINI DBMS ENGINE - IMPLEMENTING 100% S.O.L.I.D DESIGN PRINCIPLES
==================================================================
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import json

# ----------------------------------------------------------------
# 1. INTERFACES (ISP & DIP)
# ----------------------------------------------------------------

class IWalLogger(ABC):
    @abstractmethod
    def log(self, action: str, details: str): pass

class IIndexEngine(ABC):
    @abstractmethod
    def index_data(self, row_id: int, key: Any): pass

    @abstractmethod
    def search(self, key: Any) -> List[int]: pass

class ITableRepository(ABC):
    @abstractmethod
    def persist_row(self, table_name: str, row_id: int, row_data: Dict[str, Any]): pass

    @abstractmethod
    def fetch_all(self, table_name: str) -> List[Dict[str, Any]]: pass

# ----------------------------------------------------------------
# 2. INFRASTRUCTURE IMPLEMENTATIONS (SRP & OCP)
# ----------------------------------------------------------------

class DiskWalLogger(IWalLogger):
    def log(self, action: str, details: str):
        print(f"[WAL-Log] ({action}) -> {details}")

class BTreeIndexEngine(IIndexEngine):
    def __init__(self, column_name: str):
        self.column_name = column_name
        self.index_map: Dict[Any, List[int]] = {}

    def index_data(self, row_id: int, key: Any):
        if key not in self.index_map:
            self.index_map[key] = []
        self.index_map[key].append(row_id)
        print(f"[BTreeIndex:{self.column_name}] Key '{key}' maps to Row #{row_id}")

    def search(self, key: Any) -> List[int]:
        return self.index_map.get(key, [])

class InMemoryTableRepository(ITableRepository):
    def __init__(self):
        self._storage: Dict[str, List[Dict[str, Any]]] = {}

    def persist_row(self, table_name: str, row_id: int, row_data: Dict[str, Any]):
        if table_name not in self._storage:
            self._storage[table_name] = []
        self._storage[table_name].append(row_data)
        print(f"[Repository] Row #{row_id} stored in table '{table_name}'.")

    def fetch_all(self, table_name: str) -> List[Dict[str, Any]]:
        return self._storage.get(table_name, [])

# ----------------------------------------------------------------
# 3. CONSTRAINTS DOMAIN (LSP & OCP)
# ----------------------------------------------------------------

class DbConstraint(ABC):
    def __init__(self, column_name: str):
        self.column_name = column_name

    @abstractmethod
    def check(self, value: Any) -> bool: pass

class CheckMinConstraint(DbConstraint):
    def __init__(self, column_name: str, min_val: int):
        super().__init__(column_name)
        self.min_val = min_val

    def check(self, value: Any) -> bool:
        return value is not None and value >= self.min_val

class UniqueConstraint(DbConstraint):
    def __init__(self, column_name: str, existing_values: set):
        super().__init__(column_name)
        self.existing_values = existing_values

    def check(self, value: Any) -> bool:
        if value in self.existing_values:
            return False
        self.existing_values.add(value)
        return True

# ----------------------------------------------------------------
# 4. CORE TABLE DOMAIN (SRP & DIP)
# ----------------------------------------------------------------

class DbTable:
    def __init__(
        self,
        name: str,
        repository: ITableRepository,
        wal_logger: IWalLogger
    ):
        self.name = name
        self.repository = repository
        self.wal_logger = wal_logger
        self.constraints: List[DbConstraint] = []
        self.indexes: List[IIndexEngine] = []
        self._auto_increment_id = 1

    def add_constraint(self, constraint: DbConstraint):
        self.constraints.append(constraint)

    def add_index(self, index_engine: IIndexEngine):
        self.indexes.append(index_engine)

    def insert(self, row_data: Dict[str, Any]) -> bool:
        # 1. Evaluate Constraints (LSP & OCP)
        for constraint in self.constraints:
            val = row_data.get(constraint.column_name)
            if not constraint.check(val):
                print(f"[ERROR] Constraint violation '{constraint.__class__.__name__}' on column '{constraint.column_name}'")
                return False

        row_id = self._auto_increment_id
        row_data["_id"] = row_id
        self._auto_increment_id += 1

        # 2. Append WAL Log (SRP)
        self.wal_logger.log("INSERT", f"Table: {self.name}, RowID: {row_id}")

        # 3. Update Indexes (OCP)
        for index in self.indexes:
            col_val = row_data.get(getattr(index, 'column_name', ''))
            if col_val is not None:
                index.index_data(row_id, col_val)

        # 4. Persist (DIP)
        self.repository.persist_row(self.name, row_id, row_data)
        return True

# ----------------------------------------------------------------
# 5. DEMO EXECUTION (RUNNING ALL PRINCIPLES)
# ----------------------------------------------------------------

if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("=========================================================")
    print("   DBMS ENGINE DEMO - 100% S.O.L.I.D DESIGN COMPLIANCE")
    print("=========================================================\n")

    # Infrastructure setup (DIP - Dependency Injection)
    logger = DiskWalLogger()
    repo = InMemoryTableRepository()

    # Table initialization
    users_table = DbTable(name="Users", repository=repo, wal_logger=logger)

    # Attach Constraints: age >= 18 (CheckMinConstraint) & Unique Email (OCP & LSP)
    users_table.add_constraint(CheckMinConstraint(column_name="age", min_val=18))
    users_table.add_constraint(UniqueConstraint(column_name="email", existing_values=set()))

    # Attach BTree Index on age column (OCP)
    age_btree_index = BTreeIndexEngine(column_name="age")
    users_table.add_index(age_btree_index)

    print("--- 1. Insert Valid Row 1 ---")
    users_table.insert({"name": "Alice", "age": 25, "email": "alice@example.com"})

    print("\n--- 2. Insert Valid Row 2 ---")
    users_table.insert({"name": "Bob", "age": 30, "email": "bob@example.com"})

    print("\n--- 3. Insert Row Violating Age Constraint (< 18) ---")
    users_table.insert({"name": "Charlie", "age": 15, "email": "charlie@example.com"})

    print("\n--- 4. Insert Row Violating Unique Email Constraint ---")
    users_table.insert({"name": "Alice Clone", "age": 22, "email": "alice@example.com"})

    print("\n--- 5. Execute Index Search ---")
    matching_ids = age_btree_index.search(30)
    print(f"Row IDs matching condition age=30 via Index lookup: {matching_ids}")
```
