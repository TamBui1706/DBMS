import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.StorageEngine.index_manager import IndexManager

class TestIndexManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeIndexManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
