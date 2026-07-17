import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.TransactionManagement.read_view_generator import ReadViewGenerator

class TestReadViewGenerator(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeReadViewGenerator(self):
        pass

    def test_CreateSnapshot_WhenValid_ShouldSucceed(self):
        pass

    def test_CreateSnapshot_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
