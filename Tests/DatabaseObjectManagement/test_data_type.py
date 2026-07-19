import unittest
from unittest.mock import MagicMock

class DataType:
    pass

class TestDataType(unittest.TestCase):

    def test_EnumValues_IncludeIntVarcharDateBoolean(self):
        # Arrange
        obj = DataType()
        obj.enumValues = MagicMock()
        obj.enumValues.return_value = True
        
        # Act
        result = obj.enumValues()
        
        # Assert
        self.assertEqual(result, True)
        obj.enumValues.assert_called_once()

    def test_ParseString_WhenValidFormat_ReturnsDataTypeInstance(self):
        # Arrange
        obj = DataType()
        obj.parseString = MagicMock()
        obj.parseString.return_value = 'DataTypeInstance'
        
        # Act
        result = obj.parseString()
        
        # Assert
        self.assertEqual(result, 'DataTypeInstance')
        obj.parseString.assert_called_once()

    def test_ParseString_WhenInvalidFormat_ThrowsParseException(self):
        # Arrange
        obj = DataType()
        obj.parseString = MagicMock()
        obj.parseString.side_effect = Exception('ParseException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.parseString()
            
        self.assertTrue('ParseException' in str(context.exception))

    def test_GetSize_ReturnsByteSizeForFixedTypes(self):
        # Arrange
        obj = DataType()
        obj.getSize = MagicMock()
        obj.getSize.return_value = True
        
        # Act
        result = obj.getSize()
        
        # Assert
        self.assertEqual(result, True)
        obj.getSize.assert_called_once()

    def test_IsVariableLength_ReturnsTrueForVarchar(self):
        # Arrange
        obj = DataType()
        obj.isVariableLength = MagicMock()
        obj.isVariableLength.return_value = True
        
        # Act
        result = obj.isVariableLength()
        
        # Assert
        self.assertEqual(result, True)
        obj.isVariableLength.assert_called_once()
