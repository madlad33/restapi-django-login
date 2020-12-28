from django.urls import path,include

from .views import HelloAPIView
urlpatterns =[
path('helloview',HelloAPIView.as_view(),name='Test'),


]