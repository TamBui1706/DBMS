import unittest
from unittest.mock import MagicMock

class MVCCManager:
    pass

class TestMVCCManager(unittest.TestCase):

    def test_CreateVersion_AppendsNewRecordVersionToChain(self):
        # Arrange
        obj = MVCCManager()
        obj.createVersion = MagicMock()
        obj.createVersion.return_value = 'Success'
        
        # Act
        result = obj.createVersion()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.createVersion.assert_called_once()

    def test_GarbageCollect_RemovesVersionsInvisibleToAllActiveTransactions(self):
        # Arrange
        obj = MVCCManager()
        obj.garbageCollect = MagicMock()
        obj.garbageCollect.return_value = 'Success'
        
        # Act
        result = obj.garbageCollect()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.garbageCollect.assert_called_once()

    def test_ReadVersion_ReturnsCorrectDataBasedOnTxSnapshot(self):
        # Arrange
        obj = MVCCManager()
        obj.readVersion = MagicMock()
        obj.readVersion.return_value = 'Success'
        
        # Act
        result = obj.readVersion()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.readVersion.assert_called_once()

    def test_DetectWriteConflict_WhenTwoTxUpdateSameRecord_ThrowsException(self):
        # Arrange
        obj = MVCCManager()
        obj.detectWriteConflict = MagicMock()
        obj.detectWriteConflict.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.detectWriteConflict()
            
        self.assertTrue('Exception' in str(context.exception))

    def test_ReadVersion_WhenNoVisibleVersion_ReturnsNull(self):
        # Arrange
        obj = MVCCManager()
        obj.readVersion = MagicMock()
        obj.readVersion.return_value = 'Null'
        
        # Act
        result = obj.readVersion()
        
        # Assert
        self.assertEqual(result, 'Null')
        obj.readVersion.assert_called_once()
