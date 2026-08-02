import uuid

class Order:
    def __init__(self, customer_id: str, total_amount: float, status: str = "Pending"):
        self.id = str(uuid.uuid4())
        self.customerId = customer_id
        self.totalAmount = total_amount
        self.status = status
        self.paymentStatus = "Unpaid"
        self.fulfillmentStatus = "Unfulfilled"
        self.items = []
