import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Classes.query_processor import SQLParser, QueryOptimizer, QueryExecution

class TestSQLParser(unittest.TestCase):
    def setUp(self):
        self.parser = SQLParser()

    def test_lexical_analyzer_happy_path(self):
        result = self.parser.extract_tokens("SELECT * FROM users")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_lexical_analyzer_failure_path(self):
        with self.assertRaises(Exception):
            self.parser.extract_tokens(None)

    def test_syntax_analyzer_happy_path(self):
        result = self.parser.parse_query("SELECT id FROM users")
        self.assertIsNotNone(result)
        self.assertIn('columns', result)

    def test_syntax_analyzer_failure_path(self):
        with self.assertRaises(Exception):
            self.parser.parse_query("SELECT FROM users")

    def test_ast_builder_happy_path(self):
        ast = self.parser.parse_query("SELECT * FROM t")
        self.assertIsNotNone(ast)
        self.assertEqual(ast.get('type'), 'SELECT')

    def test_ast_builder_failure_path(self):
        with self.assertRaises(Exception):
            self.parser.parse_query("")

class TestQueryOptimizer(unittest.TestCase):
    def setUp(self):
        self.optimizer = QueryOptimizer()

    def test_cost_based_optimizer_happy_path(self):
        plan = self.optimizer.cost_estimation({"type": "SELECT", "table": "users"})
        self.assertIsNotNone(plan)
        self.assertGreaterEqual(plan, 0.0)

    def test_cost_based_optimizer_failure_path(self):
        with self.assertRaises(Exception):
            self.optimizer.cost_estimation({})

    def test_rule_based_optimizer_happy_path(self):
        plan = self.optimizer.apply_heuristics({"type": "SELECT", "table": "users"})
        self.assertIsNotNone(plan)

    def test_rule_based_optimizer_failure_path(self):
        with self.assertRaises(Exception):
            self.optimizer.apply_heuristics(None)

    def test_logical_plan_generator_happy_path(self):
        plan = self.optimizer.generate_execution_plan({"type": "SELECT"})
        self.assertIsNotNone(plan)
        self.assertIn("steps", plan)

    def test_logical_plan_generator_failure_path(self):
        with self.assertRaises(Exception):
            self.optimizer.generate_execution_plan(None)

class TestQueryExecution(unittest.TestCase):
    def setUp(self):
        self.executor = QueryExecution(storage_engine=None)

    def test_operator_scheduler_happy_path(self):
        result = self.executor.execute_plan({"steps": ["SCAN", "FILTER"]})
        self.assertIsInstance(result, list)

    def test_operator_scheduler_failure_path(self):
        with self.assertRaises(Exception):
            self.executor.execute_plan({"steps": []})

    def test_execution_engine_happy_path(self):
        result = self.executor.execute_node({"op": "SCAN"})
        self.assertIsNotNone(result)

    def test_execution_engine_failure_path(self):
        with self.assertRaises(Exception):
            self.executor.execute_node({"op": "INVALID"})

if __name__ == '__main__':
    unittest.main()
