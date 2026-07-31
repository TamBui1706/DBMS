from core.repositories.table_repository import TableRepository
from core.repositories.database_repository import DatabaseRepository
from Classes.DatabaseObjectManagement.column import Column

class ColumnRepository:
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
        return [child for child in table.children if type(child).__name__ == "Column"]

    def get_by_name(self, table_name: str, column_name: str):
        cols = self.get_all(table_name)
        if cols is None:
            return None
        for col in cols:
            if col.name == column_name:
                return col
        return None

    def save(self, table_name: str, column: Column):
        table, db = self._find_table_and_db(table_name)
        if not table:
            return None
        if column not in table.children:
            table.add_child(column)
        self.db_repo.save(db)
        return column

    def delete(self, table_name: str, column_name: str):
        table, db = self._find_table_and_db(table_name)
        if not table:
            return False
        col = self.get_by_name(table_name, column_name)
        if col:
            table.children.remove(col)
            self.db_repo.save(db)
            return True
        return False
