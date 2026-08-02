import uuid

class Product:
    def __init__(self, name: str, price: float, category_id: str = "", type_name: str = "Physical", stock_status: str = "InStock"):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.categoryId = category_id
        self.type = type_name
        self.stockStatus = stock_status
        self.images = []
        self.variants = []
