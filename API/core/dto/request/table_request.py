from rest_framework import serializers

class CreateTableRequest(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class UpdateTableRequest(serializers.Serializer):
    name = serializers.CharField(max_length=100)
