import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.SecurityAccessControl.user_management import UserManagement

class TestUserManagement(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeUserManagement(self):
        pass

if __name__ == '__main__':
    unittest.main()
