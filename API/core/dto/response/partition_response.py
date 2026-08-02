from rest_framework import serializers

class PartitionResponse(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    table_name = serializers.CharField(max_length=100)
    partition_key = serializers.CharField(max_length=100)
