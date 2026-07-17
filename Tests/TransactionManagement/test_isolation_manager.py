import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.TransactionManagement.isolation_manager import IsolationManager

class TestIsolationManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeIsolationManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
