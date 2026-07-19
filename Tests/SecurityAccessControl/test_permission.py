import unittest

class TestPermission(unittest.TestCase):
    def test_Init_SetsResourceAndActionType(self):
        pass

    def test_Matches_WhenActionAndResourceAlign_ReturnsTrue(self):
        pass

    def test_Matches_WhenWildcardResource_ReturnsTrueForAll(self):
        pass

    def test_ToString_FormatsPermissionForLogging(self):
        pass

    def test_Matches_WhenActionIsDeny_OverridesGrant(self):
        pass

