from core.repositories.table_repository import TableRepository
from core.repositories.database_repository import DatabaseRepository
from Classes.DatabaseObjectManagement.partition import Partition

class PartitionRepository:
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

    def get_all(self):
        # Scan all tables to return all partitions
        partitions = []
        for db in self.db_repo.get_all():
            for schema in db.children:
                if type(schema).__name__ == "Schema":
                    for table in schema.children:
                        if type(table).__name__ == "Table" and hasattr(table, "partitions_store"):
                            for p in table.partitions_store:
                                partitions.append((p, table.name))
        return partitions

    def get_by_id(self, partition_id: str):
        for p, table_name in self.get_all():
            if getattr(p, "partitionKey", None) == partition_id:
                return p, table_name
        return None, None

    def save(self, table_name: str, partition: Partition):
        table, db = self._find_table_and_db(table_name)
        if not table:
            return None
        if not hasattr(table, "partitions_store"):
            table.partitions_store = []
        table.partitions_store = [p for p in table.partitions_store if getattr(p, "partitionKey", None) != partition.partitionKey]
        table.partitions_store.append(partition)
        self.db_repo.save(db)
        return partition

    def delete(self, partition_id: str):
        p, table_name = self.get_by_id(partition_id)
        if p:
            table, db = self._find_table_and_db(table_name)
            table.partitions_store.remove(p)
            self.db_repo.save(db)
            return True
        return False
