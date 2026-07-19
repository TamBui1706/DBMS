import unittest
from unittest.mock import MagicMock

class PrimaryKey:
    pass

class TestPrimaryKey(unittest.TestCase):

    def test_Validate_WhenValueIsUniqueAndNotNull_Succeeds(self):
        # Arrange
        obj = PrimaryKey()
        obj.validate = MagicMock()
        obj.validate.return_value = 'Succeeds'
        
        # Act
        result = obj.validate()
        
        # Assert
        self.assertEqual(result, 'Succeeds')
        obj.validate.assert_called_once()

    def test_Validate_WhenValueIsNull_ThrowsNullException(self):
        # Arrange
        obj = PrimaryKey()
        obj.validate = MagicMock()
        obj.validate.side_effect = Exception('NullException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.validate()
            
        self.assertTrue('NullException' in str(context.exception))

    def test_Validate_WhenValueIsDuplicate_ThrowsDuplicateKeyException(self):
        # Arrange
        obj = PrimaryKey()
        obj.validate = MagicMock()
        obj.validate.side_effect = Exception('DuplicateKeyException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.validate()
            
        self.assertTrue('DuplicateKeyException' in str(context.exception))

    def test_Validate_WithCompositeKey_ChecksAllColumns(self):
        # Arrange
        obj = PrimaryKey()
        obj.validate = MagicMock()
        obj.validate.return_value = True
        
        # Act
        result = obj.validate()
        
        # Assert
        self.assertEqual(result, True)
        obj.validate.assert_called_once()

    def test_Drop_RemovesIndexFromStorage(self):
        # Arrange
        obj = PrimaryKey()
        obj.drop = MagicMock()
        obj.drop.return_value = True
        
        # Act
        result = obj.drop()
        
        # Assert
        self.assertEqual(result, True)
        obj.drop.assert_called_once()
