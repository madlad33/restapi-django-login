from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloAPIView(APIView):
    """Test api view"""
    def get(self,request,format=None):
        """Returns list of APIView features"""
        an_apiview = [

            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to django view',
            'Gives you control over app logic ',
            'URL are mapped manually',

        ]
        return Response({'message':'Hello','an_api':an_apiview})