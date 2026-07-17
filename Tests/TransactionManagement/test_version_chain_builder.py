import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.TransactionManagement.version_chain_builder import VersionChainBuilder

class TestVersionChainBuilder(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeVersionChainBuilder(self):
        pass

    def test_LinkVersion_WhenValid_ShouldSucceed(self):
        pass

    def test_LinkVersion_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
