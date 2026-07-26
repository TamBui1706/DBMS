import re

# ================== 1. DPSuggest.md ==================
with open('DPSuggest.md', 'r', encoding='utf-8') as f:
    dp = f.read()

dp_content = """

---

## 21. Memento Pattern: DDL Rollback (Medium Priority)

*   **Why choose Memento?**
    When a user issues an `ALTER TABLE` command (like dropping a column or changing a data type), the operation might fail halfway due to constraints or disk space. If it fails, the Database must roll back the table to its exact previous state. Storing all the previous variables manually is error-prone. Memento allows us to capture the entire internal state of the `Table` (the schema snapshot) into a `TableMemento` object before making changes, and restore it later without breaking encapsulation.

### Class Diagram
```mermaid
classDiagram
    class Table {
        -String name
        -List columns
        +save_state() TableMemento
        +restore_state(TableMemento m)
        +alter_table()
    }
    
    class TableMemento {
        -String state_snapshot
        +get_state() String
    }
    
    class DDLTransaction {
        -TableMemento history
        +execute_alter(Table t)
        +undo(Table t)
    }
    
    Table --> TableMemento : creates
    DDLTransaction o-- TableMemento : stores (Caretaker)
```

### Sequence Diagram
```mermaid
sequenceDiagram
    actor Engine
    participant Tx as DDLTransaction
    participant Tbl as Table
    participant Mem as TableMemento
    
    Engine->>Tx: execute_alter(Tbl)
    activate Tx
    Tx->>Tbl: save_state()
    activate Tbl
    Tbl->>Mem: <<create>>
    Tbl-->>Tx: returns Memento
    deactivate Tbl
    Note over Tx: Stores Memento in history
    
    Tx->>Tbl: alter_table(drop_column)
    Note over Tbl: Fails with Error!
    
    Tx->>Tbl: restore_state(Memento)
    activate Tbl
    Tbl->>Mem: get_state()
    Mem-->>Tbl: previous schema
    Note over Tbl: Restores old schema
    Tbl-->>Tx: done
    deactivate Tbl
    Tx-->>Engine: Transaction Aborted, safely rolled back
    deactivate Tx
```

### TDD Code Example
```python
import copy

class TableMemento:
    def __init__(self, columns):
        # Deep copy is essential so future modifications don't alter the snapshot
        self._columns_snapshot = copy.deepcopy(columns)
        
    def get_saved_columns(self):
        return self._columns_snapshot

class Table:
    def __init__(self, name):
        self.name = name
        self.columns = ["id", "username"]
        
    def save_state(self):
        print(f"Table '{self.name}': Saving schema state to Memento...")
        return TableMemento(self.columns)
        
    def restore_state(self, memento):
        print(f"Table '{self.name}': Restoring schema state from Memento...")
        self.columns = memento.get_saved_columns()
        
    def drop_column(self, col_name):
        print(f"Table '{self.name}': Attempting to drop column '{col_name}'...")
        if col_name == "id":
            raise Exception("Cannot drop Primary Key!")
        self.columns.remove(col_name)

class DDLTransaction:
    def __init__(self):
        self.history = None
        
    def execute_alter(self, table, col_to_drop):
        self.history = table.save_state()
        try:
            table.drop_column(col_to_drop)
            print("Transaction Committed.")
        except Exception as e:
            print(f"Error: {e}. Rolling back...")
            table.restore_state(self.history)

# --- TEST CODE ---
users = Table("users")
print(f"Initial columns: {users.columns}")

tx = DDLTransaction()
# Attempt to drop PK (Will Fail)
tx.execute_alter(users, "id")

print(f"Final columns: {users.columns}")
# Output:
# Initial columns: ['id', 'username']
# Table 'users': Saving schema state to Memento...
# Table 'users': Attempting to drop column 'id'...
# Error: Cannot drop Primary Key!. Rolling back...
# Table 'users': Restoring schema state from Memento...
# Final columns: ['id', 'username']
```

---

## 22. State Pattern: Transaction Lifecycle (Medium Priority)

*   **Why choose State?**
    A Database Transaction has different lifecycle states: `Active`, `PartiallyCommitted`, `Committed`, and `Aborted`. If you call `commit()` on a Transaction that is already `Aborted`, it should throw an error. If we use `if/else` statements inside the Transaction class (`if state == "Aborted": ...`), the code becomes a massive state machine. The State pattern extracts each state into its own class (`ActiveState`, `AbortedState`), encapsulating the specific behaviors and transitions.

### Class Diagram
```mermaid
classDiagram
    class Transaction {
        -ITxState state
        +set_state(state)
        +commit()
        +rollback()
    }
    
    class ITxState {
        <<interface>>
        +commit(tx)*
        +rollback(tx)*
    }
    
    class ActiveState {
        +commit(tx)
        +rollback(tx)
    }
    class AbortedState {
        +commit(tx)
        +rollback(tx)
    }
    
    Transaction *-- ITxState : current state
    ITxState <|.. ActiveState
    ITxState <|.. AbortedState
```

### Sequence Diagram
```mermaid
sequenceDiagram
    actor Client
    participant Tx as Transaction
    participant State as ActiveState
    participant NewState as AbortedState
    
    Client->>Tx: rollback()
    activate Tx
    Tx->>State: rollback(self)
    activate State
    Note over State: Transitions to Aborted
    State->>Tx: set_state(new AbortedState())
    State-->>Tx: success
    deactivate State
    Tx-->>Client: success
    deactivate Tx
    
    Client->>Tx: commit()
    activate Tx
    Note over Tx: State is now AbortedState
    Tx->>NewState: commit(self)
    NewState-->>Tx: throws Exception("Cannot commit aborted Tx")
    Tx-->>Client: Error
    deactivate Tx
```

### TDD Code Example
```python
from abc import ABC, abstractmethod

class ITxState(ABC):
    @abstractmethod
    def commit(self, tx): pass
    @abstractmethod
    def rollback(self, tx): pass

class ActiveState(ITxState):
    def commit(self, tx):
        print("[ActiveState] Writing REDO logs and committing...")
        tx.set_state(CommittedState())
        
    def rollback(self, tx):
        print("[ActiveState] Reverting changes and aborting...")
        tx.set_state(AbortedState())

class CommittedState(ITxState):
    def commit(self, tx):
        print("[CommittedState] Ignored. Already committed.")
    def rollback(self, tx):
        raise Exception("Cannot rollback a transaction that is already committed!")

class AbortedState(ITxState):
    def commit(self, tx):
        raise Exception("Cannot commit a transaction that has been aborted!")
    def rollback(self, tx):
        print("[AbortedState] Ignored. Already aborted.")

class Transaction:
    def __init__(self):
        self.state = ActiveState()
        
    def set_state(self, new_state):
        self.state = new_state
        
    def commit(self):
        self.state.commit(self)
        
    def rollback(self):
        self.state.rollback(self)

# --- TEST CODE ---
tx = Transaction()
tx.rollback() # Moves to AbortedState

try:
    tx.commit() # Will fail because it's aborted
except Exception as e:
    print(f"Error: {e}")

# Output:
# [ActiveState] Reverting changes and aborting...
# Error: Cannot commit a transaction that has been aborted!
```

---

## 23. Interpreter Pattern: SQL Evaluation (High Priority)

*   **Why choose Interpreter?**
    When the SQL Parser reads a `WHERE` clause like `age > 18 AND status = 'ACTIVE'`, it builds an Abstract Syntax Tree (AST). The Query Execution Engine needs to evaluate this tree against millions of rows to filter them. The Interpreter pattern defines a class for each grammatical rule (e.g., `AndExpression`, `GreaterThanExpression`). Each node has an `evaluate(row_data)` method, allowing the AST to naturally interpret the truth value of the row.

### Class Diagram
```mermaid
classDiagram
    class Expression {
        <<interface>>
        +evaluate(row)* bool
    }
    class GreaterThanExpression {
        -String col
        -int val
        +evaluate(row) bool
    }
    class AndExpression {
        -Expression left
        -Expression right
        +evaluate(row) bool
    }
    
    Expression <|.. GreaterThanExpression
    Expression <|.. AndExpression
    AndExpression o-- Expression : contains 2
```

### Sequence Diagram
```mermaid
sequenceDiagram
    actor Engine
    participant And as AndExpression
    participant GT as GreaterThanExpression
    participant EQ as EqualsExpression
    
    Engine->>And: evaluate(row)
    activate And
    And->>GT: evaluate(row)
    GT-->>And: True (age > 18)
    And->>EQ: evaluate(row)
    EQ-->>And: True (status = ACTIVE)
    And-->>Engine: True (Keep row)
    deactivate And
```

### TDD Code Example
```python
from abc import ABC, abstractmethod

# The Abstract Expression
class Expression(ABC):
    @abstractmethod
    def evaluate(self, row: dict) -> bool: pass

# Terminal Expressions (Leaves)
class GreaterThanExpression(Expression):
    def __init__(self, column, value):
        self.column = column
        self.value = value
    def evaluate(self, row):
        return row.get(self.column, 0) > self.value

class EqualsExpression(Expression):
    def __init__(self, column, value):
        self.column = column
        self.value = value
    def evaluate(self, row):
        return row.get(self.column) == self.value

# Non-Terminal Expression (Node)
class AndExpression(Expression):
    def __init__(self, expr1: Expression, expr2: Expression):
        self.expr1 = expr1
        self.expr2 = expr2
    def evaluate(self, row):
        return self.expr1.evaluate(row) and self.expr2.evaluate(row)

# --- TEST CODE ---
# SQL: WHERE age > 18 AND status = 'ACTIVE'
# The Parser builds this AST:
ast_root = AndExpression(
    GreaterThanExpression("age", 18),
    EqualsExpression("status", "ACTIVE")
)

# Execution Engine tests rows against the AST
row1 = {"id": 1, "age": 20, "status": "ACTIVE"}
row2 = {"id": 2, "age": 16, "status": "ACTIVE"}

print(f"Row 1 Matches? {ast_root.evaluate(row1)}")
print(f"Row 2 Matches? {ast_root.evaluate(row2)}")

# Output:
# Row 1 Matches? True
# Row 2 Matches? False
```
"""

