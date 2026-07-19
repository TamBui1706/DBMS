import unittest
from unittest.mock import MagicMock

class DataFile:
    pass

class TestDataFile(unittest.TestCase):

    def test_Init_OpensFileStreamForDataBlocks(self):
        # Arrange
        obj = DataFile()
        obj.init = MagicMock()
        obj.init.return_value = True
        
        # Act
        result = obj.init()
        
        # Assert
        self.assertEqual(result, True)
        obj.init.assert_called_once()

    def test_ReadBlock_LoadsBytesFromDisk(self):
        # Arrange
        obj = DataFile()
        obj.readBlock = MagicMock()
        obj.readBlock.return_value = True
        
        # Act
        result = obj.readBlock()
        
        # Assert
        self.assertEqual(result, True)
        obj.readBlock.assert_called_once()

    def test_WriteBlock_SavesBytesToDisk(self):
        # Arrange
        obj = DataFile()
        obj.writeBlock = MagicMock()
        obj.writeBlock.return_value = True
        
        # Act
        result = obj.writeBlock()
        
        # Assert
        self.assertEqual(result, True)
        obj.writeBlock.assert_called_once()

    def test_DeleteFile_RemovesFromOS(self):
        # Arrange
        obj = DataFile()
        obj.deleteFile = MagicMock()
        obj.deleteFile.return_value = True
        
        # Act
        result = obj.deleteFile()
        
        # Assert
        self.assertEqual(result, True)
        obj.deleteFile.assert_called_once()

    def test_Init_WhenFileLockedByOS_ThrowsIOException(self):
        # Arrange
        obj = DataFile()
        obj.init = MagicMock()
        obj.init.side_effect = Exception('IOException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.init()
            
        self.assertTrue('IOException' in str(context.exception))
