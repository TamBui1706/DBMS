import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.DatabaseObjectManagement.primary_key_validator import PrimaryKeyValidator

class TestPrimaryKeyValidator(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializePrimaryKeyValidator(self):
        pass

    def test_ValidatePK_WhenValid_ShouldSucceed(self):
        pass

    def test_ValidatePK_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
