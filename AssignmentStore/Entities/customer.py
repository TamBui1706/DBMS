import uuid
from datetime import datetime

class CustomerUser:
    def __init__(self, full_name: str, email: str = "", avatar_url: str = "", role: str = "Owner"):
        self.id = str(uuid.uuid4())
        self.fullName = full_name
        self.email = email
        self.avatarUrl = avatar_url
        self.role = role

class Customer:
    def __init__(self, company_name: str, domain: str = "", status: str = "Prospect", category: str = "", description: str = ""):
        self.id = str(uuid.uuid4())
        self.companyName = company_name
        self.logoUrl = ""
        self.domain = domain
        self.status = status
        self.category = category
        self.description = description
        self.userCount = 0
        self.users = []
        self.createdAt = datetime.utcnow().isoformat() + "Z"
        self.lastActiveAt = datetime.utcnow().isoformat() + "Z"
