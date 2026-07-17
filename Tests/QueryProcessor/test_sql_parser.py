import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.QueryProcessor.sql_parser import SQLParser

class TestSQLParser(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeSQLParser(self):
        pass

if __name__ == '__main__':
    unittest.main()
