from rest_framework import serializers

class TableResponse(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    schema = serializers.CharField(max_length=100)
    columns = serializers.ListField(child=serializers.CharField(max_length=100), default=list)
