from rest_framework import serializers

class CreateIndexRequest(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    type = serializers.ChoiceField(choices=["BTreeIndex", "HashIndex", "BitmapIndex"])
    column_name = serializers.CharField(max_length=100)

class IndexSearchRequest(serializers.Serializer):
    key = serializers.CharField(max_length=200)

class IndexRangeSearchRequest(serializers.Serializer):
    start_key = serializers.CharField(max_length=200)
    end_key = serializers.CharField(max_length=200)
