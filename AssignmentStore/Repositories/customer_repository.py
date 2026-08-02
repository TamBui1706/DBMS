from AssignmentStore.Entities.customer import Customer, CustomerUser

class CustomerRepository:
    _store = {}

    @classmethod
    def seed(cls):
        if not cls._store:
            c1 = Customer(company_name="Framer", domain="framer.com", status="Customer", category="Design Tools")
            c1.userCount = 4
            c1.users.append(CustomerUser(full_name="Sophia Munn", email="sophia@untitledui.com", role="Owner"))
            cls._store[c1.id] = c1

            c2 = Customer(company_name="Intercom", domain="intercom.com", status="Customer", category="Customer Engagement")
            c2.userCount = 2
            cls._store[c2.id] = c2

            c3 = Customer(company_name="Stripe", domain="stripe.com", status="Churned", category="Financial Tools")
            c3.userCount = 8
            cls._store[c3.id] = c3

    def get_all(self):
        self.seed()
        return list(self._store.values())

    def get_by_id(self, customer_id: str):
        self.seed()
        return self._store.get(customer_id)

    def save(self, customer: Customer):
        self._store[customer.id] = customer
        return customer

    def delete(self, customer_id: str):
        if customer_id in self._store:
            del self._store[customer_id]
            return True
        return False
