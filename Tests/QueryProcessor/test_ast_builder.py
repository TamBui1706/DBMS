import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.QueryProcessor.ast_builder import ASTBuilder

class TestASTBuilder(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeASTBuilder(self):
        pass

    def test_BuildTree_WhenValid_ShouldSucceed(self):
        pass

    def test_BuildTree_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
