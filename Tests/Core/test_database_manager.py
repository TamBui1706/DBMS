import unittest

class TestDatabaseManager(unittest.TestCase):
    def CreateDatabase_WhenNameIsValid_CreatesMetadataAndFiles(self):
        pass

    def CreateDatabase_WhenNameExists_ThrowsDuplicateDatabaseException(self):
        pass

    def CreateDatabase_WhenInvalidCharacters_ThrowsValidationException(self):
        pass

    def DropDatabase_WhenExists_RemovesAllAssociatedData(self):
        pass

    def DropDatabase_WhenInUse_ThrowsConcurrencyException(self):
        pass

