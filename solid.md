# Hướng Dẫn & Ví Dụ Chi Tiết Về Nguyên Tắc S.O.L.I.D Trong Thiết Kế DBMS Engine

Tài liệu này giải thích chi tiết bằng **tiếng Việt** các nguyên tắc thiết kế **SOLID**, đi kèm với **cách dùng, ví dụ so sánh (Bad Code vs Good Code)** và **đoạn mã Python runnable đầy đủ có hàm `if __name__ == "__main__":` cho TỪNG NGUYÊN TẮC** áp dụng vào hệ thống Quản Trị CSDL (DBMS).

---

## 📋 Mục Lục
1. [S - Single Responsibility Principle (SRP - Nguyên Tắc Đơn Trách Nhiệm)](#1-s---single-responsibility-principle-srp)
2. [O - Open/Closed Principle (OCP - Nguyên Tắc Mở--Đóng)](#2-o---openclosed-principle-ocp)
3. [L - Liskov Substitution Principle (LSP - Nguyên Tắc Thay Thế Liskov)](#3-l---liskov-substitution-principle-lsp)
4. [I - Interface Segregation Principle (ISP - Nguyên Tắc Phân Tách Interface)](#4-i---interface-segregation-principle-isp)
5. [D - Dependency Inversion Principle (DIP - Nguyên Tắc Đảo Ngược Phụ Thuộc)](#5-d---dependency-inversion-principle-dip)
6. [Kịch Bản Tổng Hợp: Xây Dựng DBMS Đạt 100% SOLID](#6-kịch-bản-tổng-hợp-xây-dựng-dbms-đạt-100-solid)

---

## 1. S - Single Responsibility Principle (SRP)
### 💡 1. Giải thích dễ hiểu:
> **Mỗi class chỉ nên có đúng 1 lý do để thay đổi (Single Responsibility).**  
> Trong DBMS, một lớp `Table` chỉ nên quản lý dữ liệu hàng trong RAM. Không nên bắt nó vừa quản lý hàng, vừa tự ghi nhật ký WAL ra tập tin, vừa mã hóa dữ liệu nhị phân xuống đĩa cứng.

### ❌ 2. Vi phạm SRP (Bad Code):
Lớp `TableManager` làm quá nhiều việc cùng lúc:

```python
# BAD CODE: SRP Violation
class TableManager:
    def __init__(self, table_name: str):
        self.table_name = table_name
        self.rows = []

    def insert_row(self, row_data: dict):
        # Task 1: Row memory allocation
        self.rows.append(row_data)
        
        # Task 2: Direct file log I/O
        with open("wal.log", "a") as log_file:
            log_file.write(f"INSERT INTO {self.table_name}: {row_data}\n")
            
        # Task 3: Direct binary storage I/O
        with open(f"{self.table_name}.db", "w") as db_file:
            db_file.write(str(self.rows))
```

### ✅ 3. Mã nguồn hoàn chỉnh tuân thủ SRP (Có hàm `main` chạy thử):

```python
"""
SRP DEMO: Single Responsibility Principle in DBMS
"""

class WalLogger:
    def __init__(self, log_path: str = "wal.log"):
        self.log_path = log_path

    def write_log(self, action: str, details: str):
        print(f"[WAL Engine] Logged action: [{action}] -> {details}")

class DiskStorage:
    def save_file(self, filename: str, content: str):
        print(f"[Disk Engine] Saved {len(content)} bytes to filename: {filename}")

class Table:
    def __init__(self, name: str, logger: WalLogger, storage: DiskStorage):
        self.name = name
        self.logger = logger
        self.storage = storage
        self.rows = []

    def insert_row(self, row_data: dict):
        # Only responsible for table row domain logic
        self.rows.append(row_data)
        self.logger.write_log("INSERT", f"Table {self.name}: {row_data}")
        self.storage.save_file(f"{self.name}.db", str(self.rows))

# Cách dùng & Thực thi thử nghiệm SRP
if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("=== 1. SRP DEMO EXECUTION ===")
    logger = WalLogger()
    storage = DiskStorage()
    users_table = Table("Users", logger, storage)

    users_table.insert_row({"id": 1, "username": "admin", "role": "SuperAdmin"})
    users_table.insert_row({"id": 2, "username": "john_doe", "role": "User"})
```

---

## 2. O - Open/Closed Principle (OCP)
### 💡 1. Giải thích dễ hiểu:
> **Cho phép mở rộng tính năng mới (Open for extension) nhưng Không được sửa mã nguồn cũ (Closed for modification).**  
> Khi bổ sung một loại Index mới (`BTreeIndex`, `HashIndex`, `BitmapIndex`), ta viết class mới kế thừa từ `BaseIndex` mà **không dùng `if-elif`** để sửa code sẵn có.

### ❌ 2. Vi phạm OCP (Bad Code):
Mỗi lần thêm Index mới lại phải sửa hàm `search`:

```python
# BAD CODE: OCP Violation
class BadIndexManager:
    def __init__(self, index_type: str):
        self.index_type = index_type

    def search(self, key: str):
        if self.index_type == "BTree":
            print(f"Searching BTree for '{key}'")
        elif self.index_type == "Hash":
            print(f"Searching Hash for '{key}'")
        elif self.index_type == "Bitmap": # Must edit existing code!
            print(f"Searching Bitmap for '{key}'")
        else:
            raise ValueError("Unsupported index!")
```

### ✅ 3. Mã nguồn hoàn chỉnh tuân thủ OCP (Có hàm `main` chạy thử):

```python
"""
OCP DEMO: Open/Closed Principle in DBMS
"""
from abc import ABC, abstractmethod
from typing import List, Any

class BaseIndex(ABC):
    def __init__(self, column_name: str):
        self.column_name = column_name

    @abstractmethod
    def search(self, key: Any) -> List[int]:
        pass

class BTreeIndex(BaseIndex):
    def search(self, key: Any) -> List[int]:
        print(f"[BTreeIndex:{self.column_name}] Navigating B-Tree nodes for key '{key}'")
        return [101, 102]

class HashIndex(BaseIndex):
    def search(self, key: Any) -> List[int]:
        print(f"[HashIndex:{self.column_name}] Hashing key '{key}' for direct O(1) lookup")
        return [201]

# Extend new Index class WITHOUT changing existing classes
class BitmapIndex(BaseIndex):
    def search(self, key: Any) -> List[int]:
        print(f"[BitmapIndex:{self.column_name}] Performing bitwise AND operation for key '{key}'")
        return [301, 302, 303]

class IndexService:
    def __init__(self):
        self.indexes: List[BaseIndex] = []

    def register_index(self, index: BaseIndex):
        self.indexes.append(index)

    def search_all(self, key: Any):
        for idx in self.indexes:
            results = idx.search(key)
            print(f"  -> {idx.__class__.__name__} matched Row IDs: {results}")

# Cách dùng & Thực thi thử nghiệm OCP
if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("=== 2. OCP DEMO EXECUTION ===")
    service = IndexService()
    service.register_index(BTreeIndex("user_id"))
    service.register_index(HashIndex("email"))
    service.register_index(BitmapIndex("status"))

    service.search_all("active_user")
```

---

## 3. L - Liskov Substitution Principle (LSP)
### 💡 1. Giải thích dễ hiểu:
> **Class con phải có thể thay thế hoàn toàn cho Class cha mà không gây hỏng logic chương trình.**  
> Nếu lớp cha `Constraint` trả về `bool` khi gọi `validate()`, thì mọi lớp con (`NotNullConstraint`, `CheckMinConstraint`) đều phải trả về `bool`, không được ném exception bất ngờ làm chết ứng dụng.

### ❌ 2. Vi phạm LSP (Bad Code):
Class con `BadNotNullConstraint` lại tự ý ném exception gây crash ứng dụng:

```python
# BAD CODE: LSP Violation
class BaseConstraint:
    def validate(self, value) -> bool:
        return True

class BadNotNullConstraint(BaseConstraint):
    def validate(self, value) -> bool:
        if value is None:
            # LSP Violation: Unexpected crash breaks program flow!
            raise RuntimeError("CRITICAL CRASH: Null value forbidden!")
        return True
```

### ✅ 3. Mã nguồn hoàn chỉnh tuân thủ LSP (Có hàm `main` chạy thử):

```python
"""
LSP DEMO: Liskov Substitution Principle in DBMS
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List

class Constraint(ABC):
    def __init__(self, column_name: str):
        self.column_name = column_name

    @abstractmethod
    def validate(self, value: Any) -> bool:
        pass

class NotNullConstraint(Constraint):
    def validate(self, value: Any) -> bool:
        return value is not None

class CheckMinConstraint(Constraint):
    def __init__(self, column_name: str, min_val: int):
        super().__init__(column_name)
        self.min_val = min_val

    def validate(self, value: Any) -> bool:
        if value is None:
            return False
        return value >= self.min_val

class ConstraintValidator:
    def __init__(self, constraints: List[Constraint]):
        self.constraints = constraints

    def validate_row(self, row_data: Dict[str, Any]) -> bool:
        for c in self.constraints:
            val = row_data.get(c.column_name)
            if not c.validate(val):
                print(f"[Constraint Fail] Rule '{c.__class__.__name__}' violated on column '{c.column_name}' with value '{val}'")
                return False
        return True

# Cách dùng & Thực thi thử nghiệm LSP
if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("=== 3. LSP DEMO EXECUTION ===")
    rules: List[Constraint] = [
        NotNullConstraint("username"),
        CheckMinConstraint("age", 18)
    ]
    validator = ConstraintValidator(rules)

    valid_row = {"username": "john_doe", "age": 20}
    invalid_row = {"username": "underage_user", "age": 15}

    print(f"Row 1 Valid: {validator.validate_row(valid_row)}")
    print(f"Row 2 Valid: {validator.validate_row(invalid_row)}")
```

---

## 4. I - Interface Segregation Principle (ISP)
### 💡 1. Giải thích dễ hiểu:
> **Nên chia Interface thành nhiều bộ tính năng nhỏ, không ép class phải chứa phương thức mà nó không sử dụng.**  
> Một bộ đọc dữ liệu Read-Only chỉ cần `IPageReader`, không hề cần các phương thức `write()` hay `flush()`.

### ❌ 2. Vi phạm ISP (Bad Code):
Interface khổng lồ `IMonolithicStorage` ép lớp Read-Only phải viết hàm `write()` và `flush()` dư thừa:

```python
# BAD CODE: ISP Violation
from abc import ABC, abstractmethod

class IMonolithicStorage(ABC):
    @abstractmethod
    def read_page(self, page_id: int): pass
    @abstractmethod
    def write_page(self, page_id: int, data: str): pass
    @abstractmethod
    def flush(self): pass

class ReadOnlyStorage(IMonolithicStorage):
    def read_page(self, page_id: int): return "Data"
    def write_page(self, page_id: int, data: str): raise NotImplementedError("Cannot write!")
    def flush(self): raise NotImplementedError("Cannot flush!")
```

### ✅ 3. Mã nguồn hoàn chỉnh tuân thủ ISP (Có hàm `main` chạy thử):

```python
"""
ISP DEMO: Interface Segregation Principle in DBMS
"""
from abc import ABC, abstractmethod

class IPageReader(ABC):
    @abstractmethod
    def read_page(self, page_id: int) -> str:
        pass

class IPageWriter(ABC):
    @abstractmethod
    def write_page(self, page_id: int, data: str) -> bool:
        pass

class IFlushable(ABC):
    @abstractmethod
    def flush(self):
        pass

# Read-only class inherits ONLY IPageReader
class FastPageReader(IPageReader):
    def read_page(self, page_id: int) -> str:
        print(f"[FastPageReader] High-speed reading Page #{page_id}")
        return f"PAGE_BINARY_DATA_{page_id}"

# Full storage engine inherits all required interfaces
class FullStorageEngine(IPageReader, IPageWriter, IFlushable):
    def read_page(self, page_id: int) -> str:
        return f"PAGE_BINARY_DATA_{page_id}"

    def write_page(self, page_id: int, data: str) -> bool:
        print(f"[FullStorageEngine] Writing data to Page #{page_id}")
        return True

    def flush(self):
        print("[FullStorageEngine] Flushing dirty buffer pages to physical disk.")

# Cách dùng & Thực thi thử nghiệm ISP
if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("=== 4. ISP DEMO EXECUTION ===")
    reader: IPageReader = FastPageReader()
    full_engine = FullStorageEngine()

    print("Reading data:", reader.read_page(101))
    full_engine.write_page(102, "NEW_PAYLOAD")
    full_engine.flush()
```

---

## 5. D - Dependency Inversion Principle (DIP)
### 💡 1. Giải thích dễ hiểu:
> **Class cấp cao không nên phụ thuộc trực tiếp vào Class cấp thấp. Cả hai phải phụ thuộc qua một Interface trừu tượng (Abstraction).**  
> Lớp nghiệp vụ `TableService` phụ thuộc vào Interface `ITableRepository`. Lớp lưu trữ cụ thể (`MemoryRepository` hoặc `FileRepository`) được truyền vào thông qua Constructor (Dependency Injection).

### ❌ 2. Vi phạm DIP (Bad Code):
`TableService` trực tiếp hardcode `SqliteRepository()`:

```python
# BAD CODE: DIP Violation
class SqliteRepository:
    def save(self, data: dict): print("[SQLite] Saved to disk.")

class BadTableService:
    def __init__(self):
        # Tightly coupled to concrete implementation!
        self.repository = SqliteRepository()
```

### ✅ 3. Mã nguồn hoàn chỉnh tuân thủ DIP (Có hàm `main` chạy thử):

```python
"""
DIP DEMO: Dependency Inversion Principle in DBMS
"""
from abc import ABC, abstractmethod
from typing import Dict, Any

class ITableRepository(ABC):
    @abstractmethod
    def save(self, table_name: str, data: Dict[str, Any]) -> bool:
        pass

class MemoryRepository(ITableRepository):
    def __init__(self):
        self.storage = {}

    def save(self, table_name: str, data: Dict[str, Any]) -> bool:
        if table_name not in self.storage:
            self.storage[table_name] = []
        self.storage[table_name].append(data)
        print(f"[MemoryRepo] Saved to RAM: {table_name} -> {data}")
        return True

class FileRepository(ITableRepository):
    def save(self, table_name: str, data: Dict[str, Any]) -> bool:
        print(f"[FileRepo] Saved JSON record to '{table_name}.json' on disk.")
        return True

# High-level class depends on ITableRepository abstraction!
class TableService:
    def __init__(self, repository: ITableRepository):
        # Dependency Injection via constructor
        self.repository = repository

    def insert_record(self, table_name: str, data: Dict[str, Any]):
        return self.repository.save(table_name, data)

# Cách dùng & Thực thi thử nghiệm DIP
if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("=== 5. DIP DEMO EXECUTION ===")
    memory_service = TableService(MemoryRepository())
    file_service = TableService(FileRepository())

    memory_service.insert_record("Products", {"id": 1, "name": "Laptop"})
    file_service.insert_record("Products", {"id": 2, "name": "Phone"})
```

---

## 6. Kịch Bản Tổng Hợp: Xây Dựng DBMS Đạt 100% SOLID

Đoạn mã Python dưới đây minh họa toàn bộ 5 nguyên tắc **SOLID** làm việc cùng nhau trong một hệ thống DBMS mini hoàn chỉnh:

```python
"""
==================================================================
  MASTER INTEGRATED DEMO - 100% S.O.L.I.D DBMS ARCHITECTURE
==================================================================
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any

# Interfaces (ISP & DIP)
class IWalLogger(ABC):
    @abstractmethod
    def log(self, action: str, message: str): pass

class IIndexEngine(ABC):
    @abstractmethod
    def index(self, row_id: int, key: Any): pass
    @abstractmethod
    def search(self, key: Any) -> List[int]: pass

class ITableRepository(ABC):
    @abstractmethod
    def save_row(self, table_name: str, row_id: int, data: Dict[str, Any]): pass

# Implementations (SRP & OCP)
class DiskWalLogger(IWalLogger):
    def log(self, action: str, message: str):
        print(f"[WAL Engine] [{action}] {message}")

class BTreeIndex(IIndexEngine):
    def __init__(self, column_name: str):
        self.column_name = column_name
        self.map: Dict[Any, List[int]] = {}

    def index(self, row_id: int, key: Any):
        if key not in self.map:
            self.map[key] = []
        self.map[key].append(row_id)
        print(f"[BTree Index:{self.column_name}] Indexed key '{key}' -> Row #{row_id}")

    def search(self, key: Any) -> List[int]:
        return self.map.get(key, [])

class MemoryRepository(ITableRepository):
    def __init__(self):
        self.db: Dict[str, List[Dict[str, Any]]] = {}

    def save_row(self, table_name: str, row_id: int, data: Dict[str, Any]):
        if table_name not in self.db:
            self.db[table_name] = []
        self.db[table_name].append(data)
        print(f"[Memory Repository] Saved Row #{row_id} into table '{table_name}'")

# Constraints Domain (LSP & OCP)
class DbConstraint(ABC):
    def __init__(self, column_name: str):
        self.column_name = column_name

    @abstractmethod
    def validate(self, value: Any) -> bool: pass

class MinValueConstraint(DbConstraint):
    def __init__(self, column_name: str, min_val: int):
        super().__init__(column_name)
        self.min_val = min_val

    def validate(self, value: Any) -> bool:
        return value is not None and value >= self.min_val

class UniqueConstraint(DbConstraint):
    def __init__(self, column_name: str):
        super().__init__(column_name)
        self.seen_values = set()

    def validate(self, value: Any) -> bool:
        if value in self.seen_values:
            return False
        self.seen_values.add(value)
        return True

# High-Level Core Table Engine (SRP & DIP)
class DbTable:
    def __init__(self, name: str, repository: ITableRepository, logger: IWalLogger):
        self.name = name
        self.repository = repository
        self.logger = logger
        self.constraints: List[DbConstraint] = []
        self.indexes: List[IIndexEngine] = []
        self.current_id = 1

    def add_constraint(self, constraint: DbConstraint):
        self.constraints.append(constraint)

    def add_index(self, index: IIndexEngine):
        self.indexes.append(index)

    def insert(self, row_data: Dict[str, Any]) -> bool:
        for constraint in self.constraints:
            val = row_data.get(constraint.column_name)
            if not constraint.validate(val):
                print(f"[ERROR] Constraint failed: '{constraint.__class__.__name__}' on column '{constraint.column_name}'")
                return False

        row_id = self.current_id
        row_data["id"] = row_id
        self.current_id += 1

        self.logger.log("INSERT", f"Table '{self.name}', Row #{row_id}")

        for idx in self.indexes:
            col_val = row_data.get(getattr(idx, "column_name", ""))
            if col_val is not None:
                idx.index(row_id, col_val)

        self.repository.save_row(self.name, row_id, row_data)
        return True

# Master Demo Execution
if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("=========================================================")
    print("   MASTER DBMS ENGINE DEMO - 100% S.O.L.I.D COMPLIANT")
    print("=========================================================\n")

    logger = DiskWalLogger()
    repo = MemoryRepository()

    users_table = DbTable(name="Users", repository=repo, logger=logger)
    users_table.add_constraint(MinValueConstraint(column_name="age", min_val=18))
    users_table.add_constraint(UniqueConstraint(column_name="email"))

    age_index = BTreeIndex(column_name="age")
    users_table.add_index(age_index)

    print("--- 1. Insert Valid Row 1 ---")
    users_table.insert({"name": "Alice", "age": 25, "email": "alice@example.com"})

    print("\n--- 2. Insert Valid Row 2 ---")
    users_table.insert({"name": "Bob", "age": 30, "email": "bob@example.com"})

    print("\n--- 3. Insert Row Violating Min Age Constraint (< 18) ---")
    users_table.insert({"name": "Charlie", "age": 15, "email": "charlie@example.com"})

    print("\n--- 4. Insert Row Violating Unique Email Constraint ---")
    users_table.insert({"name": "Duplicate Alice", "age": 22, "email": "alice@example.com"})

    print("\n--- 5. Perform Index Lookup ---")
    matched_ids = age_index.search(30)
    print(f"Row IDs matching age=30 via Index lookup: {matched_ids}")
```
