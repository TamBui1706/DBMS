import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.SecurityAccessControl.access_control import AccessControl

class TestAccessControl(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeAccessControl(self):
        pass

if __name__ == '__main__':
    unittest.main()
