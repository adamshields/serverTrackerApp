from servers.models import Publisher, Software, Server
from .serializers import (
    PublisherCreateUpdateSerializer,
    PublisherDetailSerializer,
    PublisherListSerializer,
    SoftwareCreateUpdateSerializer,
    SoftwareDetailSerializer,
    SoftwareListSerializer,
    PublisherSerializer,
    SoftwareSerializer,
    ServerSerializer,
    ServerCreateUpdateSerializer,
    ServerDetailSerializer,
    ServerListSerializer,
)
from rest_framework import viewsets
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def server_software_publisher_api_home(request, format=None):
    return Response(
        {
            "servers": reverse("server_list_api", request=request, format=format),
            "software": reverse("software_list_api", request=request, format=format),
            "publisher": reverse("publisher_list_api", request=request, format=format),
        }
    )

# Begin API Views ------------------------------------

class PublisherCreateAPIView(CreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherCreateUpdateSerializer


class PublisherDetailAPIView(RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherDetailSerializer
    lookup_field = "slug"


class PublisherListAPIView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherListSerializer


class SoftwareCreateAPIView(CreateAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareCreateUpdateSerializer


class SoftwareDetailAPIView(RetrieveAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareDetailSerializer
    lookup_field = "slug"


class SoftwareListAPIView(ListAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareListSerializer
    lookup_field = "slug"


class ServerCreateAPIView(CreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerCreateUpdateSerializer


class ServerDetailAPIView(RetrieveAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerDetailSerializer
    lookup_field = "slug"


class ServerListAPIView(ListAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerListSerializer
    lookup_field = "slug"

# End API Views ------------------------------------

# Begin Viewsets ------------------------------------


class PublisherViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    PublisherViewSet
    """

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = "slug"


class SoftwareViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    SoftwareViewSet
    """

    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    lookup_field = "slug"


class ServerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    ServerViewSet
    """

    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    lookup_field = "slug"


# End ViewSets ------------------------------------
