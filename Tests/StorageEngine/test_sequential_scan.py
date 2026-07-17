import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.StorageEngine.sequential_scan import SequentialScan

class TestSequentialScan(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeSequentialScan(self):
        pass

    def test_Scan_WhenValid_ShouldSucceed(self):
        pass

    def test_Scan_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
