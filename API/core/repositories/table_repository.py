from core.repositories.schema_repository import SchemaRepository
from core.repositories.database_repository import DatabaseRepository
from Classes.DatabaseObjectManagement.table import Table

class TableRepository:
    def __init__(self):
        self.db_repo = DatabaseRepository()
        self.schema_repo = SchemaRepository()

    def _find_schema_and_db(self, schema_name: str):
        for db in self.db_repo.get_all():
            schema = self.schema_repo.get_by_name(db.name, schema_name)
            if schema:
                return schema, db
        return None, None

    def get_all(self, schema_name: str):
        schema, _ = self._find_schema_and_db(schema_name)
        if not schema:
            return None
        return [child for child in schema.children if type(child).__name__ == "Table"]

    def get_by_name(self, schema_name: str, table_name: str):
        tables = self.get_all(schema_name)
        if tables is None:
            return None
        for table in tables:
            if table.name == table_name:
                return table
        return None

    def save(self, schema_name: str, table: Table):
        schema, db = self._find_schema_and_db(schema_name)
        if not schema:
            return None
        if table not in schema.children:
            schema.add_child(table)
        self.db_repo.save(db)
        return table

    def delete(self, schema_name: str, table_name: str):
        schema, db = self._find_schema_and_db(schema_name)
        if not schema:
            return False
        table = self.get_by_name(schema_name, table_name)
        if table:
            schema.children.remove(table)
            self.db_repo.save(db)
            return True
        return False
