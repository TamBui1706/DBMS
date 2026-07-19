import unittest

class TestMVCCManager(unittest.TestCase):
    def test_CreateVersion_AppendsNewRecordVersionToChain(self):
        pass

    def test_GarbageCollect_RemovesVersionsInvisibleToAllActiveTransactions(self):
        pass

    def test_ReadVersion_ReturnsCorrectDataBasedOnTxSnapshot(self):
        pass

    def test_DetectWriteConflict_WhenTwoTxUpdateSameRecord_ThrowsException(self):
        pass

    def test_ReadVersion_WhenNoVisibleVersion_ReturnsNull(self):
        pass

