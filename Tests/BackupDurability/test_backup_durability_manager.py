import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.BackupDurability.backup_durability_manager import BackupDurabilityManager

class TestBackupDurabilityManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeBackupDurabilityManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
