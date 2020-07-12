from rest_framework import serializers

from profile_api import models

class HelloSerializers(serializers.Serializer):
    """Test Serializers"""
    name = serializers.CharField(max_length=10)
    
    
    
class UserProfileSerializers(serializers.ModelSerializer):
    """User profile serializer"""
    class Meta:
        model = models.UserProfile
        fields = ["id", "name", "email", "password"]
        extra_kwargs = {
            "password": {
                'write_only': True,
                "style": {'input_type': 'password'}
            }
        }
        
    def create(self, validated_data):
        user = models.UserProfile.object.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        
        return user
    
    