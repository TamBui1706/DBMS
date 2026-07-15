from typing import List
from src.enums import IndexType, IndexState

class IndexMetadata:
    def __init__(self, index_id: int, name: str, table_id: int, column_ids: List[int], index_type: IndexType):
        self.index_id = index_id
        self.name = name
        self.table_id = table_id
        self.column_ids = column_ids
        self.index_type = index_type
        self.is_unique = False
        self.root_page_id = -1
        self.state = IndexState.BUILDING
        self.tree_height = 0
        self.node_count = 0
        self.key_count = 0
