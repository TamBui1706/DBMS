from rest_framework import serializers

class SchemaResponse(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    database = serializers.CharField(max_length=100)
    tables = serializers.ListField(child=serializers.CharField(max_length=100), default=list)
