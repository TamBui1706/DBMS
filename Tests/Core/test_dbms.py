import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.Core.dbms import DBMS

class TestDBMS(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeDBMS(self):
        pass

    def test_StartSystem_WhenValid_ShouldSucceed(self):
        pass

    def test_StartSystem_WhenInvalid_ShouldThrow(self):
        pass

    def test_StopSystem_WhenValid_ShouldSucceed(self):
        pass

    def test_StopSystem_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
