import unittest

class TestForeignKey(unittest.TestCase):
    def test_Validate_WhenReferencedRowExists_Succeeds(self):
        pass

    def test_Validate_WhenReferencedRowDoesNotExist_ThrowsForeignKeyException(self):
        pass

    def test_Init_SetsReferenceTableCorrectly(self):
        pass

    def test_OnDeleteCascade_RemovesChildRowsWhenParentDeleted(self):
        pass

    def test_OnDeleteRestrict_ThrowsExceptionWhenParentDeleted(self):
        pass

    def test_OnUpdateCascade_ModifiesChildRowsWhenParentKeyChanges(self):
        pass

