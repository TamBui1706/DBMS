import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Could not find mapping for RestoreManagement
# Could not find mapping for Recovery
# Could not find mapping for Checkpoint
# Could not find mapping for TransactionLogging

class TestRestoreManagement(unittest.TestCase):
    def setUp(self):
        self.restore_mgmt = RestoreManagement()

    def test_restore_full_backup_happy_path(self):
        res = self.restore_mgmt.restore_full_backup(1)
        self.assertTrue(res)

    def test_point_in_time_recovery_failure_path(self):
        with self.assertRaises(Exception):
            self.restore_mgmt.point_in_time_recovery(None)

class TestRecovery(unittest.TestCase):
    def setUp(self):
        self.recovery = Recovery(TransactionLogging("test_wal.log"))

    def test_perform_crash_recovery_happy_path(self):
        res = self.recovery.perform_crash_recovery()
        self.assertTrue(res)

    def test_undo_transaction_happy_path(self):
        res = self.recovery.undo_transaction(1)
        self.assertTrue(res)

class TestCheckpoint(unittest.TestCase):
    def setUp(self):
        self.checkpoint = Checkpoint()

    def test_create_checkpoint_happy_path(self):
        lsn = self.checkpoint.create_checkpoint()
        self.assertIsInstance(lsn, int)

if __name__ == '__main__':
    unittest.main()
