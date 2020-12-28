from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer
# Create your views here.

class HelloAPIView(APIView):
    """Test api view"""
    serializer_class = HelloSerializer
    def get(self,request,format=None):
        """Returns list of APIView features"""
        an_apiview = [

            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to django view',
            'Gives you control over app logic ',
            'URL are mapped manually',

        ]
        return Response({'message':'Hello','an_api':an_apiview})

    def post(self,request):
        """Create a hello message with name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk=None):
        """Update an existing name"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle partial update"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