dp = dp + dp_content

with open('DPSuggest.md', 'w', encoding='utf-8') as f:
    f.write(dp)
print("Updated DPSuggest.md with Batch 3")

# ================== 2. explain.md ==================
with open('explain.md', 'r', encoding='utf-8') as f:
    explain = f.read()

deep_dives_3 = """
---

## 21. Memento Pattern (Kỷ Vật Quay Ngược Thời Gian)
**Mục tiêu:** Lưu giữ lại trạng thái cũ của một đối tượng để có thể khôi phục (Rollback) khi xảy ra sự cố, mà không làm lộ các biến nội bộ bên trong đối tượng đó.

- **Vấn đề:** Khi quản trị viên gõ lệnh `ALTER TABLE users DROP COLUMN age`. Hệ thống bắt đầu xoá cột. Nhưng xoá được một nửa thì báo lỗi ổ cứng đầy. Lúc này Bảng Users đang ở trạng thái méo mó (nửa mới nửa cũ). Hệ thống bắt buộc phải thực hiện lệnh ROLLBACK để đưa Bảng về trạng thái y hệt như trước khi xoá. Nếu lưu từng biến (tên cột, danh sách index, constraints) ra bên ngoài thì code rất bẩn và phá vỡ nguyên lý Đóng gói (Encapsulation).
- **Giải pháp Memento:** Khái niệm Memento (Kỷ vật) ra đời. Trước khi đụng dao kéo vào Bảng, Bảng sẽ tự chụp X-Quang chính mình, đóng gói toàn bộ trạng thái vào một hộp đen gọi là `TableMemento`. Hộp đen này được giao cho Trình quản lý giao dịch cất giữ. Nếu mổ xẻ thất bại, Trình quản lý giao dịch ném cái hộp đen đó lại cho Bảng. Bảng mở hộp ra và tự động hồi phục lại y chang trạng thái cũ.
- **Sự linh hoạt:** Chỉ có Bảng mới được quyền mở hộp `TableMemento` của chính nó (nhờ class lồng nhau hoặc quyền truy cập đặc biệt). Kẻ giữ hộp đen (Caretaker) không hề biết bên trong hộp chứa gì, bảo mật tuyệt đối!

## 22. State Pattern (Máy Trạng Thái Vạn Năng)
**Mục tiêu:** Cho phép một đối tượng thay đổi hành vi của nó khi trạng thái nội bộ của nó thay đổi. Nhìn từ ngoài vào, dường như class của đối tượng đã bị thay đổi.

- **Vấn đề:** Một Giao dịch (Transaction) có 4 trạng thái: `Active` (Đang chạy), `PartiallyCommitted` (Sắp xong), `Committed` (Đã chốt), `Aborted` (Đã huỷ). Nếu người dùng gọi hàm `tx.commit()`, hệ thống phải check: Nếu đang Active thì cho commit, nếu đã Aborted thì chửi vào mặt người dùng. Dùng hàng loạt câu lệnh `if/else` để kiểm tra state sẽ biến code thành bãi rác không thể bảo trì.
- **Giải pháp State:** Bóc tách mỗi trạng thái ra thành 1 Class riêng biệt (`ActiveState`, `AbortedState`). Transaction bây giờ chỉ là một cái vỏ, ruột của nó là 1 con trỏ chỉ vào 1 trong các State này. Khi gọi `tx.commit()`, Transaction ném quả bóng trách nhiệm đó cho State hiện tại xử lý.
- **Sự linh hoạt:** Nếu ruột đang là `ActiveState`, gọi `commit()` sẽ chạy ghi đĩa. Nhưng nếu ruột đang là `AbortedState`, gọi `commit()` sẽ lập tức văng lỗi Exception. Code không hề có 1 chữ `if/else` nào, cực kỳ sạch sẽ và dễ dàng thêm Trạng thái mới.

## 23. Interpreter Pattern (Kẻ Thông Dịch Ngôn Ngữ)
**Mục tiêu:** Cung cấp một cách để đánh giá (evaluate) các biểu thức ngôn ngữ (như SQL) bằng cách xây dựng một cây cú pháp trừu tượng (Abstract Syntax Tree - AST).

- **Vấn đề:** Khi Động cơ CSDL nhận được câu lệnh `WHERE age > 18 AND status = 'ACTIVE'`. Làm sao để máy tính hiểu được câu tiếng người này để đi lọc dữ liệu?
- **Giải pháp Interpreter:** Parser sẽ phân tích câu lệnh này thành một Cây Cú Pháp. Tại các nút lá là `GreaterThan(age, 18)` và `Equals(status, 'ACTIVE')`. Nút gốc là `And()`. Mọi nút trên cây đều có một hàm duy nhất tên là `evaluate(row_data)`.
- **Sự linh hoạt:** Khi cần kiểm tra một Dòng dữ liệu, hệ thống nhét dòng đó vào Nút Gốc `And`. Nút `And` sẽ truyền xuống cho 2 đứa con. Nếu cả 2 con đều trả về `True`, Nút `And` sẽ phán quyết `True`. Động cơ SQL không cần phải đau đầu suy nghĩ, nó cứ đẩy dữ liệu vào Cây và Cây sẽ tự "Thông dịch" ra câu trả lời đúng sai!
"""

