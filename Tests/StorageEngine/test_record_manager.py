import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.StorageEngine.record_manager import RecordManager

class TestRecordManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeRecordManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
