import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.SecurityAccessControl.security_manager import SecurityManager

class TestSecurityManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeSecurityManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
