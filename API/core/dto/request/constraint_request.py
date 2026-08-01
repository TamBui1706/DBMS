from rest_framework import serializers

class CheckConstraintRequest(serializers.Serializer):
    table_name = serializers.CharField(max_length=100)
    column_name = serializers.CharField(max_length=100)
    rule = serializers.CharField(max_length=200)
    expression = serializers.CharField(max_length=300)

class PrimaryKeyRequest(serializers.Serializer):
    table_name = serializers.CharField(max_length=100)
    column_name = serializers.CharField(max_length=100)
    rule = serializers.CharField(max_length=200)

class UniqueConstraintRequest(serializers.Serializer):
    table_name = serializers.CharField(max_length=100)
    column_name = serializers.CharField(max_length=100)
    rule = serializers.CharField(max_length=200)

class ForeignKeyRequest(serializers.Serializer):
    table_name = serializers.CharField(max_length=100)
    column_name = serializers.CharField(max_length=100)
    rule = serializers.CharField(max_length=200)
    referenced_table = serializers.CharField(max_length=100)
    referenced_column = serializers.CharField(max_length=100)

class UpdateConstraintRequest(serializers.Serializer):
    rule = serializers.CharField(max_length=200)
