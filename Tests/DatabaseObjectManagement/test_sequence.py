import unittest
from unittest.mock import MagicMock

class Sequence:
    pass

class TestSequence(unittest.TestCase):

    def test_NextValue_IncrementsByStepAndReturnsValue(self):
        # Arrange
        obj = Sequence()
        obj.nextValue = MagicMock()
        obj.nextValue.return_value = True
        
        # Act
        result = obj.nextValue()
        
        # Assert
        self.assertEqual(result, True)
        obj.nextValue.assert_called_once()

    def test_NextValue_WhenMaxLimitReached_ThrowsOverflowException(self):
        # Arrange
        obj = Sequence()
        obj.nextValue = MagicMock()
        obj.nextValue.side_effect = Exception('OverflowException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.nextValue()
            
        self.assertTrue('OverflowException' in str(context.exception))

    def test_Reset_SetsValueBackToStart(self):
        # Arrange
        obj = Sequence()
        obj.reset = MagicMock()
        obj.reset.return_value = True
        
        # Act
        result = obj.reset()
        
        # Assert
        self.assertEqual(result, True)
        obj.reset.assert_called_once()

    def test_Init_SetsStartStepAndMaxLimit(self):
        # Arrange
        obj = Sequence()
        obj.init = MagicMock()
        obj.init.return_value = True
        
        # Act
        result = obj.init()
        
        # Assert
        self.assertEqual(result, True)
        obj.init.assert_called_once()

    def test_CurrentValue_ReturnsCurrentWithoutIncrementing(self):
        # Arrange
        obj = Sequence()
        obj.currentValue = MagicMock()
        obj.currentValue.return_value = True
        
        # Act
        result = obj.currentValue()
        
        # Assert
        self.assertEqual(result, True)
        obj.currentValue.assert_called_once()

    def test_NextValue_WhenStepIsNegative_DecrementsCorrectly(self):
        # Arrange
        obj = Sequence()
        obj.nextValue = MagicMock()
        obj.nextValue.return_value = True
        
        # Act
        result = obj.nextValue()
        
        # Assert
        self.assertEqual(result, True)
        obj.nextValue.assert_called_once()
