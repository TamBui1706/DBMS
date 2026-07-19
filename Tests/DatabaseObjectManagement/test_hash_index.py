import unittest

class TestHashIndex(unittest.TestCase):
    def test_InsertKey_ComputesHashAndAddsToBucket(self):
        pass

    def test_Search_WhenKeyExists_ResolvesHashToRowID(self):
        pass

    def test_HandleCollision_CreatesLinkedListInBucket(self):
        pass

    def test_Resize_ExpandsHashTableWhenLoadFactorExceeded(self):
        pass

    def test_DeleteKey_RemovesFromBucketLinkedList(self):
        pass

    def test_ComputeHash_DistributesKeysEvenly(self):
        pass

