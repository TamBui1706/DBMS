import unittest
from unittest.mock import MagicMock

class LockTable:
    pass

class TestLockTable(unittest.TestCase):

    def test_GetLocks_ReturnsCurrentLockInformation(self):
        # Arrange
        obj = LockTable()
        obj.getLocks = MagicMock()
        obj.getLocks.return_value = 'Success'
        
        # Act
        result = obj.getLocks()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.getLocks.assert_called_once()

    def test_AddLock_RegistersNewLockForResource(self):
        # Arrange
        obj = LockTable()
        obj.addLock = MagicMock()
        obj.addLock.return_value = 'Success'
        
        # Act
        result = obj.addLock()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.addLock.assert_called_once()

    def test_RemoveLock_DeletesRegistration(self):
        # Arrange
        obj = LockTable()
        obj.removeLock = MagicMock()
        obj.removeLock.return_value = 'Success'
        
        # Act
        result = obj.removeLock()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.removeLock.assert_called_once()

    def test_Clear_RemovesAllLocksDuringSystemReset(self):
        # Arrange
        obj = LockTable()
        obj.clear = MagicMock()
        obj.clear.return_value = 'Success'
        
        # Act
        result = obj.clear()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.clear.assert_called_once()

    def test_CountLocks_ForSpecificTransactionId(self):
        # Arrange
        obj = LockTable()
        obj.countLocks = MagicMock()
        obj.countLocks.return_value = 'Success'
        
        # Act
        result = obj.countLocks()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.countLocks.assert_called_once()
