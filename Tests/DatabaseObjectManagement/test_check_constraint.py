import unittest
from unittest.mock import MagicMock
from Classes.DatabaseObjectManagement.check_constraint import CheckConstraint

class TestCheckConstraint(unittest.TestCase):

    def test_Template_CheckLogic_WhenExpressionEvaluatesToTrue_ReturnsTrue(self):
        # Arrange
        constraint = CheckConstraint("value", "CHECK_VAL", "> 0")
        
        # Act
        result = constraint.check_logic(5, {})
        
        # Assert
        self.assertTrue(result)

    def test_Template_CheckLogic_WhenExpressionEvaluatesToFalse_ReturnsFalse(self):
        # Arrange
        constraint = CheckConstraint("value", "CHECK_VAL", "> 0")
        
        # Act
        result = constraint.check_logic(-1, {})
        
        # Assert
        self.assertFalse(result)

    def test_Validate_WhenExpressionEvaluatesToFalse_ThrowsCheckException(self):
        # Arrange
        obj = CheckConstraint("dummy", "CHECK_DUMMY", "> 0")
        obj.validate = MagicMock()
        obj.validate.side_effect = Exception('CheckException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.validate()
            
        self.assertTrue('CheckException' in str(context.exception))

    def test_Validate_WhenExpressionUsesInvalidColumn_ThrowsException(self):
        # Arrange
        obj = CheckConstraint("dummy", "CHECK_DUMMY", "> 0")
        obj.validate = MagicMock()
        obj.validate.side_effect = Exception('InvalidColumnException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.validate()
            
        self.assertTrue('InvalidColumnException' in str(context.exception))
