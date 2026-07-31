from Classes.DatabaseObjectManagement.column import Column
from core.repositories.column_repository import ColumnRepository

class ColumnService:
    def __init__(self):
        self.repository = ColumnRepository()

    def add_column(self, table_name: str, name: str, col_type: str):
        existing = self.repository.get_by_name(table_name, name)
        if existing:
            return None
                
        column = Column(name=name, type=col_type)
        saved = self.repository.save(table_name, column)
        if not saved:
            return None
        return self._map_to_dto(saved)

    def list_columns(self, table_name: str):
        cols = self.repository.get_all(table_name)
        if cols is None:
            return None
        return [self._map_to_dto(c) for c in cols]

    def update_column(self, table_name: str, name: str, col_type: str):
        col = self.repository.get_by_name(table_name, name)
        if not col:
            return None
        col.type = col_type
        self.repository.save(table_name, col)
        return self._map_to_dto(col)

    def delete_column(self, table_name: str, name: str):
        return self.repository.delete(table_name, name)

    def _map_to_dto(self, column: Column) -> dict:
        return {
            "name": column.name,
            "type": column.type,
            "nullable": getattr(column, "nullable", True)
        }
