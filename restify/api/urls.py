from rest_framework import routers
from .views import (
    PublisherViewSet,
    SoftwareViewSet,
    ServerViewSet,
    ServerListAPIView,
    ServerCreateAPIView,
    ServerDetailAPIView,
    # ServerUpdateAPIView,
    SoftwareListAPIView,
    SoftwareCreateAPIView,
    SoftwareDetailAPIView,
    PublisherListAPIView,
    PublisherCreateAPIView,
    PublisherDetailAPIView,
    server_software_publisher_api_home,
    # ServerAdamViewSet
)
from rest_framework import renderers
from django.urls import path, include




# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r"publishers", PublisherViewSet)
router.register(r"software", SoftwareViewSet)
router.register(r"servers", ServerViewSet)
# router.register(r"serveradam", ServerAdamViewSet)


urlpatterns = [
    path("api3/", include(router.urls)),
    # path('', server_software_publisher_api_home),
    # # Server
    # path("server/", ServerListAPIView.as_view(), name="server_list_api"),
    # path("server/create/", ServerCreateAPIView.as_view(), name="server_create_api"),
    # path("server/<slug:server_slug>/", ServerDetailAPIView.as_view(), name="server_detail_api"),
    # # path("server/<slug:server_slug>/update/", ServerUpdateAPIView.as_view(), name="server_update_api"),
    # # path("server/<slug:server_slug>/", ServerDetailAPIView.as_view(), name="server_detail_api"),
    # # Software
    # path("software/", SoftwareListAPIView.as_view(), name="software_list_api"),
    # path("software/create/", SoftwareCreateAPIView.as_view(), name="software_create_api"),
    # path("software/<slug:slug>/", SoftwareDetailAPIView.as_view(), name="software_detail_api"),
    # path("publisher/", PublisherListAPIView.as_view(), name="publisher_list_api"),
    # # Publisher
    # path("publisher/create/", PublisherCreateAPIView.as_view(), name="publisher_create_api"),
    # path("publisher/<slug:slug>", PublisherDetailAPIView.as_view(), name="publisher_detail_api"),
]
