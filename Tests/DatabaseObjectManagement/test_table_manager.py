import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.DatabaseObjectManagement.table_manager import TableManager

class TestTableManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeTableManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
