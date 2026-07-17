import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.SecurityAccessControl.authentication import Authentication

class TestAuthentication(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeAuthentication(self):
        pass

    def test_AuthenticateUser_WhenValid_ShouldSucceed(self):
        pass

    def test_AuthenticateUser_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
