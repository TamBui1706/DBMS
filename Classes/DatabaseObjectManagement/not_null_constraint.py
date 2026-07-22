from .constraint import Constraint

class NotNullConstraint(Constraint):
    def __init__(self, column_name: str, rule: str = "NOT NULL"):
        super().__init__(column_name, rule)

    def check_logic(self, value, db_context) -> bool:
        return value is not None
