import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.StorageEngine.access_methods import AccessMethods

class TestAccessMethods(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeAccessMethods(self):
        pass

if __name__ == '__main__':
    unittest.main()
