import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.QueryProcessor.syntax_analyzer import SyntaxAnalyzer

class TestSyntaxAnalyzer(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeSyntaxAnalyzer(self):
        pass

    def test_CheckSyntax_WhenValid_ShouldSucceed(self):
        pass

    def test_CheckSyntax_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
