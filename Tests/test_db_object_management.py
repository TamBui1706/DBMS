import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Classes.DatabaseObjectManagement.database_management import DatabaseManagement
# Could not find mapping for TableManagement
# Could not find mapping for ViewManagement
# Could not find mapping for ColumnManagement
# Could not find mapping for ConstraintManagement

class TestDatabaseManagement(unittest.TestCase):
    def setUp(self):
        self.db_mgmt = DatabaseManagement()

    def test_create_database_happy_path(self):
        db_id = self.db_mgmt.create_database("testdb")
        self.assertIsInstance(db_id, int)

    def test_drop_database_failure_path(self):
        with self.assertRaises(Exception):
            self.db_mgmt.drop_database(-1)

class TestTableManagement(unittest.TestCase):
    def setUp(self):
        self.table_mgmt = TableManagement()

    def test_create_table_happy_path(self):
        table_id = self.table_mgmt.create_table(1, "users", [{"name": "id", "type": "INT"}])
        self.assertIsInstance(table_id, int)

    def test_drop_table_failure_path(self):
        with self.assertRaises(Exception):
            self.table_mgmt.drop_table(-1)

class TestViewManagement(unittest.TestCase):
    def setUp(self):
        self.view_mgmt = ViewManagement()

    def test_create_view_happy_path(self):
        view_id = self.view_mgmt.create_view(1, "active_users", "SELECT * FROM users WHERE active=1")
        self.assertIsInstance(view_id, int)

class TestConstraintManagement(unittest.TestCase):
    def setUp(self):
        self.constraint_mgmt = ConstraintManagement()

    def test_add_constraint_happy_path(self):
        cid = self.constraint_mgmt.add_constraint(1, "PRIMARY_KEY", {"column": "id"})
        self.assertIsInstance(cid, int)

class TestColumnManagement(unittest.TestCase):
    def setUp(self):
        self.column_mgmt = ColumnManagement()

    def test_add_column_happy_path(self):
        res = self.column_mgmt.add_column(1, "email", "VARCHAR")
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()
