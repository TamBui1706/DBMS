import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.BackupDurability.checkpoint_manager import CheckpointManager

class TestCheckpointManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeCheckpointManager(self):
        pass

if __name__ == '__main__':
    unittest.main()
