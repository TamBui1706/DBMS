from abc import ABC, abstractmethod
from DBMS.Classes.DatabaseObjectManagement.metadata_node import MetadataNode
from DBMS.Classes.DatabaseObjectManagement.exceptions import ConstraintViolationException

class Constraint(MetadataNode, ABC):
    def __init__(self, column_name: str, rule: str):
        self.column_name = column_name
        self.rule = rule

    def validate(self, value, db_context):
        # Pre-processing: Skip nulls (except for NotNullConstraint which overrides this behavior internally or handles it in check_logic)
        if value is None and not self.rule.upper().startswith("NOT NULL"):
            return True

        # Hook Method: Core Logic
        if not self.check_logic(value, db_context):
            # Post-processing: Exception
            self.on_violation(value)

    @abstractmethod
    def check_logic(self, value, db_context) -> bool:
        pass

    def on_violation(self, value):
        raise ConstraintViolationException(f"Column '{self.column_name}' violated constraint '{self.rule}' with value '{value}'!")

    def get_metadata(self) -> dict:
        return {
            "type": "Constraint",
            "rule": self.rule,
            "column_name": self.column_name
        }
