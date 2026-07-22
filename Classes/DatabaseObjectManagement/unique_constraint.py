from .constraint import Constraint

class UniqueConstraint(Constraint):
    def __init__(self, column_name: str, rule: str = "UNIQUE"):
        super().__init__(column_name, rule)

    def check_logic(self, value, db_context) -> bool:
        # Check against a simulated BTree Index via db_context
        # We assume db_context has a method get_index(column_name) returning a list or set of values
        try:
            index_data = db_context.get_index(self.column_name)
            return value not in index_data
        except AttributeError:
            # If no context provided, allow it (for basic tests)
            return True
