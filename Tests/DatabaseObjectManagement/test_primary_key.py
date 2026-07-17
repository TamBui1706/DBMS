import unittest

class TestPrimaryKey(unittest.TestCase):
    def Validate_WhenValueIsUniqueAndNotNull_Succeeds(self):
        pass

    def Validate_WhenValueIsNull_ThrowsNullException(self):
        pass

    def Validate_WhenValueIsDuplicate_ThrowsDuplicateKeyException(self):
        pass

