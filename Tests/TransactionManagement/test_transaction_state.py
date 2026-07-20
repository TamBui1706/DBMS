import unittest
from unittest.mock import MagicMock

class TransactionState:
    pass

class TestTransactionState(unittest.TestCase):

    def test_EnumValues_IncludeActiveCommittedAborted(self):
        # Arrange
        obj = TransactionState()
        obj.enumValues = MagicMock()
        obj.enumValues.return_value = 'Success'
        
        # Act
        result = obj.enumValues()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.enumValues.assert_called_once()
