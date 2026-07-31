from rest_framework import serializers

class InsertRowRequest(serializers.Serializer):
    values = serializers.ListField(child=serializers.CharField(max_length=500))

class UpdateRowRequest(serializers.Serializer):
    values = serializers.ListField(child=serializers.CharField(max_length=500))
