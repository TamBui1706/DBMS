from .constraint import Constraint

class CheckConstraint(Constraint):
    def __init__(self, column_name: str, rule: str, expression: str):
        super().__init__(column_name, rule)
        self.expression = expression

    def check_logic(self, value, db_context) -> bool:
        # Simplified simulation of expression checking for TDD purposes
        # In reality, this would parse self.expression and evaluate it against value
        try:
            return eval(f"{value} {self.expression}")
        except:
            return False
