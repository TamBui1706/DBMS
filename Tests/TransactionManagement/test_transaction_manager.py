import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.TransactionManagement.transaction_manager import TransactionManager

class TestTransactionManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeTransactionManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
