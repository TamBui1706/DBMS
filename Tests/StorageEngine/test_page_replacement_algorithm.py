import unittest
from unittest.mock import MagicMock

class PageReplacementAlgorithm:
    pass

class TestPageReplacementAlgorithm(unittest.TestCase):

    def test_Instantiation_OfInterface_FailsWithTypeError(self):
        # Arrange
        obj = PageReplacementAlgorithm()
        obj.instantiation = MagicMock()
        obj.instantiation.side_effect = Exception('Exception')
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            obj.instantiation()
            
        self.assertTrue('Exception' in str(context.exception))
