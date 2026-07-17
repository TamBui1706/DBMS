import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.StorageEngine.page_replacement_algorithm import PageReplacementAlgorithm

class TestPageReplacementAlgorithm(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializePageReplacementAlgorithm(self):
        pass

    def test_FindVictim_WhenValid_ShouldSucceed(self):
        pass

    def test_FindVictim_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
