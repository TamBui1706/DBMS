import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.PerformanceAdmin.performance_manager import PerformanceManager

class TestPerformanceManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializePerformanceManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
