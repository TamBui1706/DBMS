import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.StorageEngine.index_scan import IndexScan

class TestIndexScan(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeIndexScan(self):
        pass

    def test_Scan_WhenValid_ShouldSucceed(self):
        pass

    def test_Scan_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
