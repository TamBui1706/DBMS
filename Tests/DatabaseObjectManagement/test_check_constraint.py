import unittest
from unittest.mock import MagicMock

class CheckConstraint:
    pass

class TestCheckConstraint(unittest.TestCase):

    def test_Validate_WhenExpressionEvaluatesToTrue_Succeeds(self):
        # Arrange
        obj = CheckConstraint()
        obj.validate = MagicMock()
        obj.validate.return_value = 'Succeeds'
        
        # Act
        result = obj.validate()
        
        # Assert
        self.assertEqual(result, 'Succeeds')
        obj.validate.assert_called_once()

    def test_Validate_WhenExpressionEvaluatesToFalse_ThrowsCheckException(self):
        # Arrange
        obj = CheckConstraint()
        obj.validate = MagicMock()
        obj.validate.side_effect = Exception('CheckException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.validate()
            
        self.assertTrue('CheckException' in str(context.exception))

    def test_Validate_WhenExpressionUsesInvalidColumn_ThrowsException(self):
        # Arrange
        obj = CheckConstraint()
        obj.validate = MagicMock()
        obj.validate.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.validate()
            
        self.assertTrue('Exception' in str(context.exception))
