from rest_framework import serializers

class DatabaseResponse(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    owner = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=20)
    size_mb = serializers.FloatField()
    description = serializers.CharField(max_length=500, allow_blank=True, required=False)
    schemas = serializers.ListField(child=serializers.CharField(max_length=50))
