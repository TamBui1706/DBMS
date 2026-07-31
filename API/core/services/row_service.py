from Classes.DatabaseObjectManagement.row import Row
from core.repositories.row_repository import RowRepository

class RowService:
    def __init__(self):
        self.repository = RowRepository()

    def insert_row(self, table_name: str, values: list):
        rows = self.repository.get_all(table_name)
        if rows is None:
            return None
            
        row = Row()
        row.rowId = len(rows) + 1
        row.values = values
        
        saved = self.repository.save(table_name, row)
        if not saved:
            return None
        return self._map_to_dto(saved)

    def list_rows(self, table_name: str):
        rows = self.repository.get_all(table_name)
        if rows is None:
            return None
        return [self._map_to_dto(r) for r in rows]

    def get_row(self, table_name: str, row_id: int):
        row = self.repository.get_by_id(table_name, row_id)
        if not row:
            return None
        return self._map_to_dto(row)

    def update_row(self, table_name: str, row_id: int, values: list):
        row = self.repository.get_by_id(table_name, row_id)
        if not row:
            return None
        row.values = values
        self.repository.save(table_name, row)
        return self._map_to_dto(row)

    def delete_row(self, table_name: str, row_id: int):
        return self.repository.delete(table_name, row_id)

    def _map_to_dto(self, row: Row) -> dict:
        return {
            "rowId": row.rowId,
            "values": row.values
        }
