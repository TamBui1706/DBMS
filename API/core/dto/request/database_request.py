from rest_framework import serializers

class CreateDatabaseRequest(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    owner = serializers.CharField(max_length=100, default="admin")
    description = serializers.CharField(max_length=500, required=False, allow_blank=True, allow_null=True)
