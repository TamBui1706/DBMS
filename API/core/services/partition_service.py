from Classes.DatabaseObjectManagement.partition import Partition
from core.repositories.partition_repository import PartitionRepository

class PartitionService:
    def __init__(self):
        self.repository = PartitionRepository()

    def create_partition(self, table_name: str, partition_key: str):
        partition = Partition()
        partition.partitionKey = partition_key
        
        saved = self.repository.save(table_name, partition)
        return self._map_to_dto(saved, table_name) if saved else None

    def list_partitions(self, table_name: str = None):
        all_p = self.repository.get_all()
        if table_name:
            all_p = [item for item in all_p if item[1] == table_name]
        return [self._map_to_dto(p, t_name) for p, t_name in all_p]

    def get_partition(self, partition_id: str):
        p, t_name = self.repository.get_by_id(partition_id)
        if not p:
            return None
        return self._map_to_dto(p, t_name)

    def update_partition(self, partition_id: str, partition_key: str):
        p, t_name = self.repository.get_by_id(partition_id)
        if not p:
            return None
        p.partitionKey = partition_key
        self.repository.save(t_name, p)
        return self._map_to_dto(p, t_name)

    def delete_partition(self, partition_id: str):
        return self.repository.delete(partition_id)

    def _map_to_dto(self, partition, table_name: str) -> dict:
        return {
            "id": getattr(partition, "partitionKey", ""),
            "table_name": table_name,
            "partition_key": getattr(partition, "partitionKey", "")
        }
