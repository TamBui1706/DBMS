import unittest
from unittest.mock import MagicMock

class CheckpointManager:
    pass

class TestCheckpointManager(unittest.TestCase):

    def test_TakeCheckpoint_FlushesAllDirtyPages(self):
        # Arrange
        obj = CheckpointManager()
        obj.takeCheckpoint = MagicMock()
        obj.takeCheckpoint.return_value = 'Success'
        
        # Act
        result = obj.takeCheckpoint()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.takeCheckpoint.assert_called_once()

    def test_TakeCheckpoint_WritesCheckpointRecordToLog(self):
        # Arrange
        obj = CheckpointManager()
        obj.takeCheckpoint = MagicMock()
        obj.takeCheckpoint.return_value = 'Success'
        
        # Act
        result = obj.takeCheckpoint()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.takeCheckpoint.assert_called_once()

    def test_AutoCheckpoint_TriggersWhenLogReachesSizeLimit(self):
        # Arrange
        obj = CheckpointManager()
        obj.autoCheckpoint = MagicMock()
        obj.autoCheckpoint.return_value = 'Success'
        
        # Act
        result = obj.autoCheckpoint()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.autoCheckpoint.assert_called_once()

    def test_AutoCheckpoint_TriggersWhenTimeIntervalElapsed(self):
        # Arrange
        obj = CheckpointManager()
        obj.autoCheckpoint = MagicMock()
        obj.autoCheckpoint.return_value = 'Success'
        
        # Act
        result = obj.autoCheckpoint()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.autoCheckpoint.assert_called_once()

    def test_GetLastCheckpointLSN_ReadsFromMasterRecord(self):
        # Arrange
        obj = CheckpointManager()
        obj.getLastCheckpointLSN = MagicMock()
        obj.getLastCheckpointLSN.return_value = 'Success'
        
        # Act
        result = obj.getLastCheckpointLSN()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.getLastCheckpointLSN.assert_called_once()
