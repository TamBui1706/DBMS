import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.DatabaseObjectManagement.schema_manager import SchemaManager

class TestSchemaManager(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeSchemaManager(self):
        pass

    def test_CreateSchema_WhenValid_ShouldSucceed(self):
        pass

    def test_CreateSchema_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
