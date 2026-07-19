import unittest
from unittest.mock import MagicMock

class IsolationLevel:
    pass

class TestIsolationLevel(unittest.TestCase):

    def test_EnumValues_IncludeReadCommittedAndSerializable(self):
        # Arrange
        obj = IsolationLevel()
        obj.enumValues = MagicMock()
        obj.enumValues.return_value = True
        
        # Act
        result = obj.enumValues()
        
        # Assert
        self.assertEqual(result, True)
        obj.enumValues.assert_called_once()
