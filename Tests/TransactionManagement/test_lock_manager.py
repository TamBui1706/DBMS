import unittest

class TestLockManager(unittest.TestCase):
    def test_AcquireLock_WhenResourceFree_GrantsLockInstantly(self):
        pass

    def test_AcquireLock_WhenResourceLocked_BlocksOrThrowsTimeout(self):
        pass

    def test_ReleaseLock_WhenHoldingLock_FreesResourceAndWakesWaiters(self):
        pass

    def test_AcquireLock_WhenSharedLockExists_GrantsAnotherSharedLock(self):
        pass

    def test_AcquireLock_WhenSharedLockExists_BlocksExclusiveLock(self):
        pass

    def test_UpgradeLock_ConvertsSharedToExclusiveIfPossible(self):
        pass

    def test_DowngradeLock_ConvertsExclusiveToShared(self):
        pass

    def test_ReleaseLock_WhenNotHoldingLock_ThrowsException(self):
        pass

