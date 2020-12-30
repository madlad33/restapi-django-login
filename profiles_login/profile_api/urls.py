from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import HelloAPIView,HelloViewsSet,UserProfileViewSet
router=DefaultRouter()
router.register('helloviewset',HelloViewsSet,basename='viewset')
router.register('profileview',UserProfileViewSet,basename='profile')
urlpatterns =[
path('helloview',HelloAPIView.as_view(),name='Test'),
path('',include(router.urls)),




]