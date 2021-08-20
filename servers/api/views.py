from servers.models import Publisher, Software, Server
from .serializers import PublisherSerializer, SoftwareSerializer, ServerSerializer
from rest_framework import viewsets


class PublisherViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    PublisherViewSet
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = 'slug'

class SoftwareViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    SoftwareViewSet
    """
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    lookup_field = 'slug'

class ServerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    ServerViewSet
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    lookup_field = 'slug'