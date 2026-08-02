from AssignmentStore.Entities.product import Product

class ProductRepository:
    _store = {}

    @classmethod
    def seed(cls):
        if not cls._store:
            p1 = Product(name="Design System Pro Kit", price=99.0, category_id="cat_ui", type_name="Digital")
            cls._store[p1.id] = p1

    def get_all(self):
        self.seed()
        return list(self._store.values())

    def get_by_id(self, product_id: str):
        self.seed()
        return self._store.get(product_id)

    def save(self, product: Product):
        self._store[product.id] = product
        return product

    def delete(self, product_id: str):
        if product_id in self._store:
            del self._store[product_id]
            return True
        return False
