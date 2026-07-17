import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.SecurityAccessControl.role_hierarchy_resolver import RoleHierarchyResolver

class TestRoleHierarchyResolver(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeRoleHierarchyResolver(self):
        pass

    def test_ResolveRoles_WhenValid_ShouldSucceed(self):
        pass

    def test_ResolveRoles_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
