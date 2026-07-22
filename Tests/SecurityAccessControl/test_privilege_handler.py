import unittest
from unittest.mock import MagicMock
from Classes.SecurityAccessControl.privilege_handler import DatabasePrivilegeHandler, SchemaPrivilegeHandler, TablePrivilegeHandler
from Classes.SecurityAccessControl.exceptions import AccessDeniedException

class TestPrivilegeHandlerChain(unittest.TestCase):

    def setUp(self):
        # Arrange: Build the chain
        # DB -> Schema -> Table
        self.db_handler = DatabasePrivilegeHandler()
        self.schema_handler = SchemaPrivilegeHandler()
        self.table_handler = TablePrivilegeHandler()

        self.db_handler.set_next(self.schema_handler)
        self.schema_handler.set_next(self.table_handler)

    def test_Chain_WhenAllLayersPass_ReturnsTrue(self):
        # Act
        result = self.db_handler.check_access("admin", "SELECT", "users")
        
        # Assert
        self.assertTrue(result)

    def test_Chain_WhenFailsAtLayer1_RaisesExceptionImmediately(self):
        # Arrange
        self.db_handler.do_check = MagicMock(return_value=False)
        
        # Act & Assert
        with self.assertRaises(AccessDeniedException) as context:
            self.db_handler.check_access("bob", "DROP", "users")
            
        self.assertIn("Access Denied", str(context.exception))
        self.db_handler.do_check.assert_called_once()

    def test_Chain_WhenFailsAtLayer3_RaisesException(self):
        # Arrange
        self.table_handler.do_check = MagicMock(return_value=False)
        
        # Act & Assert
        with self.assertRaises(AccessDeniedException) as context:
            self.db_handler.check_access("charlie", "DELETE", "users")
            
        self.assertIn("Access Denied", str(context.exception))
        self.table_handler.do_check.assert_called_once()
