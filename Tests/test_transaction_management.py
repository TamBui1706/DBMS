import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Classes.TransactionManagement.transaction_manager import TransactionManager
# Could not find mapping for Concurrency
# Could not find mapping for Deadlock
from Classes.TransactionManagement.lock_manager import LockManager

class TestTransactionManager(unittest.TestCase):
    def setUp(self):
        self.txn_manager = TransactionManager()

    def test_begin_transaction_happy_path(self):
        txn_id = self.txn_manager.begin_transaction()
        self.assertIsInstance(txn_id, int)

    def test_commit_transaction_happy_path(self):
        res = self.txn_manager.commit_transaction(1)
        self.assertTrue(res)

    def test_commit_transaction_failure_path(self):
        with self.assertRaises(Exception):
            self.txn_manager.commit_transaction(-99)

    def test_rollback_transaction_happy_path(self):
        res = self.txn_manager.rollback_transaction(1)
        self.assertTrue(res)

class TestConcurrency(unittest.TestCase):
    def setUp(self):
        self.concurrency = Concurrency(LockManager())

    def test_manage_concurrency_happy_path(self):
        res = self.concurrency.manage_concurrency()
        self.assertTrue(res)

class TestDeadlock(unittest.TestCase):
    def setUp(self):
        self.deadlock = Deadlock(LockManager())

    def test_detect_deadlock_happy_path(self):
        cycles = self.deadlock.detect_deadlock()
        self.assertIsInstance(cycles, list)

    def test_resolve_deadlock_happy_path(self):
        res = self.deadlock.resolve_deadlock(1)
        self.assertTrue(res)

if __name__ == '__main__':
    unittest.main()
