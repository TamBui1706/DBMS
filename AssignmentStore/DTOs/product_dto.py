from rest_framework import serializers

class CreateProductRequestDto(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    price = serializers.FloatField()
    categoryId = serializers.CharField(max_length=100, required=False, allow_blank=True)
    type = serializers.CharField(max_length=50, default="Physical")
    stockStatus = serializers.CharField(max_length=50, default="InStock")

class UpdateProductRequestDto(serializers.Serializer):
    name = serializers.CharField(max_length=150, required=False)
    price = serializers.FloatField(required=False)
    stockStatus = serializers.CharField(max_length=50, required=False)

class ProductResponseDto(serializers.Serializer):
    id = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=150)
    price = serializers.FloatField()
    categoryId = serializers.CharField(max_length=100, allow_blank=True)
    type = serializers.CharField(max_length=50)
    stockStatus = serializers.CharField(max_length=50)
    images = serializers.ListField(child=serializers.CharField(max_length=500), default=list)
