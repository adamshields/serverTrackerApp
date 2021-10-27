from rest_framework import routers
from .views import (
    PublisherViewSet,
    SoftwareViewSet,
    DeviceViewSet,
    # DeviceListAPIView,
    # DeviceCreateAPIView,
    # DeviceDetailAPIView,
    # # DeviceUpdateAPIView,
    # SoftwareListAPIView,
    # SoftwareCreateAPIView,
    # SoftwareDetailAPIView,
    # PublisherListAPIView,
    # PublisherCreateAPIView,
    # PublisherDetailAPIView,
    # device_software_publisher_api_home,
    # DeviceAdamViewSet
)
from rest_framework import renderers
from django.urls import path, include




# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r"publishers", PublisherViewSet)
router.register(r"software", SoftwareViewSet)
router.register(r"devices", DeviceViewSet)
# router.register(r"deviceadam", DeviceAdamViewSet)


urlpatterns = [
    path("api3/", include(router.urls)),
    # path('', device_software_publisher_api_home),
    # # Device
    # path("device/", DeviceListAPIView.as_view(), name="device_list_api"),
    # path("device/create/", DeviceCreateAPIView.as_view(), name="device_create_api"),
    # path("device/<slug:device_slug>/", DeviceDetailAPIView.as_view(), name="device_detail_api"),
    # # path("device/<slug:device_slug>/update/", DeviceUpdateAPIView.as_view(), name="device_update_api"),
    # # path("device/<slug:device_slug>/", DeviceDetailAPIView.as_view(), name="device_detail_api"),
    # # Software
    # path("software/", SoftwareListAPIView.as_view(), name="software_list_api"),
    # path("software/create/", SoftwareCreateAPIView.as_view(), name="software_create_api"),
    # path("software/<slug:slug>/", SoftwareDetailAPIView.as_view(), name="software_detail_api"),
    # path("publisher/", PublisherListAPIView.as_view(), name="publisher_list_api"),
    # # Publisher
    # path("publisher/create/", PublisherCreateAPIView.as_view(), name="publisher_create_api"),
    # path("publisher/<slug:slug>", PublisherDetailAPIView.as_view(), name="publisher_detail_api"),
]
