from rest_framework import serializers

class ViewResponse(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    query_definition = serializers.CharField(max_length=1000)
