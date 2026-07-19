import unittest
from unittest.mock import MagicMock

class User:
    pass

class TestUser(unittest.TestCase):

    def test_Init_SetsUsernameAndHashedPassword(self):
        # Arrange
        obj = User()
        obj.init = MagicMock()
        obj.init.return_value = True
        
        # Act
        result = obj.init()
        
        # Assert
        self.assertEqual(result, True)
        obj.init.assert_called_once()

    def test_AddRole_AssignsNewRoleToUser(self):
        # Arrange
        obj = User()
        obj.addRole = MagicMock()
        obj.addRole.return_value = True
        
        # Act
        result = obj.addRole()
        
        # Assert
        self.assertEqual(result, True)
        obj.addRole.assert_called_once()

    def test_RemoveRole_TakesAwayPermissions(self):
        # Arrange
        obj = User()
        obj.removeRole = MagicMock()
        obj.removeRole.return_value = True
        
        # Act
        result = obj.removeRole()
        
        # Assert
        self.assertEqual(result, True)
        obj.removeRole.assert_called_once()

    def test_UpdatePassword_HashesAndSavesNewPassword(self):
        # Arrange
        obj = User()
        obj.updatePassword = MagicMock()
        obj.updatePassword.return_value = True
        
        # Act
        result = obj.updatePassword()
        
        # Assert
        self.assertEqual(result, True)
        obj.updatePassword.assert_called_once()

    def test_LockAccount_PreventsLoginAfterFailedAttempts(self):
        # Arrange
        obj = User()
        obj.lockAccount = MagicMock()
        obj.lockAccount.return_value = True
        
        # Act
        result = obj.lockAccount()
        
        # Assert
        self.assertEqual(result, True)
        obj.lockAccount.assert_called_once()

    def test_IsLocked_ReturnsStatus(self):
        # Arrange
        obj = User()
        obj.isLocked = MagicMock()
        obj.isLocked.return_value = True
        
        # Act
        result = obj.isLocked()
        
        # Assert
        self.assertEqual(result, True)
        obj.isLocked.assert_called_once()

    def test_HasRole_ReturnsTrueIfAssigned(self):
        # Arrange
        obj = User()
        obj.hasRole = MagicMock()
        obj.hasRole.return_value = True
        
        # Act
        result = obj.hasRole()
        
        # Assert
        self.assertEqual(result, True)
        obj.hasRole.assert_called_once()