checklists_3 = """
### 21. Thuộc cho Memento Pattern (Kỷ Vật Quay Ngược Thời Gian)
**Mục tiêu:** Hỗ trợ tính năng ROLLBACK DDL bằng cách chụp snapshot an toàn.

*   **Class `TableMemento` (Kỷ Vật - Hộp Đen):**
    *   **Thuộc tính:** Chứa bản sao chép sâu (Deep Copy) của danh sách Cột, Index...
    *   **Quy tắc:** Tuyệt đối KHÔNG có hàm `set()`. Hộp đen này là Bất biến (Immutable) một khi đã được tạo ra.
*   **Class `Table` (Kẻ Lưu Giữ Lịch Sử - Originator):**
    *   **Phương thức:** 
        *   `+ save_state() -> TableMemento`: Đóng gói trạng thái hiện tại thả vào Memento.
        *   `+ restore_state(m: TableMemento)`: Moi dữ liệu từ Memento ra đè lên trạng thái hiện tại.
*   **Class `DDLTransaction` (Kẻ Giữ Hộp - Caretaker):**
    *   **Thuộc tính:** `- history: TableMemento`. Chỉ giữ con trỏ, không bao giờ gọi hàm sửa đổi Memento.

### 22. Thuộc cho State Pattern (Máy Trạng Thái Vạn Năng)
**Mục tiêu:** Quản lý vòng đời Transaction (Active, Committed, Aborted) không cần `if/else`.

*   **Interface `ITxState` (Trạng Thái):**
    *   **Phương thức:** Định nghĩa mọi hành động có thể xảy ra: `commit(tx)`, `rollback(tx)`.
*   **Các Class `ActiveState`, `AbortedState`:**
    *   **Logic:** Tự xử lý logic tuỳ thuộc vào bản thân. Ví dụ `AbortedState.commit()` ném lỗi.
    *   **Chuyển trạng thái:** Thường tự gọi `tx.set_state(new_state)` để biến hình cái Transaction.
*   **Class `Transaction` (Máy Trạng Thái):**
    *   **Thuộc tính:** `- current_state: ITxState`.
    *   **Phương thức:** Chuyển tiếp (Delegate) toàn bộ lệnh gọi từ ngoài vào cho thằng `current_state` xử lý.

### 23. Thuộc cho Interpreter Pattern (Kẻ Thông Dịch Ngôn Ngữ)
**Mục tiêu:** Duyệt cây AST để lọc điều kiện `WHERE` của câu SQL.

*   **Interface `Expression` (Biểu Thức):**
    *   **Phương thức:** `+ evaluate(row: Dict) -> bool`. Chìa khoá của mẫu này là hàm `evaluate`.
*   **Class `AndExpression` (Nút Trung Gian):**
    *   **Thuộc tính:** Giữ 2 con trỏ `left_expr`, `right_expr`.
    *   **Hàm `evaluate`:** `return left_expr.evaluate(row) && right_expr.evaluate(row)`.
*   **Class `GreaterThanExpression` (Nút Lá):**
    *   **Thuộc tính:** Tên cột (`col_name`), giá trị chuẩn (`value`).
    *   **Hàm `evaluate`:** `return row[col_name] > value`.
"""

# Insert Deep Dives before TỔNG HỢP in explain.md
idx1 = explain.find("## TỔNG HỢP: Danh sách Thuộc tính")
idx_insert1 = explain.rfind("---", 0, idx1)
explain = explain[:idx_insert1] + deep_dives_3 + "\n\n" + explain[idx_insert1:]

# Insert Checklists at the end of the file
explain = explain.strip() + "\n\n" + checklists_3

with open('explain.md', 'w', encoding='utf-8') as f:
    f.write(explain)

print("Updated explain.md with Batch 3")
