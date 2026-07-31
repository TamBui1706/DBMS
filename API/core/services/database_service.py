from Classes.Core.database import Database
from Classes.DatabaseObjectManagement.schema import Schema
from core.repositories.database_repository import DatabaseRepository

class DatabaseService:
    def __init__(self):
        self.repository = DatabaseRepository()
        self.repository.seed()

    def list_databases(self):
        dbs = self.repository.get_all()
        return [self._map_to_dto(db) for db in dbs]

    def get_database(self, name: str):
        db = self.repository.get_by_name(name)
        if not db:
            return None
        return self._map_to_dto(db)

    def create_database(self, name: str, owner: str, description: str):
        if self.repository.get_by_name(name):
            return None
        
        db = Database(name=name)
        db.owner = owner
        db.status = "closed"
        db.size_mb = 0.0
        db.description = description or ""
        db.add_child(Schema(name="public"))
        
        saved_db = self.repository.save(db)
        return self._map_to_dto(saved_db)

    def delete_database(self, name: str):
        return self.repository.delete(name)

    def open_database(self, name: str):
        db = self.repository.get_by_name(name)
        if not db:
            return None
        db.open()
        db.status = "open"
        self.repository.save(db)
        return self._map_to_dto(db)

    def close_database(self, name: str):
        db = self.repository.get_by_name(name)
        if not db:
            return None
        db.status = "closed"
        self.repository.save(db)
        return self._map_to_dto(db)

    def set_readonly_database(self, name: str):
        db = self.repository.get_by_name(name)
        if not db:
            return None
        db.status = "readonly"
        self.repository.save(db)
        return self._map_to_dto(db)

    def run_database_recovery(self, name: str):
        db = self.repository.get_by_name(name)
        if not db:
            return None
        db.status = "closed"
        self.repository.save(db)
        return self._map_to_dto(db)

    def _map_to_dto(self, db: Database) -> dict:
        metadata = db.get_metadata()
        schemas = [child["name"] for child in metadata.get("children", []) if child.get("type") == "Schema"]
        return {
            "name": db.name,
            "owner": getattr(db, "owner", "admin"),
            "status": getattr(db, "status", "closed"),
            "size_mb": getattr(db, "size_mb", 0.0),
            "description": getattr(db, "description", ""),
            "schemas": schemas
        }
