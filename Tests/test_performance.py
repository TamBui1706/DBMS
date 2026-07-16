import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Classes.performance import QueryPerformanceAnalyzer, MemoryManagement

class TestQueryPerformanceAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = QueryPerformanceAnalyzer()

    def test_analyze_slow_queries_happy_path(self):
        slow_queries = self.analyzer.analyze_slow_queries(1000)
        self.assertIsInstance(slow_queries, list)

    def test_suggest_indexes_happy_path(self):
        indexes = self.analyzer.suggest_indexes(1)
        self.assertIsInstance(indexes, list)

class TestMemoryManagement(unittest.TestCase):
    def setUp(self):
        self.memory_mgmt = MemoryManagement(1024)

    def test_allocate_memory_happy_path(self):
        res = self.memory_mgmt.allocate_memory(100)
        self.assertTrue(res)

    def test_allocate_memory_failure_path(self):
        res = self.memory_mgmt.allocate_memory(2048)
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()
