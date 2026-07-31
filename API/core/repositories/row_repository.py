from core.repositories.table_repository import TableRepository
from core.repositories.database_repository import DatabaseRepository
from Classes.DatabaseObjectManagement.row import Row

class RowRepository:
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
        if not hasattr(table, "rows_store"):
            table.rows_store = []
        return table.rows_store

    def get_by_id(self, table_name: str, row_id: int):
        rows = self.get_all(table_name)
        if rows is None:
            return None
        for r in rows:
            if r.rowId == row_id:
                return r
        return None

    def save(self, table_name: str, row: Row):
        table, db = self._find_table_and_db(table_name)
        if not table:
            return None
        if not hasattr(table, "rows_store"):
            table.rows_store = []
        if row not in table.rows_store:
            table.rows_store.append(row)
        self.db_repo.save(db)
        return row

    def delete(self, table_name: str, row_id: int):
        table, db = self._find_table_and_db(table_name)
        if not table or not hasattr(table, "rows_store"):
            return False
        row = self.get_by_id(table_name, row_id)
        if row:
            table.rows_store.remove(row)
            self.db_repo.save(db)
            return True
        return False
