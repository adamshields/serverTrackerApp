from rest_framework import routers
from .views import (
    PublisherViewSet,
    SoftwareViewSet,
    ServerViewSet,
    ServerListAPIView,
    ServerCreateAPIView,
    ServerDetailAPIView,
    SoftwareListAPIView,
    SoftwareCreateAPIView,
    SoftwareDetailAPIView,
    PublisherListAPIView,
    PublisherCreateAPIView,
    PublisherDetailAPIView,
    server_software_publisher_api_home,
)
from rest_framework import renderers
from django.urls import path, include




# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r"publishers", PublisherViewSet)
router.register(r"software", SoftwareViewSet)
router.register(r"servers", ServerViewSet)


urlpatterns = [
    path("views/", include(router.urls)),
    path('', server_software_publisher_api_home),
    path("server/", ServerListAPIView.as_view(), name="server_list_api"),
    path("server/create", ServerCreateAPIView.as_view(), name="server_create_api"),
    path("server/<slug:slug>", ServerDetailAPIView.as_view(), name="server_detail_api"),
    path("software/", SoftwareListAPIView.as_view(), name="software_list_api"),
    path("software/create", SoftwareCreateAPIView.as_view(), name="software_create_api"),
    path("software/<slug:slug>", SoftwareDetailAPIView.as_view(), name="software_detail_api"),
    path("publisher/", PublisherListAPIView.as_view(), name="publisher_list_api"),
    path("publisher/create", PublisherCreateAPIView.as_view(), name="publisher_create_api"),
    path("publisher/<slug:slug>", PublisherDetailAPIView.as_view(), name="publisher_detail_api"),
]
