# Hướng Dẫn & Mã Nguồn Áp Dụng Nguyên Tắc S.O.L.I.D Trong Hệ Quản Trị CSDL (DBMS Engine)

Tài liệu này cung cấp lý thuyết chi tiết, phân tích vi phạm và **mã nguồn Python hoàn chỉnh 100%** minh họa cách áp dụng 5 nguyên tắc thiết kế đối tượng **SOLID** vào kiến trúc nội tại của hệ thống Hệ Quản Trị CSDL (DBMS).

---

## 📋 Mục Lục
1. [S - Single Responsibility Principle (SRP)](#1-s---single-responsibility-principle-srp)
2. [O - Open/Closed Principle (OCP)](#2-o---openclosed-principle-ocp)
3. [L - Liskov Substitution Principle (LSP)](#3-l---liskov-substitution-principle-lsp)
4. [I - Interface Segregation Principle (ISP)](#4-i---interface-segregation-principle-isp)
5. [D - Dependency Inversion Principle (DIP)](#5-d---dependency-inversion-principle-dip)
6. [Kịch Bản Tổng Hợp: Kiến Trúc DBMS Đạt Chuẩn 100% SOLID](#6-kịch-bản-tổng-hợp-kiến-trúc-dbms-đạt-chuẩn-100-solid)

---

## 1. S - Single Responsibility Principle (SRP)
> **Định nghĩa:** Một class chỉ nên có một và chỉ một lý do để thay đổi (Single Reason to Change). Mỗi lớp chỉ đảm nhận đúng một trách nhiệm duy nhất trong hệ thống DBMS.

### ❌ Vi phạm SRP (Bad Code)
Một lớp `TableManager` đảm nhận quá nhiều công việc: Vừa quản lý hàng (Row), vừa tự mã hóa nhị phân đĩa (Disk I/O), vừa tự ghi Log WAL (Write-Ahead Logging).

```python
# BAD CODE: Vi phạm SRP
class TableManager:
    def __init__(self, table_name: str, log_file: str):
        self.table_name = table_name
        self.log_file = log_file
        self.rows = []

    def insert_row(self, row_data: dict):
        # Trách nhiệm 1: Logic quản lý hàng
        self.rows.append(row_data)
        
        # Trách nhiệm 2: Logic ghi Log WAL khẩn cấp (Ghi đĩa)
        with open(self.log_file, "a") as f:
            f.write(f"INSERT INTO {self.table_name}: {row_data}\n")
            
        # Trách nhiệm 3: Mã hóa và lưu trực tiếp xuống định dạng nhị phân (.db)
        binary_payload = str(self.rows).encode("utf-8")
        with open(f"{self.table_name}.db", "wb") as f:
            f.write(binary_payload)
```

### ✅ Tuân thủ SRP (Good Code)
Phân tách thành 3 lớp riêng biệt, mỗi lớp xử lý 1 nhiệm vụ độc lập:
1. `Table`: Quản lý danh sách hàng và cấu trúc bộ nhớ.
2. `WalLogger`: Chuyên trách ghi nhật ký giao dịch WAL.
3. `DiskStorage`: Chuyên trách đọc/ghi đĩa.

```python
# GOOD CODE: Tuân thủ SRP
import json

class WalLogger:
    def __init__(self, log_path: str):
        self.log_path = log_path

    def append_log(self, operation: str, table_name: str, payload: dict):
        log_entry = f"[{operation}] {table_name}: {json.dumps(payload)}\n"
        print(f"[WAL Engine] Ghi nhật ký vào {self.log_path}: {log_entry.strip()}")

class DiskStorage:
    def save_bytes(self, file_name: str, data: bytes):
        print(f"[Disk Engine] Đã ghi {len(data)} bytes xuống đĩa file: {file_name}")

class Table:
    def __init__(self, name: str, wal_logger: WalLogger, disk_storage: DiskStorage):
        self.name = name
        self.wal_logger = wal_logger
        self.disk_storage = disk_storage
        self.rows = []

    def insert_row(self, row_data: dict):
        # Chỉ tập trung vào nghiệp vụ thêm hàng
        self.rows.append(row_data)
        self.wal_logger.append_log("INSERT", self.name, row_data)
        
        # Ủy quyền lưu đĩa cho DiskStorage
        payload = json.dumps(self.rows).encode("utf-8")
        self.disk_storage.save_bytes(f"{self.name}.db", payload)
```

---

## 2. O - Open/Closed Principle (OCP)
> **Định nghĩa:** Lớp / Module phải mở cho việc mở rộng (Open for extension) nhưng đóng đối với việc chỉnh sửa mã nguồn sẵn có (Closed for modification).

### ❌ Vi phạm OCP (Bad Code)
Khi muốn thêm một chỉ mục mới (như `BitmapIndex` hoặc `HashIndex`), bắt buộc phải sửa code của lớp `IndexManager` và thêm các câu lệnh `if-elif`.

```python
# BAD CODE: Vi phạm OCP
class BadIndexManager:
    def __init__(self, index_type: str):
        self.index_type = index_type

    def search(self, key: str):
        if self.index_type == "BTree":
            print(f"Dùng thuật toán B-Tree quét key '{key}' theo đường dẫn O(log N)")
        elif self.index_type == "Hash":
            print(f"Dùng thuật toán Hash Table tra cứu key '{key}' độ phức tạp O(1)")
        elif self.index_type == "Bitmap": # Phải sửa mã nguồn sẵn có khi thêm loại Index mới!
            print(f"Dùng thuật toán Bitmap Vector quét key '{key}'")
        else:
            raise ValueError("Loại chỉ mục không hợp lệ!")
```

### ✅ Tuân thủ OCP (Good Code)
Tạo một lớp cơ sở trừu tượng `IndexEngine`. Khi muốn mở rộng thêm chỉ mục mới (ví dụ `BitmapIndexEngine`), ta tạo lớp mới kế thừa từ `IndexEngine` mà **không cần sửa đổi một dòng code nào** của lớp quản lý hay các Index cũ.

```python
# GOOD CODE: Tuân thủ OCP
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
        print(f"[BTree] Xây dựng cây B-Tree phân cấp với {len(keys)} khóa.")

    def search(self, key: Any) -> List[int]:
        print(f"[BTree] Quét nhánh cây tìm khóa '{key}'")
        return [101, 102]

class HashIndexEngine(IndexEngine):
    def build(self, keys: List[Any]):
        print(f"[Hash] Khởi tạo bảng băm Hash Table cho {len(keys)} khóa.")

    def search(self, key: Any) -> List[int]:
        print(f"[Hash] Tính giá trị hash_code({key}) tra bảng trực tiếp O(1)")
        return [105]

# Mở rộng loại Index mới mà KHÔNG CẦN SỬA CODE CŨ
class BitmapIndexEngine(IndexEngine):
    def build(self, keys: List[Any]):
        print(f"[Bitmap] Xây dựng mảng bit (Bit Vector) cho dữ liệu cardinality thấp.")

    def search(self, key: Any) -> List[int]:
        print(f"[Bitmap] Thực hiện phép toán AND trên bit-vector cho khóa '{key}'")
        return [201, 202, 203]

class IndexService:
    def __init__(self, engine: IndexEngine):
        self.engine = engine

    def execute_search(self, key: Any):
        return self.engine.search(key)
```

---

## 3. L - Liskov Substitution Principle (LSP)
> **Định nghĩa:** Các đối tượng của lớp con phải có thể thay thế hoàn toàn cho các đối tượng của lớp cha mà không làm ảnh hưởng đến tính đúng đắn của chương trình.

### ❌ Vi phạm LSP (Bad Code)
Một `NotNullConstraint` kế thừa từ `Constraint` nhưng lại tự ý thay đổi hành vi và ném lỗi bất ngờ khi gặp giá trị `None` thay vì trả về kết quả `bool` như cam kết của lớp cha.

```python
# BAD CODE: Vi phạm LSP
class BaseConstraint:
    def validate(self, value: any) -> bool:
        return True

class BadNotNullConstraint(BaseConstraint):
    def validate(self, value: any) -> bool:
        if value is None:
            # Vi phạm LSP: Ném exception làm sụp đổ chương trình thay vì tuân thủ hợp đồng bool trả về!
            raise RuntimeError("CRITICAL ERROR: Null value strictly forbidden!")
        return True
```

### ✅ Tuân thủ LSP (Good Code)
Lớp cha `Constraint` định nghĩa Template Method `validate()`. Các lớp con (`CheckConstraint`, `PrimaryKeyConstraint`, `NotNullConstraint`) thực thi `check_logic()` tuân thủ đúng định dạng trả về mà không phá vỡ kỳ vọng của caller.

```python
# GOOD CODE: Tuân thủ LSP
from abc import ABC, abstractmethod

class Constraint(ABC):
    def __init__(self, column_name: str, rule_name: str):
        self.column_name = column_name
        self.rule_name = rule_name

    def validate(self, value: any, db_context: dict = None) -> bool:
        # Pre-processing thống nhất cho mọi ràng buộc
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

# Hàm kiểm tra chấp nhận mọi lớp con mà không bị vỡ logic
def apply_table_constraints(constraints: list[Constraint], row_data: dict) -> bool:
    for constraint in constraints:
        val = row_data.get(constraint.column_name)
        if not constraint.validate(val):
            print(f"[Validation Failed] Cột '{constraint.column_name}' vi phạm quy tắc '{constraint.rule_name}' với giá trị '{val}'")
            return False
    return True
```

---

## 4. I - Interface Segregation Principle (ISP)
> **Định nghĩa:** Thay vì dùng một Interface khổng lồ phục vụ nhiều mục đích, nên tách thành nhiều Interface nhỏ và cụ thể hơn. Client không nên bị ép phụ thuộc vào các method mà nó không sử dụng.

### ❌ Vi phạm ISP (Bad Code)
Gộp chung đọc, ghi, xả đĩa (flush), khôi phục (recovery) và băm chỉ mục vào 1 Interface `IMonolithicStorage`.

```python
# BAD CODE: Vi phạm ISP
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

# Một Reader chỉ cần đọc dữ liệu nhưng vẫn bị ép phải implement các hàm write, flush, recover dư thừa
class ReadOnlyPageReader(IMonolithicStorage):
    def read_page(self, page_id: int):
        return f"Data of page {page_id}"
    
    def write_page(self, page_id: int, data: bytes):
        raise NotImplementedError("Lớp này chỉ đọc, không hỗ trợ ghi!")
        
    def flush_to_disk(self):
        raise NotImplementedError("Không hỗ trợ flush!")
        
    def recover_wal(self):
        raise NotImplementedError("Không hỗ trợ recovery!")
```

### ✅ Tuân thủ ISP (Good Code)
Phân chia thành các interface nhỏ chuyên biệt: `IPageReader`, `IPageWriter`, `IFlushableStorage`.

```python
# GOOD CODE: Tuân thủ ISP
from abc import ABC, abstractmethod

class IPageReader(ABC):
    @abstractmethod
    def read_page(self, page_id: int) -> bytes: pass

class IPageWriter(ABC):
    @abstractmethod
    def write_page(self, page_id: int, data: bytes) -> bool: pass

class IFlushableStorage(ABC):
    @abstractmethod
    def flush((self): pass

# Lớp ReadOnlyReader chỉ tuân thủ IPageReader
class FastPageReader(IPageReader):
    def read_page(self, page_id: int) -> bytes:
        print(f"[Storage Reader] Đọc dữ liệu nhanh từ Page #{page_id}")
        return b"PAGE_DATA_BUFFER"

# Lớp FullDiskEngine tuân thủ cả 3 Interface
class FullDiskEngine(IPageReader, IPageWriter, IFlushableStorage):
    def read_page(self, page_id: int) -> bytes:
        return b"DISK_PAGE_DATA"

    def write_page(self, page_id: int, data: bytes) -> bool:
        print(f"[Disk Writer] Ghi {len(data)} bytes vào Page #{page_id}")
        return True

    def flush(self):
        print("[Disk Flush] Đồng bộ tất cả Dirty Pages xuống đĩa cứng.")
```

---

## 5. D - Dependency Inversion Principle (DIP)
> **Định nghĩa:**
> 1. Các module cấp cao (High-level modules) không nên phụ thuộc vào các module cấp thấp (Low-level modules). Cả hai nên phụ thuộc vào sự trừu tượng (Abstractions).
> 2. Sự trừu tượng không nên phụ thuộc vào chi tiết. Chi tiết nên phụ thuộc vào sự trừu tượng.

### ❌ Vi phạm DIP (Bad Code)
Module cấp cao `TableService` trực tiếp khơi tạo và phụ thuộc cứng vào lớp cấp thấp `SqliteDiskRepository`. Nếu muốn đổi sang `InMemoryRepository` hay `PostgresRepository`, ta phải sửa đổi code của `TableService`.

```python
# BAD CODE: Vi phạm DIP
class SqliteDiskRepository:
    def save_table(self, name: str, data: dict):
        print(f"[SQLite] Lưu bảng '{name}' trực tiếp vào file SQLite database.")

class BadTableService:
    def __init__(self):
        # Trực tiếp phụ thuộc vào triển khai cụ thể (Concretisation)
        self.repository = SqliteDiskRepository()

    def create_new_table(self, table_name: str, schema_info: dict):
        self.repository.save_table(table_name, schema_info)
```

### ✅ Tuân thủ DIP (Good Code)
`TableService` phụ thuộc vào Interface trừu tượng `ITableRepository`. Việc lựa chọn lưu trên Đĩa (`DiskTableRepository`) hay Bộ nhớ (`InMemoryTableRepository`) sẽ được tiêm vào (Dependency Injection) từ bên ngoài.

```python
# GOOD CODE: Tuân thủ DIP
from abc import ABC, abstractmethod

# 1. Interface trừu tượng (Abstraction)
class ITableRepository(ABC):
    @abstractmethod
    def save_table(self, name: str, schema_info: dict) -> bool: pass

    @abstractmethod
    def find_table(self, name: str) -> dict: pass

# 2. Chi tiết triển khai cấp thấp 1 (Low-level module A)
class MemoryTableRepository(ITableRepository):
    def __init__(self):
        self._memory_db = {}

    def save_table(self, name: str, schema_info: dict) -> bool:
        self._memory_db[name] = schema_info
        print(f"[MemoryRepo] Đã lưu bảng '{name}' vào RAM Storage.")
        return True

    def find_table(self, name: str) -> dict:
        return self._memory_db.get(name)

# 3. Chi tiết triển khai cấp thấp 2 (Low-level module B)
class FileSystemTableRepository(ITableRepository):
    def save_table(self, name: str, schema_info: dict) -> bool:
        print(f"[FileRepo] Đã ghi cấu trúc bảng '{name}' xuống tập tin JSON đĩa.")
        return True

    def find_table(self, name: str) -> dict:
        print(f"[FileRepo] Đọc file bảng '{name}' từ đĩa cứng.")
        return {"name": name}

# 4. Module cấp cao (High-level module) chỉ phụ thuộc vào Abstraction
class TableService:
    def __init__(self, repository: ITableRepository):
        # Dependency Injection (DI) qua Constructor
        self.repository = repository

    def create_table(self, name: str, columns: list[str]):
        schema_info = {"name": name, "columns": columns}
        return self.repository.save_table(name, schema_info)
```

---

## 6. Kịch Bản Tổng Hợp: Kiến Trúc DBMS Đạt Chuẩn 100% SOLID

Dưới đây là mã nguồn Python độc lập, minh họa sự phối hợp hoàn hảo của cả 5 nguyên tắc **S.O.L.I.D** trong một hệ thống DBMS thu nhỏ (gồm tạo bảng, ghi log WAL, áp dụng ràng buộc Constraint, tạo chỉ mục Index, và lưu trữ thông qua Repository):

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
# 2. IMPLEMENTATIONS OF INFRASTRUCTURE (SRP & OCP)
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
        print(f"[BTreeIndex:{self.column_name}] Khóa '{key}' trỏ tới Row #{row_id}")

    def search(self, key: Any) -> List[int]:
        return self.index_map.get(key, [])

class InMemoryTableRepository(ITableRepository):
    def __init__(self):
        self._storage: Dict[str, List[Dict[str, Any]]] = {}

    def persist_row(self, table_name: str, row_id: int, row_data: Dict[str, Any]):
        if table_name not in self._storage:
            self._storage[table_name] = []
        self._storage[table_name].append(row_data)
        print(f"[Repository] Đã lưu Row #{row_id} vào bảng '{table_name}'.")

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
        # 1. Check Constraints (LSP & OCP)
        for constraint in self.constraints:
            val = row_data.get(constraint.column_name)
            if not constraint.check(val):
                print(f"[ERROR] Vi phạm ràng buộc '{constraint.__class__.__name__}' tại cột '{constraint.column_name}'")
                return False

        row_id = self._auto_increment_id
        row_data["_id"] = row_id
        self._auto_increment_id += 1

        # 2. Log WAL (SRP)
        self.wal_logger.log("INSERT", f"Table: {self.name}, RowID: {row_id}")

        # 3. Index data (OCP)
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
    print("   DEMO HỆ THỐNG DBMS CHẠY THEO CHUẨN S.O.L.I.D")
    print("=========================================================\n")


    # Khởi tạo hạ tầng (DIP - Dependency Injection)
    logger = DiskWalLogger()
    repo = InMemoryTableRepository()

    # Khởi tạo bảng Users
    users_table = DbTable(name="Users", repository=repo, wal_logger=logger)

    # Thêm ràng buộc tuổi >= 18 (CheckMinConstraint) và Email Unique (OCP & LSP)
    users_table.add_constraint(CheckMinConstraint(column_name="age", min_val=18))
    users_table.add_constraint(UniqueConstraint(column_name="email", existing_values=set()))

    # Thêm chỉ mục BTree trên cột age (OCP)
    age_btree_index = BTreeIndexEngine(column_name="age")
    users_table.add_index(age_btree_index)

    print("--- 1. Thêm hàng hợp lệ 1 ---")
    users_table.insert({"name": "Alice", "age": 25, "email": "alice@example.com"})

    print("\n--- 2. Thêm hàng hợp lệ 2 ---")
    users_table.insert({"name": "Bob", "age": 30, "email": "bob@example.com"})

    print("\n--- 3. Thêm hàng vi phạm ràng buộc tuổi (< 18) ---")
    users_table.insert({"name": "Charlie", "age": 15, "email": "charlie@example.com"})

    print("\n--- 4. Thêm hàng vi phạm trùng lặp Email (Unique) ---")
    users_table.insert({"name": "Alice Clone", "age": 22, "email": "alice@example.com"})

    print("\n--- 5. Thực hiện tra cứu qua Index ---")
    matching_ids = age_btree_index.search(30)
    print(f"Các Row ID khớp với điều kiện age=30 qua Index: {matching_ids}")
```
