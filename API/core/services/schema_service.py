from Classes.DatabaseObjectManagement.schema import Schema
from core.repositories.schema_repository import SchemaRepository

class SchemaService:
    def __init__(self):
        self.repository = SchemaRepository()

    def create_schema(self, db_name: str, schema_name: str):
        existing = self.repository.get_by_name(db_name, schema_name)
        if existing:
            return None
                
        # Instantiate a real Schema class object
        schema = Schema(name=schema_name)
        saved = self.repository.save(db_name, schema)
        if not saved:
            return None
        return self._map_to_dto(db_name, saved)

    def list_schemas(self, db_name: str):
        schemas = self.repository.get_all(db_name)
        if schemas is None:
            return None
        return [self._map_to_dto(db_name, s) for s in schemas]

    def get_schema(self, db_name: str, schema_name: str):
        schema = self.repository.get_by_name(db_name, schema_name)
        if not schema:
            return None
        return self._map_to_dto(db_name, schema)

    def update_schema(self, db_name: str, schema_name: str, new_name: str):
        schema = self.repository.get_by_name(db_name, schema_name)
        if not schema:
            return None
        schema.name = new_name
        self.repository.save(db_name, schema)
        return self._map_to_dto(db_name, schema)

    def delete_schema(self, db_name: str, schema_name: str):
        return self.repository.delete(db_name, schema_name)

    def _map_to_dto(self, db_name: str, schema: Schema) -> dict:
        metadata = schema.get_metadata()
        tables = [child["name"] for child in metadata.get("children", []) if child.get("type") == "Table"]
        return {
            "name": schema.name,
            "database": db_name,
            "tables": tables
        }
