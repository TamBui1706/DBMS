from rest_framework import serializers

class CreatePartitionRequest(serializers.Serializer):
    table_name = serializers.CharField(max_length=100)
    partition_key = serializers.CharField(max_length=100)

class UpdatePartitionRequest(serializers.Serializer):
    partition_key = serializers.CharField(max_length=100)
