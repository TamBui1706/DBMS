import re

# ================== 1. DPSuggest.md ==================
with open('DPSuggest.md', 'r', encoding='utf-8') as f:
    dp = f.read()

dp_content = """

---

## 18. Decorator Pattern: Dynamic Table Wrappers (Medium Priority)

*   **Why choose Decorator?**
    Sometimes we need to add temporary responsibilities to a Table without modifying its underlying class or affecting other instances. For example, during a live database backup, a specific table needs to be strictly Read-Only. Using inheritance (`ReadOnlyTable`) is static and inflexible. The Decorator pattern allows us to wrap the original `Table` object dynamically at runtime with a `ReadOnlyDecorator`, intercepting calls to `insert()` or `update()`.

### Class Diagram
```mermaid
classDiagram
    class ITable {
        <<interface>>
        +insert(row)*
        +get_name()* String
    }
    class ConcreteTable {
        +insert(row)
        +get_name() String
    }
    
    class TableDecorator {
        <<abstract>>
        #ITable wrapped_table
        +insert(row)
        +get_name() String
    }
    class ReadOnlyDecorator {
        +insert(row)
    }
    class AuditingDecorator {
        +insert(row)
    }
    
    ITable <|.. ConcreteTable
    ITable <|.. TableDecorator
    TableDecorator o-- ITable : wraps
    TableDecorator <|-- ReadOnlyDecorator
    TableDecorator <|-- AuditingDecorator
```

### Sequence Diagram
```mermaid
sequenceDiagram
    actor Engine
    participant Dec as ReadOnlyDecorator
    participant Tbl as ConcreteTable
    
    Engine->>Dec: insert(row)
    activate Dec
    Note over Dec: Intercepts request
    Dec-->>Engine: throws Exception("Table is Read-Only!")
    deactivate Dec
    
    Engine->>Dec: get_name()
    activate Dec
    Dec->>Tbl: get_name()
    Tbl-->>Dec: "users"
    Dec-->>Engine: "users"
    deactivate Dec
```

### TDD Code Example
```python
from abc import ABC, abstractmethod

class ITable(ABC):
    @abstractmethod
    def insert(self, row): pass
    @abstractmethod
    def get_name(self): pass

class ConcreteTable(ITable):
    def __init__(self, name):
        self.name = name
    def insert(self, row):
        print(f"Table '{self.name}': Successfully inserted {row}")
    def get_name(self):
        return self.name

# Base Decorator
class TableDecorator(ITable):
    def __init__(self, table: ITable):
        self.wrapped = table
    def insert(self, row):
        self.wrapped.insert(row)
    def get_name(self):
        return self.wrapped.get_name()

# Concrete Decorators
class ReadOnlyDecorator(TableDecorator):
    def insert(self, row):
        raise PermissionError(f"DENIED: Table '{self.get_name()}' is currently in READ-ONLY mode (e.g., backing up).")

class AuditingDecorator(TableDecorator):
    def insert(self, row):
        print(f"[SECURITY AUDIT] Attempting to insert into {self.get_name()}...")
        super().insert(row)
        print(f"[SECURITY AUDIT] Insert completed.")

# --- TEST CODE ---
original_table = ConcreteTable("employees")

# Wrap with Audit
audited_table = AuditingDecorator(original_table)
audited_table.insert({"id": 1, "name": "Bob"})
# Output:
# [SECURITY AUDIT] Attempting to insert into employees...
# Table 'employees': Successfully inserted {'id': 1, 'name': 'Bob'}
# [SECURITY AUDIT] Insert completed.

# Suddenly, a backup starts! Wrap the audited table with Read-Only
locked_table = ReadOnlyDecorator(audited_table)

try:
    locked_table.insert({"id": 2, "name": "Alice"})
except Exception as e:
    print(e)
# Output:
# DENIED: Table 'employees' is currently in READ-ONLY mode (e.g., backing up).
```

---

## 19. Facade Pattern: Unified Client Connection (High Priority)

*   **Why choose Facade?**
    Executing a simple SQL query internally requires coordinating dozens of complex subsystems: The Lexer, Parser, AST Builder, Query Optimizer, Execution Engine, and Storage Manager. Forcing an external application (like a Python or Java backend) to interact with all these subsystems directly is a nightmare. Facade provides a single, unified `DBMSClient` class with a simple `execute(query)` method, completely hiding the internal orchestration.

### Class Diagram
```mermaid
classDiagram
    class DBMSFacade {
        -Parser parser
        -Optimizer optimizer
        -Executor executor
        +execute(query) Result
    }
    
    class Parser { +parse(query) AST }
    class Optimizer { +optimize(ast) Plan }
    class Executor { +run(plan) Result }
    
    DBMSFacade --> Parser
    DBMSFacade --> Optimizer
    DBMSFacade --> Executor
```

### Sequence Diagram
```mermaid
sequenceDiagram
    actor AppDeveloper
    participant Facade as DBMSFacade
    participant P as Parser
    participant O as Optimizer
    participant E as Executor
    
    AppDeveloper->>Facade: execute("SELECT * FROM users")
    activate Facade
    Facade->>P: parse(query)
    P-->>Facade: AST
    Facade->>O: optimize(AST)
    O-->>Facade: ExecutionPlan
    Facade->>E: run(ExecutionPlan)
    E-->>Facade: ResultSet
    Facade-->>AppDeveloper: ResultSet
    deactivate Facade
```

### TDD Code Example
```python
# --- Complex Internal Subsystems ---
class Parser:
    def parse(self, sql):
        print("Parser: Breaking SQL into tokens and building AST...")
        return {"type": "SELECT", "table": "users"}

class Optimizer:
    def optimize(self, ast):
        print("Optimizer: Finding best execution path (Index Scan vs Full Scan)...")
        return "Plan(IndexScan on users)"

class Executor:
    def run(self, plan):
        print(f"Executor: Running {plan}...")
        return [{"id": 1, "name": "Alice"}]

# --- The Facade ---
class DBMSFacade:
    def __init__(self):
        # Initializes the complex web of subsystems
        self.parser = Parser()
        self.optimizer = Optimizer()
        self.executor = Executor()
        
    def execute(self, sql_query):
        print(f"--- Facade received query: '{sql_query}' ---")
        ast = self.parser.parse(sql_query)
        plan = self.optimizer.optimize(ast)
        result = self.executor.run(plan)
        return result

# --- TEST CODE ---
# The App Developer's code is extremely clean!
db = DBMSFacade()
rows = db.execute("SELECT * FROM users")
print(f"Result: {rows}")
# Output:
# --- Facade received query: 'SELECT * FROM users' ---
# Parser: Breaking SQL into tokens and building AST...
# Optimizer: Finding best execution path (Index Scan vs Full Scan)...
# Executor: Running Plan(IndexScan on users)...
# Result: [{'id': 1, 'name': 'Alice'}]
```

---

## 20. Mediator Pattern: Transaction Coordination (High Priority)

*   **Why choose Mediator?**
    In a concurrent DBMS, Transactions, Locks, and Recovery Logs must communicate continuously. If `Transaction A` directly asks the `LockManager` for a lock, and the `LockManager` directly talks to the `Table` to apply it, and the `Table` directly talks to the `LogManager` to record it... the system becomes a chaotic web of tight dependencies (Spaghetti code). Mediator introduces a `TransactionCoordinator`. Components only communicate with the Coordinator, which handles the complex routing and deadlock prevention.

### Class Diagram
```mermaid
classDiagram
    class IMediator {
        <<interface>>
        +notify(sender, event, context)*
    }
    
    class TransactionCoordinator {
        -LockManager lock_mgr
        -LogManager log_mgr
        -StorageEngine storage
        +notify(sender, event, context)
    }
    
    class Component {
        <<abstract>>
        #IMediator mediator
    }
    
    class Transaction {
        +execute_query()
    }
    class LockManager {
        +acquire_lock()
    }
    class LogManager {
        +write_log()
    }
    
    IMediator <|.. TransactionCoordinator
    Component <|-- Transaction
    Component <|-- LockManager
    Component <|-- LogManager
    TransactionCoordinator --> Component : coordinates
    Component --> IMediator : notifies
```

### Sequence Diagram
```mermaid
sequenceDiagram
    actor Engine
    participant Tx as Transaction
    participant Med as Coordinator (Mediator)
    participant Lock as LockManager
    participant Log as LogManager
    
    Engine->>Tx: execute_query("UPDATE users")
    activate Tx
    Tx->>Med: notify(self, "REQUEST_WRITE", "users")
    activate Med
    
    Med->>Lock: acquire_lock("users", WRITE)
    Lock-->>Med: success
    
    Med->>Log: write_log("Tx started writing to users")
    Log-->>Med: success
    
    Med-->>Tx: granted
    deactivate Med
    
    Note over Tx: Transaction performs write operation
    Tx-->>Engine: done
    deactivate Tx
```

### TDD Code Example
```python
# The Mediator Interface
class IMediator:
    def notify(self, sender, event, context): pass

# Base Component
class BaseComponent:
    def __init__(self, mediator: IMediator = None):
        self.mediator = mediator

# Concrete Components
class Transaction(BaseComponent):
    def execute_write(self, table_name):
        print(f"Tx: I want to write to '{table_name}'. Asking Coordinator...")
        self.mediator.notify(self, "REQUEST_WRITE", table_name)

class LockManager(BaseComponent):
    def acquire_lock(self, table_name):
        print(f"LockManager: Locking table '{table_name}' for write.")
        return True

class LogManager(BaseComponent):
    def write_log(self, message):
        print(f"LogManager: [LOG] {message}")

# Concrete Mediator
class TransactionCoordinator(IMediator):
    def __init__(self):
        self.lock_mgr = LockManager(self)
        self.log_mgr = LogManager(self)
        
    def notify(self, sender, event, context):
        if event == "REQUEST_WRITE":
            table_name = context
            # Centralized coordination logic
            self.log_mgr.write_log(f"Transaction requested write lock on {table_name}")
            if self.lock_mgr.acquire_lock(table_name):
                self.log_mgr.write_log(f"Write lock granted for {table_name}")
                print(f"Coordinator: Permission granted to Transaction.")

# --- TEST CODE ---
coordinator = TransactionCoordinator()
tx1 = Transaction(coordinator)

tx1.execute_write("employees")
# Output:
# Tx: I want to write to 'employees'. Asking Coordinator...
# LogManager: [LOG] Transaction requested write lock on employees
# LockManager: Locking table 'employees' for write.
# LogManager: [LOG] Write lock granted for employees
# Coordinator: Permission granted to Transaction.
```
"""

