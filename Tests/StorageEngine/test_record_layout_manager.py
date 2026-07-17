import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.StorageEngine.record_layout_manager import RecordLayoutManager

class TestRecordLayoutManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeRecordLayoutManager(self):
        pass

    def test_FormatRecord_WhenValid_ShouldSucceed(self):
        pass

    def test_FormatRecord_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
