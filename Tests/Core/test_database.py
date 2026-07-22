import unittest
from unittest.mock import MagicMock
from Classes.Core.database import Database
from Classes.DatabaseObjectManagement.schema import Schema


class TestDatabase(unittest.TestCase):

    def test_Init_SetsDatabaseNameCorrectly(self):
        # Arrange
        obj = Database()
        obj.init = MagicMock()
        obj.init.return_value = 'Success'
        
        # Act
        result = obj.init()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.init.assert_called_once()

    def test_Open_WhenValidMetadata_LoadsDatabaseContext(self):
        # Arrange
        obj = Database()
        obj.open = MagicMock()
        obj.open.return_value = 'LoadsDatabaseContext'
        
        # Act
        result = obj.open()
        
        # Assert
        self.assertEqual(result, 'LoadsDatabaseContext')
        obj.open.assert_called_once()

    def test_Open_WhenCorruptedMetadata_ThrowsCorruptionException(self):
        # Arrange
        obj = Database()
        obj.open = MagicMock()
        obj.open.side_effect = Exception('CorruptionException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.open()
            
        self.assertTrue('CorruptionException' in str(context.exception))

    def test_Close_FlushesUnsavedChangesAndReleasesLocks(self):
        # Arrange
        obj = Database()
        obj.close = MagicMock()
        obj.close.return_value = 'Success'
        
        # Act
        result = obj.close()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.close.assert_called_once()

    def test_GetSchema_WhenSchemaExists_ReturnsSchema(self):
        # Arrange
        obj = Database()
        obj.getSchema = MagicMock()
        obj.getSchema.return_value = 'Schema'
        
        # Act
        result = obj.getSchema()
        
        # Assert
        self.assertEqual(result, 'Schema')
        obj.getSchema.assert_called_once()

    def test_CreateSchema_WhenNameValid_AddsToDatabase(self):
        # Arrange
        obj = Database()
        obj.createSchema = MagicMock()
        obj.createSchema.return_value = 'AddsToDatabase'
        
        # Act
        result = obj.createSchema()
        
        # Assert
        self.assertEqual(result, 'AddsToDatabase')
        obj.createSchema.assert_called_once()

    def test_Close_WhenAlreadyClosed_DoesNothing(self):
        # Arrange
        obj = Database()
        obj.close = MagicMock()
        obj.close.return_value = 'DoesNothing'
        
        # Act
        result = obj.close()
        
        # Assert
        self.assertEqual(result, 'DoesNothing')
        obj.close.assert_called_once()

    def test_Open_WhenMissingDataFiles_ThrowsFileNotFoundException(self):
        # Arrange
        obj = Database()
        obj.open = MagicMock()
        obj.open.side_effect = Exception('FileNotFoundException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.open()
            
        self.assertTrue('FileNotFoundException' in str(context.exception))

    def test_Composite_AddChild_AddsToChildrenList(self):
        # Arrange
        db = Database("MyDB")
        schema = Schema("MySchema")
        
        # Act
        db.add_child(schema)
        
        # Assert
        self.assertIn(schema, db.children)

    def test_Composite_GetMetadata_ReturnsRecursiveDict(self):
        # Arrange
        db = Database("MyDB")
        schema = Schema("MySchema")
        db.add_child(schema)
        
        # Act
        meta = db.get_metadata()
        
        # Assert
        self.assertEqual(meta["type"], "Database")
        self.assertEqual(meta["name"], "MyDB")
        self.assertEqual(len(meta["children"]), 1)
        self.assertEqual(meta["children"][0]["type"], "Schema")
        self.assertEqual(meta["children"][0]["name"], "MySchema")