dp = dp + dp_content

with open('DPSuggest.md', 'w', encoding='utf-8') as f:
    f.write(dp)
print("Updated DPSuggest.md with Batch 2")

# ================== 2. explain.md ==================
with open('explain.md', 'r', encoding='utf-8') as f:
    explain = f.read()

deep_dives_2 = """
---

## 18. Decorator Pattern (Kẻ Bọc Lót Linh Hoạt)
**Mục tiêu:** Thêm tính năng tạm thời vào một đối tượng một cách linh hoạt tại thời điểm chạy (runtime) thay vì dùng kế thừa cứng nhắc.

- **Vấn đề:** Đang yên đang lành, sếp yêu cầu: "Khi hệ thống đang chạy Backup, tất cả các bảng đang được backup phải lập tức chuyển sang chế độ Chỉ-Đọc (Read-Only) để tránh sai lệch dữ liệu". Nếu bạn dùng kế thừa để tạo class `ReadOnlyTable`, bạn sẽ không thể ép một object `Table` đang tồn tại trong RAM biến hình thành `ReadOnlyTable` được.
- **Giải pháp Decorator:** Đừng sửa object cũ. Hãy tạo ra một cái Vỏ Bọc (Decorator) tên là `ReadOnlyDecorator`. Cái vỏ bọc này có hình dạng y hệt cái Table (Cùng interface). Khi đến giờ Backup, bạn thò tay tóm lấy object `Table`, bọc cái vỏ `ReadOnlyDecorator` ra ngoài nó.
- **Sự linh hoạt:** Khi người dùng gửi lệnh `insert()`, lệnh này sẽ đập vào cái vỏ bọc trước. Cái vỏ lập tức hét lên: "Lỗi! Đang Read-Only!". Khi quá trình Backup xong, bạn chỉ cần gỡ cái vỏ bọc vứt đi, object `Table` bên trong lại `insert()` bình thường mà không hề bị tổn thương. Bạn có thể bọc vô số lớp: Lớp Auditing (Ghi log bảo mật) bọc ngoài lớp Read-Only bọc ngoài Table!

## 19. Facade Pattern (Mặt Tiền Đồng Nhất)
**Mục tiêu:** Cung cấp một giao diện đơn giản duy nhất để giao tiếp với cả một hệ thống nội bộ khổng lồ và phức tạp.

- **Vấn đề:** Để chạy được một lệnh SQL cực kỳ đơn giản `SELECT * FROM users`, bộ máy DBMS phải huy động hàng loạt phòng ban: Phòng Phân Tích Từ Vựng (Lexer), Phòng Cú Pháp (Parser), Phòng Tối Ưu (Optimizer), Phòng Thực Thi (Executor). Nếu bắt người dùng (Lập trình viên viết App) phải tự mình đi gọi lần lượt từng phòng ban này thì họ sẽ phát điên.
- **Giải pháp Facade:** Xây một cái "Mặt tiền" (Facade) đẹp đẽ tên là `DBMSClient`. Mặt tiền này chỉ có đúng 1 cửa sổ giao dịch: hàm `execute(sql)`. Người dùng ném câu SQL qua cửa sổ. Bên trong Facade, các nhân viên tự gọi điện cho Lexer, Parser, Optimizer loạn xạ với nhau, xử lý xong xuôi thì ném trả kết quả ra ngoài.
- **Sự linh hoạt:** Người dùng (Client) bị cô lập hoàn toàn khỏi sự phức tạp của hệ thống. Dù bạn có nâng cấp, đập bỏ thay mới Optimizer, người dùng cũng không bao giờ biết và code của họ không bao giờ bị lỗi.

## 20. Mediator Pattern (Nhà Hoà Giải Trung Tâm)
**Mục tiêu:** Giảm bớt sự giao tiếp hỗn loạn chằng chịt giữa các đối tượng bằng cách ép chúng giao tiếp qua một trung tâm điều phối.

- **Vấn đề:** Trong thế giới giao dịch (Transaction) của Database, sự an toàn là trên hết. Khi một `Transaction` muốn ghi dữ liệu, nó gọi `LockManager` để xin khoá. Nhận khoá xong nó gọi `Table` để ghi. Ghi xong `Table` gọi `LogManager` để lưu lịch sử. Nếu có hàng trăm Transaction chạy cùng lúc, các đối tượng này gọi nhau tạo thành một mạng nhện (Spaghetti code) cực kỳ rối rắm. Nguy cơ Deadlock (Khoá chéo nhau) là 99%.
- **Giải pháp Mediator:** Cấm tuyệt đối các phòng ban tự ý nói chuyện với nhau! Bổ nhiệm một ông `TransactionCoordinator` (Nhà Hoà Giải). Khi Transaction muốn ghi, nó nhắn tin cho Coordinator. Coordinator sẽ tự mình đi xin Lock, tự mình ghi Log, rồi mới báo lại cho Transaction.
- **Sự linh hoạt:** Mọi logic phối hợp phức tạp nhất, logic chống Deadlock, logic huỷ giao dịch (Rollback)... đều được nhét chung vào một chỗ duy nhất là Coordinator. Các phòng ban khác chỉ làm đúng một việc của mình, code cực kỳ sáng sủa và dễ maintain.
"""

