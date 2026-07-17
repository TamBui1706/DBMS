import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.BackupDurability.restore_manager import RestoreManager

class TestRestoreManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeRestoreManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
