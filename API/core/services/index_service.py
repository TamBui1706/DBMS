from Classes.DatabaseObjectManagement.b_tree_index import BTreeIndex
from Classes.DatabaseObjectManagement.hash_index import HashIndex
from Classes.DatabaseObjectManagement.bitmap_index import BitmapIndex
from core.repositories.index_repository import IndexRepository

class IndexService:
    def __init__(self):
        self.repository = IndexRepository()

    def create_index(self, table_name: str, name: str, idx_type: str, column_name: str):
        if idx_type == "BTreeIndex":
            index = BTreeIndex()
        elif idx_type == "HashIndex":
            index = HashIndex()
        elif idx_type == "BitmapIndex":
            index = BitmapIndex()
        else:
            return None

        index.name = name
        index.type = idx_type
        index.column_name = column_name
        
        saved = self.repository.save(table_name, index)
        return self._map_to_dto(saved) if saved else None

    def list_indexes(self, table_name: str):
        indexes = self.repository.get_all(table_name)
        if indexes is None:
            return None
        return [self._map_to_dto(idx) for idx in indexes]

    def delete_index(self, table_name: str, index_name: str):
        return self.repository.delete(table_name, index_name)

    def search_index(self, table_name: str, index_name: str, key: str):
        idx = self.repository.get_by_name(table_name, index_name)
        if not idx:
            return None
        # Call search stub
        idx.search()
        # Return mock results for demo
        return {
            "found": True,
            "results": [f"Row pointing to key '{key}' via index '{index_name}'"]
        }

    def range_search_index(self, table_name: str, index_name: str, start_key: str, end_key: str):
        idx = self.repository.get_by_name(table_name, index_name)
        if not idx:
            return None
        idx.search()
        return {
            "found": True,
            "results": [
                f"Row pointing to key '{start_key}' via index '{index_name}'",
                f"Row pointing to key '{end_key}' via index '{index_name}'"
            ]
        }

    def _map_to_dto(self, index) -> dict:
        return {
            "name": getattr(index, "name", ""),
            "type": getattr(index, "type", ""),
            "column_name": getattr(index, "column_name", "")
        }
