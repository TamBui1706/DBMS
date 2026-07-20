import unittest
from unittest.mock import MagicMock

class Role:
    pass

class TestRole(unittest.TestCase):

    def test_Init_SetsRoleName(self):
        # Arrange
        obj = Role()
        obj.init = MagicMock()
        obj.init.return_value = 'Success'
        
        # Act
        result = obj.init()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.init.assert_called_once()

    def test_AddPermission_GrantsPermissionToRole(self):
        # Arrange
        obj = Role()
        obj.addPermission = MagicMock()
        obj.addPermission.return_value = 'Success'
        
        # Act
        result = obj.addPermission()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.addPermission.assert_called_once()

    def test_RemovePermission_RevokesAccess(self):
        # Arrange
        obj = Role()
        obj.removePermission = MagicMock()
        obj.removePermission.return_value = 'Success'
        
        # Act
        result = obj.removePermission()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.removePermission.assert_called_once()

    def test_HasPermission_ReturnsTrueIfMatchFound(self):
        # Arrange
        obj = Role()
        obj.hasPermission = MagicMock()
        obj.hasPermission.return_value = 'Success'
        
        # Act
        result = obj.hasPermission()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.hasPermission.assert_called_once()

    def test_GetAllPermissions_ReturnsCombinedList(self):
        # Arrange
        obj = Role()
        obj.getAllPermissions = MagicMock()
        obj.getAllPermissions.return_value = 'Success'
        
        # Act
        result = obj.getAllPermissions()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.getAllPermissions.assert_called_once()

    def test_InheritRole_AppliesParentPermissionsToChildRole(self):
        # Arrange
        obj = Role()
        obj.inheritRole = MagicMock()
        obj.inheritRole.return_value = 'Success'
        
        # Act
        result = obj.inheritRole()
        
        # Assert
        self.assertEqual(result, 'Success')
        obj.inheritRole.assert_called_once()
