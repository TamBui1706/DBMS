import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.BackupDurability.undo_log_applier import UNDOLogApplier

class TestUNDOLogApplier(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeUNDOLogApplier(self):
        pass

    def test_Rollback_WhenValid_ShouldSucceed(self):
        pass

    def test_Rollback_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
