from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer, ProfileSerializer,ProfileFeedItemSerializer
from .models import *
from rest_framework import viewsets
from .permissions import UpdateOwnProfile,UpdateOwnFeed
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
class HelloAPIView(APIView):
    """Test api view"""
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns list of APIView features"""
        an_apiview = [

            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to django view',
            'Gives you control over app logic ',
            'URL are mapped manually',

        ]
        return Response({'message': 'Hello', 'an_api': an_apiview})

    def post(self, request):
        """Create a hello message with name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Update an existing name"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewsSet(viewsets.ViewSet):
    """Test api viewset"""
    serializer_class = HelloSerializer

    def list(self, request):
        """Return hello message"""
        a_viewset = [
            'Uses action ()',
            'automatically maps to urls using router',
            'More functionality with less code',

        ]
        return Response({'message': 'Hello', 'viewset': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self, request, pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']


class UserLoginAPIView(ObtainAuthToken):
    """Handles creating of user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles CRUD profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (UpdateOwnFeed,IsAuthenticated)
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)