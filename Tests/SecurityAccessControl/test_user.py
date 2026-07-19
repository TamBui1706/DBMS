import unittest

class TestUser(unittest.TestCase):
    def test_Init_SetsUsernameAndHashedPassword(self):
        pass

    def test_AddRole_AssignsNewRoleToUser(self):
        pass

    def test_RemoveRole_TakesAwayPermissions(self):
        pass

    def test_UpdatePassword_HashesAndSavesNewPassword(self):
        pass

    def test_LockAccount_PreventsLoginAfterFailedAttempts(self):
        pass

    def test_IsLocked_ReturnsStatus(self):
        pass

    def test_HasRole_ReturnsTrueIfAssigned(self):
        pass

