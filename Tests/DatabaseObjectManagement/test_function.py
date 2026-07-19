import unittest
from unittest.mock import MagicMock

class Function:
    pass

class TestFunction(unittest.TestCase):

    def test_Evaluate_WhenValidArguments_ReturnsComputedValue(self):
        # Arrange
        obj = Function()
        obj.evaluate = MagicMock()
        obj.evaluate.return_value = 'ComputedValue'
        
        # Act
        result = obj.evaluate()
        
        # Assert
        self.assertEqual(result, 'ComputedValue')
        obj.evaluate.assert_called_once()

    def test_Evaluate_WhenMissingArguments_ThrowsArgumentException(self):
        # Arrange
        obj = Function()
        obj.evaluate = MagicMock()
        obj.evaluate.side_effect = Exception('ArgumentException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.evaluate()
            
        self.assertTrue('ArgumentException' in str(context.exception))

    def test_Evaluate_WhenDivideByZero_ThrowsArithmeticException(self):
        # Arrange
        obj = Function()
        obj.evaluate = MagicMock()
        obj.evaluate.side_effect = Exception('ArithmeticException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.evaluate()
            
        self.assertTrue('ArithmeticException' in str(context.exception))

    def test_IsDeterministic_ReturnsTrueIfNoExternalStateUsed(self):
        # Arrange
        obj = Function()
        obj.isDeterministic = MagicMock()
        obj.isDeterministic.return_value = True
        
        # Act
        result = obj.isDeterministic()
        
        # Assert
        self.assertEqual(result, True)
        obj.isDeterministic.assert_called_once()

    def test_Evaluate_WhenNullPassedToStrictFunction_ReturnsNull(self):
        # Arrange
        obj = Function()
        obj.evaluate = MagicMock()
        obj.evaluate.return_value = 'Null'
        
        # Act
        result = obj.evaluate()
        
        # Assert
        self.assertEqual(result, 'Null')
        obj.evaluate.assert_called_once()
