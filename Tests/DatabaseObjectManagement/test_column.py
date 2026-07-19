import unittest

class TestColumn(unittest.TestCase):
    def test_Init_SetsNameAndNullableFlags(self):
        pass

    def test_ValidateType_WhenDataMatchesColumnType_Succeeds(self):
        pass

    def test_ValidateType_WhenDataIsStringForIntColumn_ThrowsTypeException(self):
        pass

    def test_ValidateNullable_WhenNullPassedToNotNullColumn_ThrowsException(self):
        pass

    def test_SetDefaultValue_StoresDefaultExpression(self):
        pass

    def test_ChangeType_WhenCompatible_Succeeds(self):
        pass

    def test_ChangeType_WhenIncompatible_ThrowsException(self):
        pass

