from core.repositories.database_repository import DatabaseRepository
from Classes.DatabaseObjectManagement.schema import Schema

class SchemaRepository:
    def __init__(self):
        self.db_repo = DatabaseRepository()

    def get_all(self, db_name: str):
        db = self.db_repo.get_by_name(db_name)
        if not db:
            return None
        return [child for child in db.children if type(child).__name__ == "Schema"]

    def get_by_name(self, db_name: str, schema_name: str):
        schemas = self.get_all(db_name)
        if schemas is None:
            return None
        for schema in schemas:
            if schema.name == schema_name:
                return schema
        return None

    def save(self, db_name: str, schema: Schema):
        db = self.db_repo.get_by_name(db_name)
        if not db:
            return None
        if schema not in db.children:
            db.add_child(schema)
        self.db_repo.save(db)
        return schema

    def delete(self, db_name: str, schema_name: str):
        db = self.db_repo.get_by_name(db_name)
        if not db:
            return False
        schema = self.get_by_name(db_name, schema_name)
        if schema:
            db.children.remove(schema)
            self.db_repo.save(db)
            return True
        return False
