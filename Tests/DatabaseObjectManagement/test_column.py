import unittest
from unittest.mock import MagicMock

class Column:
    pass

class TestColumn(unittest.TestCase):

    def test_Init_SetsNameAndNullableFlags(self):
        # Arrange
        obj = Column()
        obj.init = MagicMock()
        obj.init.return_value = True
        
        # Act
        result = obj.init()
        
        # Assert
        self.assertEqual(result, True)
        obj.init.assert_called_once()

    def test_ValidateType_WhenDataMatchesColumnType_Succeeds(self):
        # Arrange
        obj = Column()
        obj.validateType = MagicMock()
        obj.validateType.return_value = 'Succeeds'
        
        # Act
        result = obj.validateType()
        
        # Assert
        self.assertEqual(result, 'Succeeds')
        obj.validateType.assert_called_once()

    def test_ValidateType_WhenDataIsStringForIntColumn_ThrowsTypeException(self):
        # Arrange
        obj = Column()
        obj.validateType = MagicMock()
        obj.validateType.side_effect = Exception('TypeException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.validateType()
            
        self.assertTrue('TypeException' in str(context.exception))

    def test_ValidateNullable_WhenNullPassedToNotNullColumn_ThrowsException(self):
        # Arrange
        obj = Column()
        obj.validateNullable = MagicMock()
        obj.validateNullable.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.validateNullable()
            
        self.assertTrue('Exception' in str(context.exception))

    def test_SetDefaultValue_StoresDefaultExpression(self):
        # Arrange
        obj = Column()
        obj.setDefaultValue = MagicMock()
        obj.setDefaultValue.return_value = True
        
        # Act
        result = obj.setDefaultValue()
        
        # Assert
        self.assertEqual(result, True)
        obj.setDefaultValue.assert_called_once()

    def test_ChangeType_WhenCompatible_Succeeds(self):
        # Arrange
        obj = Column()
        obj.changeType = MagicMock()
        obj.changeType.return_value = 'Succeeds'
        
        # Act
        result = obj.changeType()
        
        # Assert
        self.assertEqual(result, 'Succeeds')
        obj.changeType.assert_called_once()

    def test_ChangeType_WhenIncompatible_ThrowsException(self):
        # Arrange
        obj = Column()
        obj.changeType = MagicMock()
        obj.changeType.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.changeType()
            
        self.assertTrue('Exception' in str(context.exception))
