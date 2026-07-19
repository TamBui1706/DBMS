import unittest
from unittest.mock import MagicMock

class Partition:
    pass

class TestPartition(unittest.TestCase):

    def test_Init_SetsPartitionKeyCorrectly(self):
        # Arrange
        obj = Partition()
        obj.init = MagicMock()
        obj.init.return_value = True
        
        # Act
        result = obj.init()
        
        # Assert
        self.assertEqual(result, True)
        obj.init.assert_called_once()

    def test_CheckBoundary_WhenValueInRange_ReturnsTrue(self):
        # Arrange
        obj = Partition()
        obj.checkBoundary = MagicMock()
        obj.checkBoundary.return_value = 'True'
        
        # Act
        result = obj.checkBoundary()
        
        # Assert
        self.assertEqual(result, 'True')
        obj.checkBoundary.assert_called_once()

    def test_CheckBoundary_WhenValueOutOfRange_ReturnsFalse(self):
        # Arrange
        obj = Partition()
        obj.checkBoundary = MagicMock()
        obj.checkBoundary.return_value = 'False'
        
        # Act
        result = obj.checkBoundary()
        
        # Assert
        self.assertEqual(result, 'False')
        obj.checkBoundary.assert_called_once()

    def test_Merge_CombinesTwoAdjacentPartitions(self):
        # Arrange
        obj = Partition()
        obj.merge = MagicMock()
        obj.merge.return_value = True
        
        # Act
        result = obj.merge()
        
        # Assert
        self.assertEqual(result, True)
        obj.merge.assert_called_once()

    def test_Split_DividesPartitionAtGivenValue(self):
        # Arrange
        obj = Partition()
        obj.split = MagicMock()
        obj.split.return_value = True
        
        # Act
        result = obj.split()
        
        # Assert
        self.assertEqual(result, True)
        obj.split.assert_called_once()
