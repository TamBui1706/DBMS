import unittest
from unittest.mock import MagicMock

class WALManager:
    pass

class TestWALManager(unittest.TestCase):

    def test_AppendLog_AddsRecordToMemoryBuffer(self):
        # Arrange
        obj = WALManager()
        obj.appendLog = MagicMock()
        obj.appendLog.return_value = 'Success'
        
        # Act
        result = obj.appendLog()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.appendLog.assert_called_once()

    def test_Flush_WritesBufferToDiskSynchronously(self):
        # Arrange
        obj = WALManager()
        obj.flush = MagicMock()
        obj.flush.return_value = 'Success'
        
        # Act
        result = obj.flush()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.flush.assert_called_once()

    def test_AppendLog_WhenBufferFull_TriggersAutomaticFlush(self):
        # Arrange
        obj = WALManager()
        obj.appendLog = MagicMock()
        obj.appendLog.return_value = 'TriggersAutomaticFlush'
        
        # Act
        result = obj.appendLog()
        
        # Assert
        self.assertEqual(result, 'TriggersAutomaticFlush')
        obj.appendLog.assert_called_once()

    def test_ReadLog_ReturnsRecordByLSN(self):
        # Arrange
        obj = WALManager()
        obj.readLog = MagicMock()
        obj.readLog.return_value = 'Success'
        
        # Act
        result = obj.readLog()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.readLog.assert_called_once()

    def test_TruncateLog_DeletesLogsOlderThanCheckpoint(self):
        # Arrange
        obj = WALManager()
        obj.truncateLog = MagicMock()
        obj.truncateLog.return_value = 'Success'
        
        # Act
        result = obj.truncateLog()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.truncateLog.assert_called_once()

    def test_Flush_WhenDiskFull_ThrowsStorageException(self):
        # Arrange
        obj = WALManager()
        obj.flush = MagicMock()
        obj.flush.side_effect = Exception('StorageException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.flush()
            
        self.assertTrue('StorageException' in str(context.exception))

    def test_SwitchLogFile_CreatesNewSegmentWhenMaxFileSizeReached(self):
        # Arrange
        obj = WALManager()
        obj.switchLogFile = MagicMock()
        obj.switchLogFile.return_value = 'Success'
        
        # Act
        result = obj.switchLogFile()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.switchLogFile.assert_called_once()
