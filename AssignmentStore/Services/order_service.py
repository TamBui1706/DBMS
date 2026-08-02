from AssignmentStore.Entities.order import Order
from AssignmentStore.Repositories.order_repository import OrderRepository

class OrderService:
    def __init__(self):
        self.repository = OrderRepository()

    def list_orders(self, customer_id: str = None, status: str = None):
        orders = self.repository.get_all()
        if customer_id:
            orders = [o for o in orders if o.customerId == customer_id]
        if status:
            orders = [o for o in orders if o.status.lower() == status.lower()]
        return [self._map_to_dto(o) for o in orders]

    def get_order(self, order_id: str):
        o = self.repository.get_by_id(order_id)
        return self._map_to_dto(o) if o else None

    def create_order(self, customer_id: str, total_amount: float, items: list = None):
        o = Order(customer_id=customer_id, total_amount=total_amount)
        if items:
            o.items = items
        saved = self.repository.save(o)
        return self._map_to_dto(saved)

    def update_order_status(self, order_id: str, new_status: str):
        o = self.repository.get_by_id(order_id)
        if not o:
            return None
        o.status = new_status
        self.repository.save(o)
        return self._map_to_dto(o)

    def delete_order(self, order_id: str):
        return self.repository.delete(order_id)

    def _map_to_dto(self, o: Order) -> dict:
        return {
            "id": o.id,
            "customerId": o.customerId,
            "totalAmount": o.totalAmount,
            "status": o.status,
            "paymentStatus": o.paymentStatus,
            "fulfillmentStatus": o.fulfillmentStatus,
            "items": o.items
        }
