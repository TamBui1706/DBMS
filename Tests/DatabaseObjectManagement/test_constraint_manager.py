import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.DatabaseObjectManagement.constraint_manager import ConstraintManager

class TestConstraintManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeConstraintManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
