from rest_framework import serializers

class CreateViewRequest(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    query_definition = serializers.CharField(max_length=1000)

class UpdateViewRequest(serializers.Serializer):
    query_definition = serializers.CharField(max_length=1000)
