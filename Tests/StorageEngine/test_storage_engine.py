import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.StorageEngine.storage_engine import StorageEngine

class TestStorageEngine(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeStorageEngine(self):
        pass

if __name__ == '__main__':
    unittest.main()
