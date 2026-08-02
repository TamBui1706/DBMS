from AssignmentStore.Entities.product import Product
from AssignmentStore.Repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def list_products(self, search: str = None, category_id: str = None):
        products = self.repository.get_all()
        if search:
            products = [p for p in products if search.lower() in p.name.lower()]
        if category_id:
            products = [p for p in products if p.categoryId == category_id]
        return [self._map_to_dto(p) for p in products]

    def get_product(self, product_id: str):
        p = self.repository.get_by_id(product_id)
        return self._map_to_dto(p) if p else None

    def create_product(self, name: str, price: float, category_id: str = "", type_name: str = "Physical", stock_status: str = "InStock"):
        p = Product(name=name, price=price, category_id=category_id, type_name=type_name, stock_status=stock_status)
        saved = self.repository.save(p)
        return self._map_to_dto(saved)

    def delete_product(self, product_id: str):
        return self.repository.delete(product_id)

    def _map_to_dto(self, p: Product) -> dict:
        return {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "categoryId": p.categoryId,
            "type": p.type,
            "stockStatus": p.stockStatus,
            "images": p.images
        }
