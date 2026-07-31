from rest_framework import serializers

class CreateSchemaRequest(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class UpdateSchemaRequest(serializers.Serializer):
    name = serializers.CharField(max_length=100)
