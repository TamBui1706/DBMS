import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.StorageEngine.log_manager import LogManager

class TestLogManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeLogManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
