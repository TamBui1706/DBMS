from AssignmentStore.Entities.customer import Customer, CustomerUser
from AssignmentStore.Repositories.customer_repository import CustomerRepository

class CustomerService:
    def __init__(self):
        self.repository = CustomerRepository()

    def list_customers(self, search: str = None, status: str = None, category: str = None):
        customers = self.repository.get_all()
        if search:
            customers = [c for c in customers if search.lower() in c.companyName.lower() or search.lower() in c.domain.lower()]
        if status:
            customers = [c for c in customers if c.status.lower() == status.lower()]
        if category:
            customers = [c for c in customers if category.lower() in c.category.lower()]
        return [self._map_to_dto(c) for c in customers]

    def get_customer(self, customer_id: str):
        c = self.repository.get_by_id(customer_id)
        if not c:
            return None
        return self._map_to_dto(c)

    def create_customer(self, company_name: str, domain: str = "", status: str = "Prospect", category: str = "", description: str = "", users_data: list = None):
        customer = Customer(company_name=company_name, domain=domain, status=status, category=category, description=description)
        if users_data:
            for u in users_data:
                user_obj = CustomerUser(full_name=u.get("fullName", ""), email=u.get("email", ""), avatar_url=u.get("avatarUrl", ""), role=u.get("role", "Owner"))
                customer.users.append(user_obj)
            customer.userCount = len(customer.users)
            
        saved = self.repository.save(customer)
        return self._map_to_dto(saved)

    def delete_customer(self, customer_id: str):
        return self.repository.delete(customer_id)

    def _map_to_dto(self, c: Customer) -> dict:
        return {
            "id": c.id,
            "companyName": c.companyName,
            "logoUrl": c.logoUrl,
            "domain": c.domain,
            "status": c.status,
            "category": c.category,
            "description": c.description,
            "userCount": c.userCount,
            "users": [
                {
                    "id": u.id,
                    "fullName": u.fullName,
                    "avatarUrl": u.avatarUrl
                } for u in c.users
            ],
            "createdAt": c.createdAt,
            "lastActiveAt": c.lastActiveAt
        }
