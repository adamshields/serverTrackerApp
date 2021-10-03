from rest_framework import routers
from .views import (
    PublisherViewSet,
    SoftwareViewSet,
    ServerViewSet,
    AitViewSet,
    ProjectViewSet,
    EnvironmentViewSet
)
from rest_framework import renderers
from django.urls import path, include




# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r"publishers", PublisherViewSet)
router.register(r"software", SoftwareViewSet)
router.register(r"servers", ServerViewSet)
router.register(r"aits", AitViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"environments", EnvironmentViewSet)


urlpatterns = [
    path("api3/", include(router.urls)),
]
