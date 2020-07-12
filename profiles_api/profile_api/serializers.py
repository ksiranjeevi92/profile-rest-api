from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    """Test Serializers"""
    name = serializers.CharField(max_length=10)
    