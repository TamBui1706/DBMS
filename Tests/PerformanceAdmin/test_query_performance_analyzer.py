import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.PerformanceAdmin.query_performance_analyzer import QueryPerformanceAnalyzer

class TestQueryPerformanceAnalyzer(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeQueryPerformanceAnalyzer(self):
        pass

if __name__ == '__main__':
    unittest.main()
