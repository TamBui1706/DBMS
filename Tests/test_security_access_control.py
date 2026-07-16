import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Classes.SecurityAccessControl.access_control import AccessControl
from Classes.SecurityAccessControl.user_management import UserManagement
from Classes.SecurityAccessControl.authentication import Authentication
from Classes.SecurityAccessControl.authorization import Authorization

class TestAccessControl(unittest.TestCase):
    def setUp(self):
        self.access_control = AccessControl(Authentication(), Authorization())

    def test_grant_access_happy_path(self):
        res = self.access_control.grant_access(1, 1, "READ")
        self.assertTrue(res)

    def test_grant_access_failure_path(self):
        with self.assertRaises(Exception):
            self.access_control.grant_access(-1, -1, "INVALID")

class TestUserManagement(unittest.TestCase):
    def setUp(self):
        self.user_mgmt = UserManagement()

    def test_create_user_happy_path(self):
        user_id = self.user_mgmt.create_user("admin", "hash")
        self.assertIsInstance(user_id, int)

    def test_delete_user_failure_path(self):
        with self.assertRaises(Exception):
            self.user_mgmt.delete_user(-1)

if __name__ == '__main__':
    unittest.main()
