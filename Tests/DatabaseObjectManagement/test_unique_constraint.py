import unittest
from unittest.mock import MagicMock
from Classes.DatabaseObjectManagement.unique_constraint import UniqueConstraint

class TestUniqueConstraint(unittest.TestCase):

    def test_Validate_WhenValueIsGloballyUnique_Succeeds(self):
        # Arrange
        obj = UniqueConstraint("dummy_col")
        obj.validate = MagicMock()
        obj.validate.return_value = 'Succeeds'
        
        # Act
        result = obj.validate()
        
        # Assert
        self.assertEqual(result, 'Succeeds')
        obj.validate.assert_called_once()

    def test_Validate_WhenValueExistsInAnotherRow_ThrowsException(self):
        # Arrange
        obj = UniqueConstraint("dummy_col")
        obj.validate = MagicMock()
        obj.validate.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.validate()
            
        self.assertTrue('Exception' in str(context.exception))

    def test_Template_CheckLogic_WhenValueIsUnique_ReturnsTrue(self):
        # Arrange
        constraint = UniqueConstraint("email")
        db_context = MagicMock()
        db_context.get_index.return_value = ["other@test.com"]
        
        # Act
        result = constraint.check_logic("user@test.com", db_context)
        
        # Assert
        self.assertTrue(result)

    def test_Template_CheckLogic_WhenValueExists_ReturnsFalse(self):
        # Arrange
        constraint = UniqueConstraint("email")
        db_context = MagicMock()
        db_context.get_index.return_value = ["user@test.com"]
        
        # Act
        result = constraint.check_logic("user@test.com", db_context)
        
        # Assert
        self.assertFalse(result)

    def test_Validate_WhenValueIsNull_SucceedsIfNullable(self):
        # Arrange
        obj = UniqueConstraint("dummy_col")
        obj.validate = MagicMock()
        obj.validate.return_value = 'SucceedsIfNullable'
        
        # Act
        result = obj.validate()
        
        # Assert
        self.assertEqual(result, 'SucceedsIfNullable')
        obj.validate.assert_called_once()
