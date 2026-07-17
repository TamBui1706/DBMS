import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.StorageEngine.rid_generator import RIDGenerator

class TestRIDGenerator(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeRIDGenerator(self):
        pass

    def test_GenerateRID_WhenValid_ShouldSucceed(self):
        pass

    def test_GenerateRID_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
