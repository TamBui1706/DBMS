import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.BackupDurability.recovery_manager import RecoveryManager

class TestRecoveryManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeRecoveryManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
