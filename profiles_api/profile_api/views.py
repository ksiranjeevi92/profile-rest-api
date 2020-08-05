from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profile_api import serializers
from profile_api import models
from profile_api import permissions

class HelloAPIView(APIView):
    """Test api view"""
    serializer_class = serializers.HelloSerializers
    
    def get(self, request, format=None):
        
        return Response({"mesage": "Hello"})
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello{name}'
            return Response({"message": message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        return Response({"method": "PUT"})
        
    def patch(self,request,pk=None):
        
        return Response({"method": "PATCH"})
        
    def delete(self,request,pk=None):
        return Response({"method": "DELETE"})
    
    
class HelloViewSet(viewsets.ViewSet):
    """Test api view set"""
    
    serializer_class = serializers.HelloSerializers
    
    def list(self,request):
        return Response({"message": "Hello viewset"})
    
    def create(self,request):
        """Test viewset"""
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello{name}'
            return Response({"message": message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,request,pk=None):
        return Response({"Type": "Update"})
    
    def partial_update(self,request,pk=None):
        return Response({"Type": "PARTIAL_Update"})
    
    def retrieve(self,request,pk=None):
        return Response({"Type": "RETRIEVE"})
    
    def destroy(self,request,pk=None):
        return Response({"Type": "DESTROY"})
    
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Model view set"""
    serializer_class = serializers.UserProfileSerializers
    queryset = models.UserProfile.object.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "email")
    
class UserApiLoginView(ObtainAuthToken):
    """Handle user authentication toke"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    "user profile feed view set"
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatusTest,
        IsAuthenticated
    )
    
    def perform_create(self,serializer):
        serializer.save(user_profile=self.request.user)
    
