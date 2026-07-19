import unittest

class TestPrimaryKey(unittest.TestCase):
    def test_Validate_WhenValueIsUniqueAndNotNull_Succeeds(self):
        pass

    def test_Validate_WhenValueIsNull_ThrowsNullException(self):
        pass

    def test_Validate_WhenValueIsDuplicate_ThrowsDuplicateKeyException(self):
        pass

    def test_Validate_WithCompositeKey_ChecksAllColumns(self):
        pass

    def test_Drop_RemovesIndexFromStorage(self):
        pass

