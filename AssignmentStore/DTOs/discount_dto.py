from rest_framework import serializers

class DiscountResponseDto(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    code = serializers.CharField(max_length=50)
    type = serializers.CharField(max_length=50)
    value = serializers.FloatField()
    status = serializers.CharField(max_length=50)
