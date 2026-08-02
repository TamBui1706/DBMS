from core.repositories.table_repository import TableRepository
from core.repositories.database_repository import DatabaseRepository
from Classes.DatabaseObjectManagement.index import Index

class IndexRepository:
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
        if not hasattr(table, "indexes_store"):
            table.indexes_store = []
        return table.indexes_store

    def get_by_name(self, table_name: str, index_name: str):
        indexes = self.get_all(table_name)
        if indexes is None:
            return None
        for idx in indexes:
            if idx.name == index_name:
                return idx
        return None

    def save(self, table_name: str, index: Index):
        table, db = self._find_table_and_db(table_name)
        if not table:
            return None
        if not hasattr(table, "indexes_store"):
            table.indexes_store = []
        # Remove old matching index if exists to overwrite
        table.indexes_store = [i for i in table.indexes_store if i.name != index.name]
        table.indexes_store.append(index)
        self.db_repo.save(db)
        return index

    def delete(self, table_name: str, index_name: str):
        table, db = self._find_table_and_db(table_name)
        if not table or not hasattr(table, "indexes_store"):
            return False
        idx = self.get_by_name(table_name, index_name)
        if idx:
            table.indexes_store.remove(idx)
            self.db_repo.save(db)
            return True
        return False
