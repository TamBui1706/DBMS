from Classes.DatabaseObjectManagement.schema import Schema
from core.repositories.database_repository import DatabaseRepository

class SchemaService:
    def __init__(self):
        self.db_repository = DatabaseRepository()
        self.db_repository.seed()

    def create_schema(self, db_name: str, schema_name: str):
        db = self.db_repository.get_by_name(db_name)
        if not db:
            return None
            
        # Check if schema already exists in children
        for child in db.children:
            if getattr(child, "name", None) == schema_name:
                return None
                
        # Instantiate a real Schema class object
        schema = Schema(name=schema_name)
        db.add_child(schema)
        self.db_repository.save(db)
        return self._map_to_dto(db_name, schema)

    def list_schemas(self, db_name: str):
        db = self.db_repository.get_by_name(db_name)
        if not db:
            return None
            
        schemas = []
        for child in db.children:
            if type(child).__name__ == "Schema":
                schemas.append(self._map_to_dto(db_name, child))
        return schemas

    def get_schema(self, db_name: str, schema_name: str):
        db = self.db_repository.get_by_name(db_name)
        if not db:
            return None
            
        for child in db.children:
            if type(child).__name__ == "Schema" and getattr(child, "name", None) == schema_name:
                return self._map_to_dto(db_name, child)
        return None

    def update_schema(self, db_name: str, schema_name: str, new_name: str):
        db = self.db_repository.get_by_name(db_name)
        if not db:
            return None
            
        for child in db.children:
            if type(child).__name__ == "Schema" and getattr(child, "name", None) == schema_name:
                child.name = new_name
                self.db_repository.save(db)
                return self._map_to_dto(db_name, child)
        return None

    def delete_schema(self, db_name: str, schema_name: str):
        db = self.db_repository.get_by_name(db_name)
        if not db:
            return False
            
        target_schema = None
        for child in db.children:
            if type(child).__name__ == "Schema" and getattr(child, "name", None) == schema_name:
                target_schema = child
                break
                
        if target_schema:
            db.children.remove(target_schema)
            self.db_repository.save(db)
            return True
        return False

    def _map_to_dto(self, db_name: str, schema: Schema) -> dict:
        metadata = schema.get_metadata()
        tables = [child["name"] for child in metadata.get("children", []) if child.get("type") == "Table"]
        return {
            "name": schema.name,
            "database": db_name,
            "tables": tables
        }
