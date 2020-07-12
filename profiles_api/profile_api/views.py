from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test api view"""
    
    def get(self, request, format=None):
        return Response({"mesage": "Hello"})
