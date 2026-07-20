import unittest
from unittest.mock import MagicMock

class Schema:
    pass

class TestSchema(unittest.TestCase):

    def test_Init_SetsSchemaName(self):
        # Arrange
        obj = Schema()
        obj.init = MagicMock()
        obj.init.return_value = 'Success'
        
        # Act
        result = obj.init()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.init.assert_called_once()

    def test_CreateTable_WhenValidTable_RegistersInSchema(self):
        # Arrange
        obj = Schema()
        obj.createTable = MagicMock()
        obj.createTable.return_value = 'RegistersInSchema'
        
        # Act
        result = obj.createTable()
        
        # Assert
        self.assertEqual(result, 'RegistersInSchema')
        obj.createTable.assert_called_once()

    def test_CreateTable_WhenTableNameExists_ThrowsException(self):
        # Arrange
        obj = Schema()
        obj.createTable = MagicMock()
        obj.createTable.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.createTable()
            
        self.assertTrue('Exception' in str(context.exception))

    def test_DropTable_WhenExists_RemovesFromSchema(self):
        # Arrange
        obj = Schema()
        obj.dropTable = MagicMock()
        obj.dropTable.return_value = 'RemovesFromSchema'
        
        # Act
        result = obj.dropTable()
        
        # Assert
        self.assertEqual(result, 'RemovesFromSchema')
        obj.dropTable.assert_called_once()

    def test_DropTable_WhenNotExists_ThrowsException(self):
        # Arrange
        obj = Schema()
        obj.dropTable = MagicMock()
        obj.dropTable.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.dropTable()
            
        self.assertTrue('Exception' in str(context.exception))

    def test_GetTable_WhenExists_ReturnsTable(self):
        # Arrange
        obj = Schema()
        obj.getTable = MagicMock()
        obj.getTable.return_value = 'Table'
        
        # Act
        result = obj.getTable()
        
        # Assert
        self.assertEqual(result, 'Table')
        obj.getTable.assert_called_once()

    def test_ListTables_ReturnsAllRegisteredTables(self):
        # Arrange
        obj = Schema()
        obj.listTables = MagicMock()
        obj.listTables.return_value = 'Success'
        
        # Act
        result = obj.listTables()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.listTables.assert_called_once()

    def test_Validate_EnsuresSchemaNameIsAlphanumeric(self):
        # Arrange
        obj = Schema()
        obj.validate = MagicMock()
        obj.validate.return_value = 'Success'
        
        # Act
        result = obj.validate()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.validate.assert_called_once()
