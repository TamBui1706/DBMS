import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.QueryProcessor.query_optimizer import QueryOptimizer

class TestQueryOptimizer(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeQueryOptimizer(self):
        pass

if __name__ == '__main__':
    unittest.main()