checklists_2 = """
### 18. Thuộc cho Decorator Pattern (Kẻ Bọc Lót Linh Hoạt)
**Mục tiêu:** Bọc tính năng ngoài rìa (như Read-Only, Security Audit) vào Table mà không sửa code Table.

*   **Abstract Class `TableDecorator` (Vỏ Bọc Gốc):**
    *   **Kế thừa:** Bắt buộc implement interface `ITable` y hệt như bảng thật.
    *   **Thuộc tính:** `protected ITable wrapped_table` (Chứa đối tượng bị bọc).
    *   **Phương thức:** Chuyển tiếp (forward) toàn bộ các hàm gọi sang cho `wrapped_table`.
*   **Class `ReadOnlyDecorator` (Vỏ Bọc Chỉ Đọc):**
    *   **Phương thức `insert()`:** Thay vì chuyển tiếp lệnh `insert`, nó ném ra lỗi `PermissionError` ngay lập tức để chặn họng.

### 19. Thuộc cho Facade Pattern (Mặt Tiền Đồng Nhất)
**Mục tiêu:** Giấu sự tàn khốc của hệ thống nội bộ sau một nụ cười thân thiện.

*   **Class `DBMSFacade` (Đại Diện Uỷ Quyền):**
    *   **Thuộc tính:** Chứa toàn bộ các con trỏ đến các hệ thống con khổng lồ: `Parser`, `Optimizer`, `Executor`.
    *   **Phương thức `execute(sql_string) -> ResultSet`:** Là hàm duy nhất được public ra thế giới bên ngoài. Nội bộ hàm này sẽ tự động điều phối chuỗi: Parse -> Optimize -> Execute.

### 20. Thuộc cho Mediator Pattern (Nhà Hoà Giải Trung Tâm)
**Mục tiêu:** Chống Deadlock bằng cách tập trung quyền điều phối vào một trung tâm.

*   **Class `TransactionCoordinator` (Kẻ Điều Phối):**
    *   **Kế thừa:** `IMediator`.
    *   **Phương thức cốt lõi:** `+ notify(sender, event, context)`: Hàm này là cái rổ hứng mọi yêu cầu. Bên trong dùng `if/else` để check `event`. Ví dụ nếu event là `REQUEST_WRITE`, nó sẽ ra lệnh cho `LockManager` và `LogManager`.
*   **Các Class `Transaction`, `LockManager` (Đàn em):**
    *   **Thuộc tính:** Chứa duy nhất 1 con trỏ trỏ về sếp `mediator`.
    *   **Quy tắc:** Không bao giờ lưu con trỏ của các đàn em khác. Cần gì thì gọi `self.mediator.notify(...)`.
"""

# Insert Deep Dives before TỔNG HỢP in explain.md
idx1 = explain.find("## TỔNG HỢP: Danh sách Thuộc tính")
idx_insert1 = explain.rfind("---", 0, idx1)
explain = explain[:idx_insert1] + deep_dives_2 + "\n\n" + explain[idx_insert1:]

# Insert Checklists at the end of the file
explain = explain.strip() + "\n\n" + checklists_2

with open('explain.md', 'w', encoding='utf-8') as f:
    f.write(explain)

print("Updated explain.md with Batch 2")
