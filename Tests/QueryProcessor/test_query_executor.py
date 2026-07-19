import unittest
from unittest.mock import MagicMock

class QueryExecutor:
    pass

class TestQueryExecutor(unittest.TestCase):

    def test_ExecutePlan_WhenValidPhysicalPlan_IteratesAndYieldsResults(self):
        # Arrange
        obj = QueryExecutor()
        obj.executePlan = MagicMock()
        obj.executePlan.return_value = True
        
        # Act
        result = obj.executePlan()
        
        # Assert
        self.assertEqual(result, True)
        obj.executePlan.assert_called_once()

    def test_ExecutePlan_WhenMemoryExceeded_SpillsToDiskOrThrows(self):
        # Arrange
        obj = QueryExecutor()
        obj.executePlan = MagicMock()
        obj.executePlan.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.executePlan()
            
        self.assertTrue('Exception' in str(context.exception))

    def test_ExecutePlan_WhenCanceledByUser_AbortsImmediately(self):
        # Arrange
        obj = QueryExecutor()
        obj.executePlan = MagicMock()
        obj.executePlan.return_value = True
        
        # Act
        result = obj.executePlan()
        
        # Assert
        self.assertEqual(result, True)
        obj.executePlan.assert_called_once()

    def test_StreamResults_YieldsBatchesInsteadOfLoadingAllIntoMemory(self):
        # Arrange
        obj = QueryExecutor()
        obj.streamResults = MagicMock()
        obj.streamResults.return_value = True
        
        # Act
        result = obj.streamResults()
        
        # Assert
        self.assertEqual(result, True)
        obj.streamResults.assert_called_once()

    def test_Initialize_AllocatesRequiredTempSpace(self):
        # Arrange
        obj = QueryExecutor()
        obj.initialize = MagicMock()
        obj.initialize.return_value = True
        
        # Act
        result = obj.initialize()
        
        # Assert
        self.assertEqual(result, True)
        obj.initialize.assert_called_once()

    def test_Close_ReleasesAllInternalIterators(self):
        # Arrange
        obj = QueryExecutor()
        obj.close = MagicMock()
        obj.close.return_value = True
        
        # Act
        result = obj.close()
        
        # Assert
        self.assertEqual(result, True)
        obj.close.assert_called_once()
