class AuthRepository:
    _users = {
        "sophia@untitledui.com": {
            "id": "usr_998877",
            "fullName": "Sophia Munn",
            "email": "sophia@untitledui.com",
            "role": "Admin",
            "password": "password123"
        }
    }

    def get_user_by_email(self, email: str):
        return self._users.get(email)

    def create_user(self, full_name: str, email: str, password: str):
        user_id = f"usr_{len(self._users) + 1000}"
        user = {
            "id": user_id,
            "fullName": full_name,
            "email": email,
            "role": "User",
            "password": password
        }
        self._users[email] = user
        return user
