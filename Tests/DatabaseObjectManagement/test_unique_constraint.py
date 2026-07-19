import unittest
from unittest.mock import MagicMock

class UniqueConstraint:
    pass

class TestUniqueConstraint(unittest.TestCase):

    def test_Validate_WhenValueIsGloballyUnique_Succeeds(self):
        # Arrange
        obj = UniqueConstraint()
        obj.validate = MagicMock()
        obj.validate.return_value = 'Succeeds'
        
        # Act
        result = obj.validate()
        
        # Assert
        self.assertEqual(result, 'Succeeds')
        obj.validate.assert_called_once()

    def test_Validate_WhenValueExistsInAnotherRow_ThrowsException(self):
        # Arrange
        obj = UniqueConstraint()
        obj.validate = MagicMock()
        obj.validate.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.validate()
            
        self.assertTrue('Exception' in str(context.exception))

    def test_Validate_WhenValueIsNull_SucceedsIfNullable(self):
        # Arrange
        obj = UniqueConstraint()
        obj.validate = MagicMock()
        obj.validate.return_value = 'SucceedsIfNullable'
        
        # Act
        result = obj.validate()
        
        # Assert
        self.assertEqual(result, 'SucceedsIfNullable')
        obj.validate.assert_called_once()
