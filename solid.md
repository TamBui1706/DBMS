# Hướng Dẫn & Ví Dụ Dễ Hiểu Về Nguyên Tắc S.O.L.I.D Trong Thiết Kế DBMS

Tài liệu này giải thích chi tiết bằng **tiếng Việt** các nguyên tắc thiết kế **SOLID**, đi kèm với **mã nguồn Python chuẩn bằng tiếng Anh** áp dụng trực tiếp vào hệ thống Quản Trị CSDL (DBMS).

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
### 💡 Giải thích dễ hiểu:
> **Mỗi class chỉ nên làm ĐÚNG 1 VIỆC duy nhất.**  
> Ví dụ: Bạn không nên bắt một lớp `Table` vừa lưu trữ dữ liệu hàng trong RAM, vừa ghi log nhật ký (WAL) ra tập tin, vừa mã hóa dữ liệu xuống đĩa cứng. Nếu sau này cách ghi log hay cách lưu đĩa thay đổi, bạn phải sửa lớp `Table` - điều đó rất dễ gây ra lỗi dây chuyền.

### ❌ Vi phạm SRP (Bad Code)
Một class `TableManager` ôm đồm cả 3 việc: quản lý hàng, ghi log nhật ký, và ghi file đĩa.

```python
# BAD CODE: SRP Violation
class TableManager:
    def __init__(self, table_name: str):
        self.table_name = table_name
        self.rows = []

    def insert_row(self, row_data: dict):
        # Task 1: Manage row memory
        self.rows.append(row_data)
        
        # Task 2: Log write-ahead entry directly to file
        with open("wal.log", "a") as log_file:
            log_file.write(f"INSERT INTO {self.table_name}: {row_data}\n")
            
        # Task 3: Save binary data to storage file
        with open(f"{self.table_name}.db", "w") as db_file:
            db_file.write(str(self.rows))
```

### ✅ Tuân thủ SRP (Good Code)
Tách thành 3 class riêng biệt, mỗi class làm đúng 1 việc:
1. `Table`: Chỉ quản lý dữ liệu hàng trong bộ nhớ.
2. `WalLogger`: Chỉ làm nhiệm vụ ghi log.
3. `DiskStorage`: Chỉ làm nhiệm vụ ghi đĩa.

```python
# GOOD CODE: SRP Compliant
class WalLogger:
    def __init__(self, log_path: str = "wal.log"):
        self.log_path = log_path

    def write_log(self, action: str, details: str):
        print(f"[WAL Engine] Logged: [{action}] {details}")

class DiskStorage:
    def save_file(self, filename: str, content: str):
        print(f"[Disk Engine] Saved file: {filename}")

class Table:
    def __init__(self, name: str, logger: WalLogger, storage: DiskStorage):
        self.name = name
        self.logger = logger
        self.storage = storage
        self.rows = []

    def insert_row(self, row_data: dict):
        self.rows.append(row_data)
        self.logger.write_log("INSERT", f"Table {self.name}: {row_data}")
        self.storage.save_file(f"{self.name}.db", str(self.rows))
```

---

## 2. O - Open/Closed Principle (OCP)
### 💡 Giải thích dễ hiểu:
> **Thêm tính năng mới bằng cách MỞ RỘNG (viết thêm class mới), KHÔNG ĐƯỢC SỬA CODE CŨ.**  
> Ví dụ: Hệ thống DBMS hỗ trợ tạo chỉ mục (Index). Hôm nay dùng `BTreeIndex`, hôm sau muốn thêm `HashIndex` hoặc `BitmapIndex`, ta chỉ việc tạo thêm class `BitmapIndex` mới kế thừa từ `BaseIndex`. Ta **không được dùng câu lệnh `if-elif`** để sửa code cũ của hệ thống.

### ❌ Vi phạm OCP (Bad Code)
Mỗi lần thêm loại Index mới lại phải vào sửa hàm `search` và thêm `if-elif`.

```python
# BAD CODE: OCP Violation
class BadIndexManager:
    def __init__(self, index_type: str):
        self.index_type = index_type

    def search(self, key: str):
        if self.index_type == "BTree":
            print(f"Searching with BTree Index for key '{key}'")
        elif self.index_type == "Hash":
            print(f"Searching with Hash Index for key '{key}'")
        elif self.index_type == "Bitmap": # Editing existing code when adding new features!
            print(f"Searching with Bitmap Index for key '{key}'")
        else:
            raise ValueError("Unsupported index type!")
```

### ✅ Tuân thủ OCP (Good Code)
Tạo 1 class cha trừu tượng `BaseIndex`. Muốn có Index nào thì tạo class con cho Index đó. Code quản lý sẽ gọi qua class cha mà không bao giờ cần sửa đổi.

