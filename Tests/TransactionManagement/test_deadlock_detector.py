import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.TransactionManagement.deadlock_detector import DeadlockDetector

class TestDeadlockDetector(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeDeadlockDetector(self):
        pass

if __name__ == '__main__':
    unittest.main()
