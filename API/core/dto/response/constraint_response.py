from rest_framework import serializers

class ConstraintResponse(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=50)
    column_name = serializers.CharField(max_length=100)
    rule = serializers.CharField(max_length=200)
    details = serializers.JSONField(required=False, default=dict)
