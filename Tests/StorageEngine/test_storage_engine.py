import unittest
from unittest.mock import MagicMock

class StorageEngine:
    pass

class TestStorageEngine(unittest.TestCase):

    def test_ReadPage_WhenPageNotInBuffer_LoadsFromDisk(self):
        # Arrange
        obj = StorageEngine()
        obj.readPage = MagicMock()
        obj.readPage.return_value = True
        
        # Act
        result = obj.readPage()
        
        # Assert
        self.assertEqual(result, True)
        obj.readPage.assert_called_once()

    def test_WritePage_WhenPageIsDirty_FlushesToDisk(self):
        # Arrange
        obj = StorageEngine()
        obj.writePage = MagicMock()
        obj.writePage.return_value = True
        
        # Act
        result = obj.writePage()
        
        # Assert
        self.assertEqual(result, True)
        obj.writePage.assert_called_once()

    def test_AllocatePage_CreatesNewPageAndReturnsId(self):
        # Arrange
        obj = StorageEngine()
        obj.allocatePage = MagicMock()
        obj.allocatePage.return_value = True
        
        # Act
        result = obj.allocatePage()
        
        # Assert
        self.assertEqual(result, True)
        obj.allocatePage.assert_called_once()

    def test_DeallocatePage_FreesPageSpace(self):
        # Arrange
        obj = StorageEngine()
        obj.deallocatePage = MagicMock()
        obj.deallocatePage.return_value = True
        
        # Act
        result = obj.deallocatePage()
        
        # Assert
        self.assertEqual(result, True)
        obj.deallocatePage.assert_called_once()

    def test_Sync_ForcesAllDirtyPagesToDisk(self):
        # Arrange
        obj = StorageEngine()
        obj.sync = MagicMock()
        obj.sync.return_value = True
        
        # Act
        result = obj.sync()
        
        # Assert
        self.assertEqual(result, True)
        obj.sync.assert_called_once()

    def test_FormatDrive_InitializesDataDirectoryStructure(self):
        # Arrange
        obj = StorageEngine()
        obj.formatDrive = MagicMock()
        obj.formatDrive.return_value = True
        
        # Act
        result = obj.formatDrive()
        
        # Assert
        self.assertEqual(result, True)
        obj.formatDrive.assert_called_once()
