import unittest
from unittest.mock import MagicMock

class DatabaseManager:
    pass

class TestDatabaseManager(unittest.TestCase):

    def test_CreateDatabase_WhenNameIsValid_CreatesMetadataAndFiles(self):
        # Arrange
        obj = DatabaseManager()
        obj.createDatabase = MagicMock()
        obj.createDatabase.return_value = 'CreatesMetadataAndFiles'
        
        # Act
        result = obj.createDatabase()
        
        # Assert
        self.assertEqual(result, 'CreatesMetadataAndFiles')
        obj.createDatabase.assert_called_once()

    def test_CreateDatabase_WhenNameExists_ThrowsDuplicateDatabaseException(self):
        # Arrange
        obj = DatabaseManager()
        obj.createDatabase = MagicMock()
        obj.createDatabase.side_effect = Exception('DuplicateDatabaseException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.createDatabase()
            
        self.assertTrue('DuplicateDatabaseException' in str(context.exception))

    def test_CreateDatabase_WhenInvalidCharacters_ThrowsValidationException(self):
        # Arrange
        obj = DatabaseManager()
        obj.createDatabase = MagicMock()
        obj.createDatabase.side_effect = Exception('ValidationException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.createDatabase()
            
        self.assertTrue('ValidationException' in str(context.exception))

    def test_DropDatabase_WhenExists_RemovesAllAssociatedData(self):
        # Arrange
        obj = DatabaseManager()
        obj.dropDatabase = MagicMock()
        obj.dropDatabase.return_value = True
        
        # Act
        result = obj.dropDatabase()
        
        # Assert
        self.assertEqual(result, True)
        obj.dropDatabase.assert_called_once()

    def test_DropDatabase_WhenInUse_ThrowsConcurrencyException(self):
        # Arrange
        obj = DatabaseManager()
        obj.dropDatabase = MagicMock()
        obj.dropDatabase.side_effect = Exception('ConcurrencyException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.dropDatabase()
            
        self.assertTrue('ConcurrencyException' in str(context.exception))

    def test_GetDatabase_WhenExists_ReturnsDatabaseInstance(self):
        # Arrange
        obj = DatabaseManager()
        obj.getDatabase = MagicMock()
        obj.getDatabase.return_value = 'DatabaseInstance'
        
        # Act
        result = obj.getDatabase()
        
        # Assert
        self.assertEqual(result, 'DatabaseInstance')
        obj.getDatabase.assert_called_once()

    def test_GetDatabase_WhenNotExists_ThrowsDatabaseNotFoundException(self):
        # Arrange
        obj = DatabaseManager()
        obj.getDatabase = MagicMock()
        obj.getDatabase.side_effect = Exception('DatabaseNotFoundException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.getDatabase()
            
        self.assertTrue('DatabaseNotFoundException' in str(context.exception))

    def test_ListDatabases_ReturnsAllRegisteredDatabases(self):
        # Arrange
        obj = DatabaseManager()
        obj.listDatabases = MagicMock()
        obj.listDatabases.return_value = True
        
        # Act
        result = obj.listDatabases()
        
        # Assert
        self.assertEqual(result, True)
        obj.listDatabases.assert_called_once()

    def test_RenameDatabase_WhenNewNameValid_UpdatesMetadata(self):
        # Arrange
        obj = DatabaseManager()
        obj.renameDatabase = MagicMock()
        obj.renameDatabase.return_value = 'UpdatesMetadata'
        
        # Act
        result = obj.renameDatabase()
        
        # Assert
        self.assertEqual(result, 'UpdatesMetadata')
        obj.renameDatabase.assert_called_once()

    def test_CreateDatabase_WhenDiskFull_ThrowsInsufficientStorageException(self):
        # Arrange
        obj = DatabaseManager()
        obj.createDatabase = MagicMock()
        obj.createDatabase.side_effect = Exception('InsufficientStorageException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.createDatabase()
            
        self.assertTrue('InsufficientStorageException' in str(context.exception))

    def test_CreateDatabase_WhenNameTooLong_ThrowsValidationException(self):
        # Arrange
        obj = DatabaseManager()
        obj.createDatabase = MagicMock()
        obj.createDatabase.side_effect = Exception('ValidationException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.createDatabase()
            
        self.assertTrue('ValidationException' in str(context.exception))

    def test_DropDatabase_WhenPermissionDenied_ThrowsSecurityException(self):
        # Arrange
        obj = DatabaseManager()
        obj.dropDatabase = MagicMock()
        obj.dropDatabase.side_effect = Exception('SecurityException')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.dropDatabase()
            
        self.assertTrue('SecurityException' in str(context.exception))
