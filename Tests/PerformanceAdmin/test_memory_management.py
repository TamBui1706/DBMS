import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.PerformanceAdmin.memory_management import MemoryManagement

class TestMemoryManagement(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeMemoryManagement(self):
        pass

if __name__ == '__main__':
    unittest.main()
