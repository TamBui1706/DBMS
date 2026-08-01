from Classes.DatabaseObjectManagement.check_constraint import CheckConstraint
from Classes.DatabaseObjectManagement.primary_key import PrimaryKey
from Classes.DatabaseObjectManagement.unique_constraint import UniqueConstraint
from Classes.DatabaseObjectManagement.foreign_key import ForeignKey
from core.repositories.constraint_repository import ConstraintRepository

class ConstraintService:
    def __init__(self):
        self.repository = ConstraintRepository()

    def create_check(self, table_name: str, column_name: str, rule: str, expression: str):
        constraint = CheckConstraint(column_name=column_name, rule=rule, expression=expression)
        saved = self.repository.save(table_name, constraint)
        return self._map_to_dto(saved) if saved else None

    def create_primary_key(self, table_name: str, column_name: str, rule: str):
        # PrimaryKey in our project inherits from Constraint
        constraint = PrimaryKey(column_name=column_name, rule=rule)
        saved = self.repository.save(table_name, constraint)
        return self._map_to_dto(saved) if saved else None

    def create_unique(self, table_name: str, column_name: str, rule: str):
        constraint = UniqueConstraint(column_name=column_name, rule=rule)
        saved = self.repository.save(table_name, constraint)
        return self._map_to_dto(saved) if saved else None

    def create_foreign_key(self, table_name: str, column_name: str, rule: str, referenced_table: str, referenced_column: str):
        # ForeignKey class might take extra reference args
        # Let's use kwargs or match the constructor
        constraint = ForeignKey(column_name=column_name, rule=rule)
        # Add custom properties dynamically if missing
        constraint.referenced_table = referenced_table
        constraint.referenced_column = referenced_column
        saved = self.repository.save(table_name, constraint)
        return self._map_to_dto(saved) if saved else None

    def update_constraint(self, constraint_id: str, new_rule: str):
        updated = self.repository.update_rule(constraint_id, new_rule)
        return self._map_to_dto(updated) if updated else None

    def delete_constraint(self, constraint_id: str):
        return self.repository.delete(constraint_id)

    def _map_to_dto(self, constraint) -> dict:
        metadata = constraint.get_metadata()
        details = {}
        if isinstance(constraint, CheckConstraint):
            details["expression"] = getattr(constraint, "expression", "")
        elif isinstance(constraint, ForeignKey):
            details["referenced_table"] = getattr(constraint, "referenced_table", "")
            details["referenced_column"] = getattr(constraint, "referenced_column", "")
            
        return {
            "id": constraint.rule, # We treat the rule (e.g. name of constraint) as its ID
            "type": type(constraint).__name__,
            "column_name": constraint.column_name,
            "rule": constraint.rule,
            "details": details
        }