```python
# GOOD CODE: OCP Compliant
from abc import ABC, abstractmethod

class BaseIndex(ABC):
    @abstractmethod
    def search(self, key: str) -> list:
        pass

class BTreeIndex(BaseIndex):
    def search(self, key: str) -> list:
        print(f"[BTreeIndex] Navigating B-Tree nodes for key '{key}'")
        return [1, 2]

class HashIndex(BaseIndex):
    def search(self, key: str) -> list:
        print(f"[HashIndex] Hashing key '{key}' for direct O(1) lookup")
        return [3]

# Extend a new index WITHOUT changing existing classes!
class BitmapIndex(BaseIndex):
    def search(self, key: str) -> list:
        print(f"[BitmapIndex] Performing bitwise AND operation for key '{key}'")
        return [4, 5]
```

---

## 3. L - Liskov Substitution Principle (LSP)
### 💡 Giải thích dễ hiểu:
> **Class con phải thay thế được Class cha mà không làm hỏng chương trình.**  
> Ví dụ: Class cha `Constraint` có phương thức `validate(value)` trả về `True` hoặc `False`. Class con `NotNullConstraint` hoặc `CheckMinConstraint` phải tuân thủ đúng việc trả về `True/False`, không được tự ý tung ra ngoại lệ `RuntimeError` gây treo ứng dụng khi gặp dữ liệu không hợp lệ.

### ❌ Vi phạm LSP (Bad Code)
Class con `BadNotNullConstraint` lại ném exception bất ngờ làm chết chương trình thay vì trả về `False`.

```python
# BAD CODE: LSP Violation
class BaseConstraint:
    def validate(self, value) -> bool:
        return True

class BadNotNullConstraint(BaseConstraint):
    def validate(self, value) -> bool:
        if value is None:
            # LSP Violation: Unexpected crash breaks program flow!
            raise RuntimeError("Crash! Null value is forbidden!")
        return True
```

### ✅ Tuân thủ LSP (Good Code)
Tất cả các class con (`NotNullConstraint`, `CheckMinConstraint`) đều trả về kết quả `bool` đồng nhất và đúng hợp đồng của class cha.

```python
# GOOD CODE: LSP Compliant
from abc import ABC, abstractmethod

class Constraint(ABC):
    @abstractmethod
    def validate(self, value) -> bool:
        pass

class NotNullConstraint(Constraint):
    def validate(self, value) -> bool:
        return value is not None

class CheckMinConstraint(Constraint):
    def __init__(self, min_val: int):
        self.min_val = min_val

    def validate(self, value) -> bool:
        if value is None:
            return False
        return value >= self.min_val

# Safe execution function accepting any subclass
def check_all_constraints(constraints: list[Constraint], data: dict) -> bool:
    for constraint in constraints:
        if not constraint.validate(data.get("age")):
            print("[Constraint Check] Validation failed safely returning False!")
            return False
    return True
```

---

## 4. I - Interface Segregation Principle (ISP)
### 💡 Giải thích dễ hiểu:
> **Chia nhỏ Interface thành nhiều bộ tính năng chuyên biệt, không ép class phải chứa phương thức dư thừa.**  
> Ví dụ: Đừng tạo 1 Interface `Storage` quá to chứa cả `read()`, `write()`, `flush()`, `backup()`. Một bộ đọc dữ liệu Read-Only chỉ cần `IPageReader`, không hề cần hàm `write()` hay `backup()`.

### ❌ Vi phạm ISP (Bad Code)
Một Interface `IMonolithicStorage` khổng lồ bắt bộ đọc Read-Only phải viết hàm `write()` và `flush()`.

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
    def read_page(self, page_id: int):
        return f"Page Data #{page_id}"

    # Forced to implement useless methods!
    def write_page(self, page_id: int, data: str):
        raise NotImplementedError("Read-Only engine cannot write!")

    def flush(self):
        raise NotImplementedError("Read-Only engine cannot flush!")
```

### ✅ Tuân thủ ISP (Good Code)
Tách thành các Interface nhỏ gọn: `IPageReader`, `IPageWriter`, `IFlushable`.

```python
# GOOD CODE: ISP Compliant
from abc import ABC, abstractmethod

class IPageReader(ABC):
    @abstractmethod
    def read_page(self, page_id: int) -> str: pass

class IPageWriter(ABC):
    @abstractmethod
    def write_page(self, page_id: int, data: str) -> bool: pass

# Read-only class only inherits what it needs!
class FastPageReader(IPageReader):
    def read_page(self, page_id: int) -> str:
        print(f"[Reader] Reading page #{page_id}")
        return "PAGE_CONTENT"

# Full storage class inherits all required interfaces
class FullStorageEngine(IPageReader, IPageWriter):
    def read_page(self, page_id: int) -> str:
        return "PAGE_CONTENT"

    def write_page(self, page_id: int, data: str) -> bool:
        print(f"[Writer] Writing data to page #{page_id}")
        return True
