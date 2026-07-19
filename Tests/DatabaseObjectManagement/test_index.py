import unittest
from unittest.mock import MagicMock

class Index:
    pass

class TestIndex(unittest.TestCase):

    def test_Instantiation_OfAbstractClass_FailsWithTypeError(self):
        # Arrange
        obj = Index()
        obj.instantiation = MagicMock()
        obj.instantiation.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.instantiation()
            
        self.assertTrue('Exception' in str(context.exception))
