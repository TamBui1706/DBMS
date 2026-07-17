import unittest

class TestLockManager(unittest.TestCase):
    def AcquireLock_WhenResourceFree_GrantsLockInstantly(self):
        pass

    def AcquireLock_WhenResourceLocked_BlocksOrThrowsTimeout(self):
        pass

    def ReleaseLock_WhenHoldingLock_FreesResourceAndWakesWaiters(self):
        pass

