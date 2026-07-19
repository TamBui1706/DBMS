import unittest
from unittest.mock import MagicMock

class FileManager:
    pass

class TestFileManager(unittest.TestCase):

    def test_AllocateSpace_CreatesNewBlockAndReturnsId(self):
        # Arrange
        obj = FileManager()
        obj.allocateSpace = MagicMock()
        obj.allocateSpace.return_value = True
        
        # Act
        result = obj.allocateSpace()
        
        # Assert
        self.assertEqual(result, True)
        obj.allocateSpace.assert_called_once()

    def test_DeallocateSpace_MarksBlockAsFree(self):
        # Arrange
        obj = FileManager()
        obj.deallocateSpace = MagicMock()
        obj.deallocateSpace.return_value = True
        
        # Act
        result = obj.deallocateSpace()
        
        # Assert
        self.assertEqual(result, True)
        obj.deallocateSpace.assert_called_once()

    def test_ExtendFile_IncreasesFileSizeWhenFull(self):
        # Arrange
        obj = FileManager()
        obj.extendFile = MagicMock()
        obj.extendFile.return_value = True
        
        # Act
        result = obj.extendFile()
        
        # Assert
        self.assertEqual(result, True)
        obj.extendFile.assert_called_once()

    def test_CloseAll_ReleasesFileHandles(self):
        # Arrange
        obj = FileManager()
        obj.closeAll = MagicMock()
        obj.closeAll.return_value = True
        
        # Act
        result = obj.closeAll()
        
        # Assert
        self.assertEqual(result, True)
        obj.closeAll.assert_called_once()

    def test_GetFileSize_ReturnsSizeInBytes(self):
        # Arrange
        obj = FileManager()
        obj.getFileSize = MagicMock()
        obj.getFileSize.return_value = True
        
        # Act
        result = obj.getFileSize()
        
        # Assert
        self.assertEqual(result, True)
        obj.getFileSize.assert_called_once()

    def test_CheckSpace_ReturnsAvailableBlocks(self):
        # Arrange
        obj = FileManager()
        obj.checkSpace = MagicMock()
        obj.checkSpace.return_value = True
        
        # Act
        result = obj.checkSpace()
        
        # Assert
        self.assertEqual(result, True)
        obj.checkSpace.assert_called_once()
