import unittest
from Classes.DatabaseObjectManagement.constraint import Constraint
from Classes.DatabaseObjectManagement.exceptions import ConstraintViolationException

class DummyConstraint(Constraint):
    def __init__(self, rule, should_pass=True):
        super().__init__("dummy_col", rule)
        self.should_pass = should_pass

    def check_logic(self, value, db_context):
        return self.should_pass


class TestConstraint(unittest.TestCase):

    def test_Composite_GetMetadata_ReturnsLeafDict(self):
        # Arrange
        constraint = DummyConstraint("TEST RULE")
        
        # Act
        meta = constraint.get_metadata()
        
        # Assert
        self.assertEqual(meta["type"], "Constraint")
        self.assertEqual(meta["rule"], "TEST RULE")

    def test_Template_Validate_WhenValueIsNone_ReturnsTrueImmediately(self):
        # Arrange
        constraint = DummyConstraint("TEST RULE", should_pass=False)
        
        # Act
        result = constraint.validate(None, {})
        
        # Assert
        self.assertTrue(result, "Null values should bypass validation by default")

    def test_Template_Validate_WhenCheckLogicFails_RaisesException(self):
        # Arrange
        constraint = DummyConstraint("TEST RULE", should_pass=False)
        
        # Act & Assert
        with self.assertRaises(ConstraintViolationException) as context:
            constraint.validate("SomeValue", {})
        
        self.assertIn("TEST RULE", str(context.exception))

    def test_Template_Validate_WhenCheckLogicPasses_ReturnsTrue(self):
        # Arrange
        constraint = DummyConstraint("TEST RULE", should_pass=True)
        
        # Act
        result = constraint.validate("SomeValue", {})
        
        # Assert
        self.assertTrue(result)
