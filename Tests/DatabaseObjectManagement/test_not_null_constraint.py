import unittest
from Classes.DatabaseObjectManagement.not_null_constraint import NotNullConstraint
from Classes.DatabaseObjectManagement.exceptions import ConstraintViolationException

class TestNotNullConstraint(unittest.TestCase):

    def test_Template_CheckLogic_WhenValueIsNone_ReturnsFalse(self):
        # Arrange
        constraint = NotNullConstraint("email")
        
        # Act
        result = constraint.check_logic(None, {})
        
        # Assert
        self.assertFalse(result)

    def test_Template_CheckLogic_WhenValueIsNotNull_ReturnsTrue(self):
        # Arrange
        constraint = NotNullConstraint("email")
        
        # Act
        result = constraint.check_logic("user@example.com", {})
        
        # Assert
        self.assertTrue(result)

    def test_Template_Validate_WhenValueIsNone_RaisesException(self):
        # Arrange
        constraint = NotNullConstraint("email")
        
        # Act & Assert
        with self.assertRaises(ConstraintViolationException) as context:
            constraint.validate(None, {})
        
        self.assertIn("violated constraint 'NOT NULL'", str(context.exception))