```

---

## 5. D - Dependency Inversion Principle (DIP)
### 💡 Giải thích dễ hiểu:
> **Class cấp cao không được phụ thuộc trực tiếp vào Class cấp thấp. Cả hai phải phụ thuộc qua một Interface trừu tượng.**  
> Ví dụ: Lớp nghiệp vụ `TableService` không được hardcode trực tiếp `SqliteRepository()`. Hãy truyền qua Interface `ITableRepository`. Khi cần chuyển từ lưu tập tin sang lưu RAM, ta chỉ việc truyền `MemoryRepository` vào mà không phải sửa code của `TableService`.

### ❌ Vi phạm DIP (Bad Code)
`TableService` trực tiếp khởi tạo và phụ thuộc cứng vào `SqliteRepository`.

```python
# BAD CODE: DIP Violation
class SqliteRepository:
    def save(self, data: dict):
        print("[SQLite] Saved data to disk file.")

class BadTableService:
    def __init__(self):
        # Tightly coupled to concrete implementation!
        self.repository = SqliteRepository()

    def create_row(self, data: dict):
        self.repository.save(data)
```

### ✅ Tuân thủ DIP (Good Code)
`TableService` phụ thuộc vào Interface `ITableRepository`. Lớp lưu trữ cụ thể được truyền vào thông qua Constructor (Dependency Injection).

```python
# GOOD CODE: DIP Compliant
from abc import ABC, abstractmethod

class ITableRepository(ABC):
    @abstractmethod
    def save(self, data: dict) -> bool: pass

class MemoryRepository(ITableRepository):
    def save(self, data: dict) -> bool:
        print("[MemoryRepo] Saved data into RAM storage.")
        return True

class FileRepository(ITableRepository):
    def save(self, data: dict) -> bool:
        print("[FileRepo] Saved data into JSON file on disk.")
        return True

# High-level class depends on abstraction!
class TableService:
    def __init__(self, repository: ITableRepository):
        # Dependency Injection via constructor
        self.repository = repository

    def create_row(self, data: dict):
        return self.repository.save(data)
```

---

## 6. Kịch Bản Tổng Hợp: Xây Dựng DBMS Đạt 100% SOLID

Đoạn mã Python dưới đây minh họa toàn bộ 5 nguyên tắc **SOLID** hoạt động gắn kết với nhau trong một hệ thống DBMS thu nhỏ:

```python
"""
==================================================================
  MINI DBMS ENGINE - IMPLEMENTING 100% S.O.L.I.D DESIGN PRINCIPLES
==================================================================
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any

# ----------------------------------------------------------------
# 1. INTERFACES (ISP & DIP)
# ----------------------------------------------------------------

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

# ----------------------------------------------------------------
# 2. CONCRETE IMPLEMENTATIONS (SRP & OCP)
# ----------------------------------------------------------------

class DiskWalLogger(IWalLogger):
    def log(self, action: str, message: str):
        print(f"[WAL Engine] Logged action: [{action}] {message}")

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

# ----------------------------------------------------------------
# 3. CONSTRAINTS DOMAIN (LSP & OCP)
# ----------------------------------------------------------------

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

# ----------------------------------------------------------------
# 4. HIGH-LEVEL CORE TABLE (SRP & DIP)
# ----------------------------------------------------------------

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
        # 1. Validate Constraints (LSP & OCP)
        for constraint in self.constraints:
            val = row_data.get(constraint.column_name)
            if not constraint.validate(val):
                print(f"[ERROR] Constraint failed: '{constraint.__class__.__name__}' on column '{constraint.column_name}'")
                return False

        row_id = self.current_id
        row_data["id"] = row_id
        self.current_id += 1

        # 2. Write Log (SRP)
        self.logger.log("INSERT", f"Table '{self.name}', Row #{row_id}")

        # 3. Build Index (OCP)
        for idx in self.indexes:
            col_val = row_data.get(getattr(idx, "column_name", ""))
            if col_val is not None:
                idx.index(row_id, col_val)

        # 4. Save to Repository (DIP)
        self.repository.save_row(self.name, row_id, row_data)
        return True

# ----------------------------------------------------------------
# 5. DEMO EXECUTION
# ----------------------------------------------------------------

if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("=========================================================")
    print("   DBMS ENGINE DEMO - 100% S.O.L.I.D COMPLIANT")
    print("=========================================================\n")

    # Dependency Injection (DIP)
    logger = DiskWalLogger()
    repo = MemoryRepository()

    # Table setup
    users_table = DbTable(name="Users", repository=repo, logger=logger)

    # Attach Constraints (LSP & OCP)
    users_table.add_constraint(MinValueConstraint(column_name="age", min_val=18))
    users_table.add_constraint(UniqueConstraint(column_name="email"))

    # Attach Index (OCP)
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
