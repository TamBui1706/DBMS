import unittest

class TestStorageEngine(unittest.TestCase):
    def test_ReadPage_WhenPageNotInBuffer_LoadsFromDisk(self):
        pass

    def test_WritePage_WhenPageIsDirty_FlushesToDisk(self):
        pass

    def test_AllocatePage_CreatesNewPageAndReturnsId(self):
        pass

    def test_DeallocatePage_FreesPageSpace(self):
        pass

    def test_Sync_ForcesAllDirtyPagesToDisk(self):
        pass

    def test_FormatDrive_InitializesDataDirectoryStructure(self):
        pass

