from AssignmentStore.Entities.order import Order

class OrderRepository:
    _store = {}

    @classmethod
    def seed(cls):
        if not cls._store:
            o1 = Order(customer_id="cust_123", total_amount=250.0, status="Completed")
            o1.paymentStatus = "Paid"
            o1.fulfillmentStatus = "Fulfilled"
            o1.items = [{"productId": "prd_1", "quantity": 2, "price": 125.0}]
            cls._store[o1.id] = o1

    def get_all(self):
        self.seed()
        return list(self._store.values())

    def get_by_id(self, order_id: str):
        self.seed()
        return self._store.get(order_id)

    def save(self, order: Order):
        self._store[order.id] = order
        return order

    def delete(self, order_id: str):
        if order_id in self._store:
            del self._store[order_id]
            return True
        return False
