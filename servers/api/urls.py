from rest_framework import routers
from .views import PublisherViewSet, SoftwareViewSet, ServerViewSet
from rest_framework import renderers
from django.urls import path, include

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'publishers', PublisherViewSet)
router.register(r'software', SoftwareViewSet)
router.register(r'servers', ServerViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
