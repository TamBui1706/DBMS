import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.DatabaseObjectManagement.database_object_manager import DatabaseObjectManager

class TestDatabaseObjectManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeDatabaseObjectManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
