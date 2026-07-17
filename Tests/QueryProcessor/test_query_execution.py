import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.QueryProcessor.query_execution import QueryExecution

class TestQueryExecution(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeQueryExecution(self):
        pass

if __name__ == '__main__':
    unittest.main()
