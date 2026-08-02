from rest_framework import serializers

class UpdateStoreRequestDto(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    domain = serializers.CharField(max_length=150, required=False, allow_blank=True)
    currency = serializers.CharField(max_length=10, default="USD")

class StoreResponseDto(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=150)
    domain = serializers.CharField(max_length=150)
    logoUrl = serializers.CharField(max_length=500, allow_blank=True)
    currency = serializers.CharField(max_length=10)
    owner = serializers.JSONField(required=False, default=dict)
