import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.StorageEngine.lsn_generator import LSNGenerator

class TestLSNGenerator(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeLSNGenerator(self):
        pass

    def test_NextLSN_WhenValid_ShouldSucceed(self):
        pass

    def test_NextLSN_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
