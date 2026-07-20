# 📐 Bảng Tổng Hợp Design Patterns cho Kiến Trúc DBMS

Dưới đây là bảng tổng hợp các Design Patterns được **sắp xếp theo độ quan trọng của tính năng (Feature ưu tiên làm trước)**. 

> [!NOTE] 
> **Một Feature có áp dụng được nhiều Design Pattern không?**
> CÂU TRẢ LỜI LÀ CÓ! Đây gọi là **Compound Patterns** (Mẫu thiết kế kết hợp). Một tính năng lớn thường là sự giao thoa của 2-3 Pattern cùng lúc. Ví dụ cụ thể nhất nằm ở mục **Quản lý Database (Core)** bên dưới.

## 📊 Tóm tắt trực quan

| Feature (Ưu tiên giảm dần) | Vấn đề cần giải quyết | Pattern kết hợp | Ý tưởng |
| :--- | :--- | :--- | :--- |
| **1. Database & Catalog Management**<br/>*(Quản lý Database cốt lõi)* | 1. Hệ thống chỉ được có 1 sổ cái duy nhất để ghi chép.<br/>2. Lệnh tạo DB quá rườm rà (phải cấp ổ cứng, cấp quyền...).<br/>3. Xóa DB phải xóa sạch Schema, Table, Column bên trong. | **Singleton** + **Facade** + **Composite** | - **Singleton:** Dùng cho `CatalogManager` để làm cuốn sổ cái duy nhất.<br/>- **Facade:** Dùng cho `DatabaseManager` để gom hết các lệnh cấp đĩa, cấp quyền phức tạp thành 1 hàm `CreateDatabase()` đơn giản.<br/>- **Composite:** Cấu trúc DB -> Schema -> Table -> Column thành 1 cây phả hệ. Khi gọi `DB.get_size()`, nó sẽ đệ quy tự cộng dồn dung lượng của các con. |
| **2. Query Execution**<br/>*(Xử lý truy vấn)* | Làm sao duyệt bảng có 1 tỷ dòng mà không bị tràn bộ nhớ RAM? | **Iterator**<br/>*(Volcano Model)* | Ép tất cả toán tử (Scan, Filter, Join) giao tiếp với nhau bằng hàm `next()`. Dữ liệu sẽ nhích lên từng dòng một giống như băng chuyền. |
| **3. Transaction Commit/Rollback**<br/>*(Quản lý giao dịch)* | Khi một giao dịch (TX) kết thúc, làm sao báo cho LockManager nhả khóa và BufferPool ghi Log mà không bị dính code chéo? | **Observer** | Cho LockManager và BufferPool "đăng ký theo dõi" TransactionManager. Khi TX chốt xong, nó chỉ cần hô to "Sự kiện Commit", những người kia tự động làm việc của mình. |
| **4. Cache Eviction**<br/>*(Quản lý Buffer Pool)* | Khi RAM đầy, thuật toán đuổi trang (Page) ra khỏi RAM có thể thay đổi liên tục (LRU, Clock, MRU) tùy cấu hình. | **Strategy** | Đóng gói từng thuật toán đuổi trang thành các Strategy riêng. Khởi tạo BufferPool với Strategy nào thì nó xài thuật toán đó. |
| **5. Create Table**<br/>*(Định nghĩa cấu trúc)* | Object Table có rất nhiều thành phần phức tạp (Column, PK, FK, Check Constraint...) làm constructor quá dài và rối. | **Builder** | Xây dựng Table từng bước một thông qua các hàm dây chuyền (Fluent API) thay vì ném một cục tham số vào constructor. |
| **6. Index Creation**<br/>*(Tạo chỉ mục)* | DBMS hỗ trợ nhiều loại Index khác nhau. Làm sao giấu đi sự phức tạp khi đẻ ra `BTreeIndex`, `HashIndex` hay `BitmapIndex`? | **Factory Method** | Đẩy việc tạo Object cho `IndexFactory` quyết định, dựa trên tham số đầu vào (ví dụ: DataType hoặc Cấu hình từ user). |

---

## 💻 Ví dụ Code TDD (Minh họa Kết hợp Patterns)

### 1. Sự kết hợp hoàn hảo (Singleton + Facade + Composite) trong Database
Tính năng tạo và cấu trúc Database.
```python
# 1. SINGLETON: Cuốn sổ cái duy nhất của Server
class CatalogManager:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.databases = {}
        return cls._instance

# 2. COMPOSITE: Cấu trúc cây (Database -> Schema -> Table -> Column)
class Database(Node):
    def __init__(self):
        self.schemas = []
    
    def get_size(self):
        # Đệ quy hỏi các node con (Schema -> Table) để tính tổng dung lượng
        return sum(schema.get_size() for schema in self.schemas)

# 3. FACADE: Giấu đi sự phức tạp khi tạo mới DB
class DatabaseManager:
    def create_database(self, name):
        # Người dùng chỉ gọi hàm này, Facade sẽ tự đi liên hệ các bộ phận khác:
        db = Database(name)
        StorageEngine.allocate_files_for(name)  # Cấp ổ cứng
        SecurityManager.grant_owner_rights()    # Phân quyền
        CatalogManager().register(db)           # Đăng ký vào sổ cái
        return db
```

### 2. Iterator Pattern (Volcano Model - Xử lý tỷ dòng)
```python
class FilterOperator(PhysicalOperator):
    def __init__(self, child_operator, condition):
        self.child = child_operator
        self.condition = condition

    def next(self):
        while True:
            # Nhích băng chuyền lên 1 dòng
            row = self.child.next()
            if row is None: 
                return None # Đã cạn dữ liệu
            
            # Chỉ trả về khi thỏa mãn WHERE
            if self.condition.evaluate(row): 
                return row
```

### 3. Observer Pattern (Quản lý Giao dịch)
```python
class TransactionManager:
    def commit_tx(self, tx_id):
        # 1. Ghi log thành công...
        
        # 2. Phóng sự kiện (Broadcast) cho tất cả những người đang theo dõi
        for observer in self.observers:
            observer.on_transaction_committed(tx_id)
            
class LockManager(TransactionObserver):
    def on_transaction_committed(self, tx_id):
        # Tự động nhả khóa khi nghe thấy tín hiệu Commit
        self.release_all_locks(tx_id) 
```
