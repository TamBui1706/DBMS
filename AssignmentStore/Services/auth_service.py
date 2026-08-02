from AssignmentStore.Repositories.auth_repository import AuthRepository

class AuthService:
    def __init__(self):
        self.repository = AuthRepository()

    def login(self, email: str, password: str):
        user = self.repository.get_user_by_email(email)
        if not user or user["password"] != password:
            return None
        return {
            "accessToken": f"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.{user['id']}",
            "refreshToken": "d98347f8-9a3b-4c2d-8e1f-6a7b8c9d0e1f",
            "tokenType": "Bearer"
        }

    def register(self, full_name: str, email: str, password: str):
        user = self.repository.create_user(full_name, email, password)
        return {
            "accessToken": f"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.{user['id']}",
            "refreshToken": "d98347f8-9a3b-4c2d-8e1f-6a7b8c9d0e1f",
            "tokenType": "Bearer"
        }

    def get_me(self, email: str = "sophia@untitledui.com"):
        user = self.repository.get_user_by_email(email)
        if not user:
            return None
        return {
            "id": user["id"],
            "fullName": user["fullName"],
            "email": user["email"],
            "role": user["role"],
            "store": {"name": "My online store"}
        }
