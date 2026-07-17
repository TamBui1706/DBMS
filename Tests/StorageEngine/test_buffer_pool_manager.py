import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.StorageEngine.buffer_pool_manager import BufferPoolManager

class TestBufferPoolManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeBufferPoolManager(self):
        pass

    def test_FetchPage_WhenValid_ShouldSucceed(self):
        pass

    def test_FetchPage_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
