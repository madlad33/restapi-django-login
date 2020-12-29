from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import HelloAPIView,HelloViewsSet
router=DefaultRouter()
router.register('helloviewset',HelloViewsSet,basename='viewset')
urlpatterns =[
path('helloview',HelloAPIView.as_view(),name='Test'),
path('',include(router.urls))


]