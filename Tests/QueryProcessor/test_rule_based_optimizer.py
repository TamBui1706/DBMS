import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Classes.QueryProcessor.rule_based_optimizer import RuleBasedOptimizer

class TestRuleBasedOptimizer(unittest.TestCase):
    def test_Init_WhenCalled_ShouldInitializeRuleBasedOptimizer(self):
        pass

    def test_ApplyRules_WhenValid_ShouldSucceed(self):
        pass

    def test_ApplyRules_WhenInvalid_ShouldThrow(self):
        pass

if __name__ == '__main__':
    unittest.main()
