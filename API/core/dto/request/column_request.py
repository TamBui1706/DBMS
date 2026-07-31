from rest_framework import serializers

class AddColumnRequest(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=50)

class UpdateColumnRequest(serializers.Serializer):
    type = serializers.CharField(max_length=50)
