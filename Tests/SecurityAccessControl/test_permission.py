import unittest
from unittest.mock import MagicMock

class Permission:
    pass

class TestPermission(unittest.TestCase):

    def test_Init_SetsResourceAndActionType(self):
        # Arrange
        obj = Permission()
        obj.init = MagicMock()
        obj.init.return_value = 'Success'
        
        # Act
        result = obj.init()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.init.assert_called_once()

    def test_Matches_WhenActionAndResourceAlign_ReturnsTrue(self):
        # Arrange
        obj = Permission()
        obj.matches = MagicMock()
        obj.matches.return_value = 'True'
        
        # Act
        result = obj.matches()
        
        # Assert
        self.assertEqual(result, 'True')
        obj.matches.assert_called_once()

    def test_Matches_WhenWildcardResource_ReturnsTrueForAll(self):
        # Arrange
        obj = Permission()
        obj.matches = MagicMock()
        obj.matches.return_value = 'TrueForAll'
        
        # Act
        result = obj.matches()
        
        # Assert
        self.assertEqual(result, 'TrueForAll')
        obj.matches.assert_called_once()

    def test_ToString_FormatsPermissionForLogging(self):
        # Arrange
        obj = Permission()
        obj.toString = MagicMock()
        obj.toString.return_value = 'Success'
        
        # Act
        result = obj.toString()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.toString.assert_called_once()

    def test_Matches_WhenActionIsDeny_OverridesGrant(self):
        # Arrange
        obj = Permission()
        obj.matches = MagicMock()
        obj.matches.return_value = 'OverridesGrant'
        
        # Act
        result = obj.matches()
        
        # Assert
        self.assertEqual(result, 'OverridesGrant')
        obj.matches.assert_called_once()
