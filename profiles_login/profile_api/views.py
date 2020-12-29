from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer
from .models import *
from rest_framework import viewsets
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



class HelloViewsSet(viewsets.ViewSet):
    """Test api viewset"""
    serializer_class = HelloSerializer
    def list(self,request):
        """Return hello message"""
        a_viewset=[
            'Uses action ()',
            'automatically maps to urls using router',
            'More functionality with less code',

        ]
        return Response({'message':'Hello','viewset':a_viewset})

    def create(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self,request,pk=None):
        return Response({'http_method':'GET'})


    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})