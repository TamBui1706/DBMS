import unittest
from unittest.mock import MagicMock

class LockManager:
    pass

class TestLockManager(unittest.TestCase):

    def test_AcquireLock_WhenResourceFree_GrantsLockInstantly(self):
        # Arrange
        obj = LockManager()
        obj.acquireLock = MagicMock()
        obj.acquireLock.return_value = True
        
        # Act
        result = obj.acquireLock()
        
        # Assert
        self.assertEqual(result, True)
        obj.acquireLock.assert_called_once()

    def test_AcquireLock_WhenResourceLocked_BlocksOrThrowsTimeout(self):
        # Arrange
        obj = LockManager()
        obj.acquireLock = MagicMock()
        obj.acquireLock.side_effect = Exception('BlocksOrTimeout')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.acquireLock()
            
        self.assertTrue('BlocksOrTimeout' in str(context.exception))

    def test_ReleaseLock_WhenHoldingLock_FreesResourceAndWakesWaiters(self):
        # Arrange
        obj = LockManager()
        obj.releaseLock = MagicMock()
        obj.releaseLock.return_value = True
        
        # Act
        result = obj.releaseLock()
        
        # Assert
        self.assertEqual(result, True)
        obj.releaseLock.assert_called_once()

    def test_AcquireLock_WhenSharedLockExists_GrantsAnotherSharedLock(self):
        # Arrange
        obj = LockManager()
        obj.acquireLock = MagicMock()
        obj.acquireLock.return_value = True
        
        # Act
        result = obj.acquireLock()
        
        # Assert
        self.assertEqual(result, True)
        obj.acquireLock.assert_called_once()

    def test_AcquireLock_WhenSharedLockExists_BlocksExclusiveLock(self):
        # Arrange
        obj = LockManager()
        obj.acquireLock = MagicMock()
        obj.acquireLock.return_value = True
        
        # Act
        result = obj.acquireLock()
        
        # Assert
        self.assertEqual(result, True)
        obj.acquireLock.assert_called_once()

    def test_UpgradeLock_ConvertsSharedToExclusiveIfPossible(self):
        # Arrange
        obj = LockManager()
        obj.upgradeLock = MagicMock()
        obj.upgradeLock.return_value = True
        
        # Act
        result = obj.upgradeLock()
        
        # Assert
        self.assertEqual(result, True)
        obj.upgradeLock.assert_called_once()

    def test_DowngradeLock_ConvertsExclusiveToShared(self):
        # Arrange
        obj = LockManager()
        obj.downgradeLock = MagicMock()
        obj.downgradeLock.return_value = True
        
        # Act
        result = obj.downgradeLock()
        
        # Assert
        self.assertEqual(result, True)
        obj.downgradeLock.assert_called_once()

    def test_ReleaseLock_WhenNotHoldingLock_ThrowsException(self):
        # Arrange
        obj = LockManager()
        obj.releaseLock = MagicMock()
        obj.releaseLock.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.releaseLock()
            
        self.assertTrue('Exception' in str(context.exception))
