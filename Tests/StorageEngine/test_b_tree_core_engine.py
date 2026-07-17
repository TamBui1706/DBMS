import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.StorageEngine.b_tree_core_engine import BTreeCoreEngine

class TestBTreeCoreEngine(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeBTreeCoreEngine(self):
        pass

    def test_InsertNode_WhenValid_ShouldSucceed(self):
        pass

    def test_InsertNode_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
