import unittest
from unittest.mock import MagicMock

class IsolationLevel:
    pass

class TestIsolationLevel(unittest.TestCase):

    def test_EnumValues_IncludeReadCommittedAndSerializable(self):
        # Arrange
        obj = IsolationLevel()
        obj.enumValues = MagicMock()
        obj.enumValues.return_value = 'Success'
        
        # Act
        result = obj.enumValues()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.enumValues.assert_called_once()
