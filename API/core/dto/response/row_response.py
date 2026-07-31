from rest_framework import serializers

class RowResponse(serializers.Serializer):
    rowId = serializers.IntegerField()
    values = serializers.ListField(child=serializers.CharField(max_length=500))
