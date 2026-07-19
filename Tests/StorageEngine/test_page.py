import unittest

class TestPage(unittest.TestCase):
    def test_Init_SetsPageIdAndClearsDirtyFlag(self):
        pass

    def test_MarkDirty_SetsDirtyFlagToTrue(self):
        pass

    def test_ReadTuple_ReturnsDataAtOffset(self):
        pass

    def test_WriteTuple_SavesDataAndUpdatesFreeSpace(self):
        pass

    def test_HasSpace_ReturnsTrueIfTupleFits(self):
        pass

    def test_Compact_ReorganizesTuplesToRemoveFragmentation(self):
        pass

    def test_DeleteTuple_MarksSlotAsEmpty(self):
        pass

