import unittest

class TestUniqueConstraint(unittest.TestCase):
    def test_Validate_WhenValueIsGloballyUnique_Succeeds(self):
        pass

    def test_Validate_WhenValueExistsInAnotherRow_ThrowsException(self):
        pass

    def test_Validate_WhenValueIsNull_SucceedsIfNullable(self):
        pass

