from rest_framework import serializers

class DatabaseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    owner = serializers.CharField(max_length=100, default="admin")
    status = serializers.CharField(max_length=20, default="closed")
    size_mb = serializers.FloatField(default=0.0)
    description = serializers.CharField(max_length=500, required=False, allow_blank=True, allow_null=True)
    schemas = serializers.ListField(child=serializers.CharField(max_length=50), default=list)
