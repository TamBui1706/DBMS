import unittest

class TestSchema(unittest.TestCase):
    def test_Init_SetsSchemaName(self):
        pass

    def test_CreateTable_WhenValidTable_RegistersInSchema(self):
        pass

    def test_CreateTable_WhenTableNameExists_ThrowsException(self):
        pass

    def test_DropTable_WhenExists_RemovesFromSchema(self):
        pass

    def test_DropTable_WhenNotExists_ThrowsException(self):
        pass

    def test_GetTable_WhenExists_ReturnsTable(self):
        pass

    def test_ListTables_ReturnsAllRegisteredTables(self):
        pass

    def test_Validate_EnsuresSchemaNameIsAlphanumeric(self):
        pass

