import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.DatabaseObjectManagement.column_manager import ColumnManager

class TestColumnManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeColumnManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
