from core.repositories.table_repository import TableRepository
from core.repositories.database_repository import DatabaseRepository
from Classes.DatabaseObjectManagement.constraint import Constraint

class ConstraintRepository:
    def __init__(self):
        self.db_repo = DatabaseRepository()
        self.table_repo = TableRepository()

    def _find_table_and_db(self, table_name: str):
        for db in self.db_repo.get_all():
            for schema in db.children:
                if type(schema).__name__ == "Schema":
                    table = self.table_repo.get_by_name(schema.name, table_name)
                    if table:
                        return table, db
        return None, None

    def get_all(self, table_name: str):
        table, _ = self._find_table_and_db(table_name)
        if not table:
            return None
        return [child for child in table.children if isinstance(child, Constraint)]

    def get_by_id(self, constraint_id: str):
        # We search across all tables for the matching constraint by its rule/id
        for db in self.db_repo.get_all():
            for schema in db.children:
                if type(schema).__name__ == "Schema":
                    for table in schema.children:
                        if type(table).__name__ == "Table":
                            for child in table.children:
                                if isinstance(child, Constraint) and getattr(child, "rule", None) == constraint_id:
                                    return child, table, db
        return None, None, None

    def save(self, table_name: str, constraint: Constraint):
        table, db = self._find_table_and_db(table_name)
        if not table:
            return None
        if constraint not in table.children:
            table.add_child(constraint)
        self.db_repo.save(db)
        return constraint

    def delete(self, constraint_id: str):
        constraint, table, db = self.get_by_id(constraint_id)
        if constraint:
            table.children.remove(constraint)
            self.db_repo.save(db)
            return True
        return False

    def update_rule(self, constraint_id: str, new_rule: str):
        constraint, _, db = self.get_by_id(constraint_id)
        if constraint:
            constraint.rule = new_rule
            self.db_repo.save(db)
            return constraint
        return None
