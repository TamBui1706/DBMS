from Classes.Core.database import Database
from Classes.DatabaseObjectManagement.schema import Schema

class DatabaseRepository:
    # Class-level static store mimicking database persistence
    _store = {}

    @classmethod
    def seed(cls):
        # Seed initial database object hierarchies
        if not cls._store:
            db_prod = Database(name="ProductionDB")
            db_prod.status = "open"
            db_prod.owner = "admin"
            db_prod.size_mb = 170.0
            db_prod.add_child(Schema(name="public"))
            db_prod.add_child(Schema(name="sales"))
            db_prod.add_child(Schema(name="inventory"))
            cls._store["ProductionDB"] = db_prod

            db_test = Database(name="TestDB")
            db_test.status = "closed"
            db_test.owner = "developer"
            db_test.size_mb = 12.5
            db_test.add_child(Schema(name="public"))
            cls._store["TestDB"] = db_test

    def get_all(self):
        return list(self._store.values())

    def get_by_name(self, name: str):
        return self._store.get(name)

    def save(self, db: Database):
        self._store[db.name] = db
        return db

    def delete(self, name: str):
        if name in self._store:
            del self._store[name]
            return True
        return False
