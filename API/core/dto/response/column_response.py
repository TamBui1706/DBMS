from rest_framework import serializers

class ColumnResponse(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=50)
    nullable = serializers.BooleanField(default=True)
