from Classes.DatabaseObjectManagement.table import Table
from core.repositories.table_repository import TableRepository

class TableService:
    def __init__(self):
        self.repository = TableRepository()

    def create_table(self, schema_name: str, table_name: str):
        existing = self.repository.get_by_name(schema_name, table_name)
        if existing:
            return None
                
        table = Table(name=table_name)
        # Initialize an in-memory row storage segment dynamically
        table.rows_store = []
        saved = self.repository.save(schema_name, table)
        if not saved:
            return None
        return self._map_to_dto(schema_name, saved)

    def list_tables(self, schema_name: str):
        tables = self.repository.get_all(schema_name)
        if tables is None:
            return None
        return [self._map_to_dto(schema_name, t) for t in tables]

    def get_table(self, schema_name: str, table_name: str):
        table = self.repository.get_by_name(schema_name, table_name)
        if not table:
            return None
        return self._map_to_dto(schema_name, table)

    def update_table(self, schema_name: str, table_name: str, new_name: str):
        table = self.repository.get_by_name(schema_name, table_name)
        if not table:
            return None
        table.name = new_name
        self.repository.save(schema_name, table)
        return self._map_to_dto(schema_name, table)

    def delete_table(self, schema_name: str, table_name: str):
        return self.repository.delete(schema_name, table_name)

    def _map_to_dto(self, schema_name: str, table: Table) -> dict:
        metadata = table.get_metadata()
        columns = [child["name"] for child in metadata.get("children", []) if child.get("type") == "Column"]
        return {
            "name": table.name,
            "schema": schema_name,
            "columns": columns
        }
