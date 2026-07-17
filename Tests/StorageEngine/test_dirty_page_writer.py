import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.StorageEngine.dirty_page_writer import DirtyPageWriter

class TestDirtyPageWriter(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeDirtyPageWriter(self):
        pass

    def test_FlushDirtyPages_WhenValid_ShouldSucceed(self):
        pass

    def test_FlushDirtyPages_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
