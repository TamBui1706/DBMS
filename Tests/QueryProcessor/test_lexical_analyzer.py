import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.QueryProcessor.lexical_analyzer import LexicalAnalyzer

class TestLexicalAnalyzer(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeLexicalAnalyzer(self):
        pass

    def test_Tokenize_WhenValid_ShouldSucceed(self):
        pass

    def test_Tokenize_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
