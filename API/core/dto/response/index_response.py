from rest_framework import serializers

class IndexResponse(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=50)
    column_name = serializers.CharField(max_length=100)

class IndexSearchResponse(serializers.Serializer):
    found = serializers.BooleanField()
    results = serializers.ListField(child=serializers.CharField(max_length=500), default=list)
