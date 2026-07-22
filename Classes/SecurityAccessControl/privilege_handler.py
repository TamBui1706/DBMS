from abc import ABC, abstractmethod
from DBMS.Classes.SecurityAccessControl.exceptions import AccessDeniedException

class PrivilegeHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler: 'PrivilegeHandler') -> 'PrivilegeHandler':
        self.next_handler = handler
        return handler

    def check_access(self, user: str, action: str, target: str) -> bool:
        if not self.do_check(user, action, target):
            raise AccessDeniedException(f"Access Denied for user '{user}' attempting '{action}' on '{target}' at {self.__class__.__name__}")
        
        if self.next_handler:
            return self.next_handler.check_access(user, action, target)
        return True

    @abstractmethod
    def do_check(self, user: str, action: str, target: str) -> bool:
        pass

class DatabasePrivilegeHandler(PrivilegeHandler):
    def do_check(self, user: str, action: str, target: str) -> bool:
        # Check DB-level access
        # e.g., if user is admin, return True
        return True

class SchemaPrivilegeHandler(PrivilegeHandler):
    def do_check(self, user: str, action: str, target: str) -> bool:
        # Check Schema-level access
        return True

class TablePrivilegeHandler(PrivilegeHandler):
    def do_check(self, user: str, action: str, target: str) -> bool:
        # Check Table-level access
        return True

class ColumnPrivilegeHandler(PrivilegeHandler):
    def do_check(self, user: str, action: str, target: str) -> bool:
        # Check Column-level access
        return True
