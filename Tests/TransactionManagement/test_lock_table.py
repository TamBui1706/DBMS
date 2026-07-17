import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.TransactionManagement.lock_table import LockTable

class TestLockTable(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeLockTable(self):
        pass

    def test_GetLocks_WhenValid_ShouldSucceed(self):
        pass

    def test_GetLocks_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
