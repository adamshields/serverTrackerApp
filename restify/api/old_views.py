from restify.models import Publisher, Software, Server
from .serializers import (
    # PublisherCreateUpdateSerializer,
    # PublisherDetailSerializer,
    # PublisherListSerializer,
    # SoftwareCreateUpdateSerializer,
    # SoftwareDetailSerializer,
    # SoftwareListSerializer,
    PublisherSerializer,
    SoftwareSerializer,
    ServerSerializer,
    # ServerCreateUpdateSerializer,
    # ServerDetailSerializer,
    # ServerListSerializer,
)
from rest_framework import viewsets
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

# # Begin Viewsets ------------------------------------


class PublisherViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    PublisherViewSet
    """

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = 'publisher_slug'


class SoftwareViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    SoftwareViewSet
    """

    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    lookup_field = 'software_slug'


class ServerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    ServerViewSet
    """

    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    lookup_field = 'server_slug'


# End ViewSets ------------------------------------


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse


# @api_view(["GET"])
# def server_software_publisher_api_home(request, format=None):
#     return Response(
#         {
#             "servers": reverse("server_list_api", request=request, format=format),
#             "software": reverse("software_list_api", request=request, format=format),
#             "publisher": reverse("publisher_list_api", request=request, format=format),
#         }
#     )

# # Begin API Views ------------------------------------

# class PublisherCreateAPIView(CreateAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherCreateUpdateSerializer


# class PublisherDetailAPIView(RetrieveAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherDetailSerializer
#     lookup_field = 'publisher_slug'


# class PublisherListAPIView(ListAPIView):
#     queryset = Publisher.objects.all()
#     serializer_class = PublisherListSerializer
#     lookup_field = 'publisher_slug'


# class SoftwareCreateAPIView(CreateAPIView):
#     queryset = Software.objects.all()
#     serializer_class = SoftwareCreateUpdateSerializer


# class SoftwareDetailAPIView(RetrieveAPIView):
#     queryset = Software.objects.all()
#     serializer_class = SoftwareDetailSerializer
#     lookup_field = 'software_slug'


# class SoftwareListAPIView(ListAPIView):
#     queryset = Software.objects.all()
#     serializer_class = SoftwareListSerializer
#     lookup_field = 'software_slug'


# class ServerCreateAPIView(CreateAPIView):
#     queryset = Server.objects.all()
#     serializer_class = ServerCreateUpdateSerializer


# class ServerDetailAPIView(RetrieveAPIView):
#     queryset = Server.objects.all()
#     serializer_class = ServerDetailSerializer
#     lookup_field = 'server_slug'


# class ServerListAPIView(ListAPIView):
#     queryset = Server.objects.all()
#     serializer_class = ServerListSerializer
#     lookup_field = 'server_slug'

# # End API Views ------------------------------------


from restify.models import Publisher, Software, Server
from django.core.exceptions import ObjectDoesNotExist

from .serializers import (
    PublisherSerializer,
    SoftwareSerializer,
    ServerSerializer,
)
from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

class PublisherViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    PublisherViewSet
    """

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = 'publisher_slug'


class SoftwareViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    SoftwareViewSet
    """

    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    lookup_field = 'software_slug'


class ServerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    ServerViewSet
    """

    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    lookup_field = 'server_slug'


    def create(self, request, *args, **kwargs):
        
        data = request.data
        print(data)

        server, created = Server.objects.update_or_create(
            server_name = data['server_name'],
            defaults = {
                'server_status': data['server_status']
            }
        )
        software_data = data['server_software']

        for publisher in software_data:
            publisher, created = Publisher.objects.update_or_create(
                publisher_name = publisher['software_publisher']
            )
        if created == False:
            print(f'\nUpdated {publisher.publisher_name}')
        else:
            print(f'\nCreated {publisher.publisher_name}')

        for software in software_data:
            software, created = Software.objects.update_or_create(
                software_name = software['software_name'],
                software_version = software['software_version'],
                software_publisher = Publisher.objects.get(publisher_name=software['software_publisher'])
            )
            print(f'\n{software.software_publisher} | {software.software_name} | {software.software_version} ')
            server.server_software.add(software)
        serializer = ServerSerializer(server)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def partial_update(self, request, *args, **kwargs):
    #     print(f'This is request.data on partial update:\n {request.data}')
    #     serialized = ServerSerializer(data=request.data, partial=True)
    #     print(f'\n Running Partial Update \n')
    #     if serialized.is_valid():
    #     # if serialized.is_valid(raise_exception=True):
    #         serialized.save()
    #     headers = self.get_success_headers(serialized.data)
    #     return Response(serialized.data, status=status.HTTP_201_CREATED, headers=headers)
    def update(self, request, *args, **kwargs):
        data = request.data
        print(data)

        server, created = Server.objects.update_or_create(
            server_name = data['server_name'],
            defaults = {
                'server_status': data['server_status']
            }
        )
        software_data = data['server_software']
        try:
        # try something
            for publisher in software_data:
                publisher = Publisher.objects.get(
                    publisher_name = publisher['software_publisher']
                )
        except Publisher.DoesNotExist:
            # do something
            for publisher in software_data:
                print(f'\nCreating New Publisher {publisher}')
                # print(f'\nCreating New Publisher {publisher["software_publisher"]}')
                publisher = Publisher.objects.create(
                    publisher_name = publisher['software_publisher']
                )
                print(f'\n{publisher.publisher_name}\n')


        # for publisher in software_data:
        #     publisher, created = Publisher.objects.update_or_create(
        #         publisher_name = publisher['software_publisher']
        #     )
        # if created == False:
        #     print(f'\nUpdated {publisher.publisher_name}')
        # else:
        #     print(f'\nCreated {publisher.publisher_name}')

        for software in software_data:
            software, created = Software.objects.update_or_create(
                software_name = software['software_name'],
                software_version = software['software_version'],
                software_publisher = Publisher.objects.get(publisher_name=software['software_publisher'])
            )
            print(f'\n{software.software_publisher} | {software.software_name} | {software.software_version} ')
            server.server_software.add(software)


        serializer = ServerSerializer(server)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)










from restify.models import Publisher, Software, Server
from django.core.exceptions import ObjectDoesNotExist

from .serializers import (
    PublisherSerializer,
    SoftwareSerializer,
    ServerSerializer,
)
from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status

class PublisherViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    PublisherViewSet
    """

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = 'publisher_slug'


class SoftwareViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    SoftwareViewSet
    """

    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    lookup_field = 'software_slug'


class ServerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    ServerViewSet
    """

    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    lookup_field = 'server_slug'


    def create(self, request, *args, **kwargs):
        
        data = request.data
        print(data)

        server, created = Server.objects.update_or_create(
            server_name = data['server_name'],
            defaults = {
                'server_status': data['server_status']
            }
        )
        software_data = data['server_software']

        for publisher in software_data:
            publisher, created = Publisher.objects.update_or_create(
                publisher_name = publisher['software_publisher']
            )
        if created == False:
            print(f'\nUpdated {publisher.publisher_name}')
        else:
            print(f'\nCreated {publisher.publisher_name}')

        for software in software_data:
            software, created = Software.objects.update_or_create(
                software_name = software['software_name'],
                software_version = software['software_version'],
                software_publisher = Publisher.objects.get(publisher_name=software['software_publisher'])
            )
            print(f'\n{software.software_publisher} | {software.software_name} | {software.software_version} ')
            server.server_software.add(software)
        serializer = ServerSerializer(server)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def partial_update(self, request, *args, **kwargs):
    #     print(f'This is request.data on partial update:\n {request.data}')
    #     serialized = ServerSerializer(data=request.data, partial=True)
    #     print(f'\n Running Partial Update \n')
    #     if serialized.is_valid():
    #     # if serialized.is_valid(raise_exception=True):
    #         serialized.save()
    #     headers = self.get_success_headers(serialized.data)
    #     return Response(serialized.data, status=status.HTTP_201_CREATED, headers=headers)
    def update(self, request, *args, **kwargs):
        
        data = request.data
        
        server, created = Server.objects.update_or_create(
            server_name = data['server_name'],
            defaults = {
                'server_status': data['server_status']
            }
        )
        software_data = data['server_software']
        # publisher_list = []
        for publisher in software_data:
            print(f'\nCreating New Publisher {publisher}')
            # print(f'\nCreating New Publisher {publisher["software_publisher"]}')
            publisher = Publisher.objects.get_or_create(
                publisher_name = publisher['software_publisher']
            )
            # print(Publisher.objects.get(id=publisher))
            # publisher_list.append(publisher)
            # print(f'\nLIST {publisher_list}')
        # try:
        #     for publisher in software_data:
        #         publisher = Publisher.objects.get(
        #             publisher_name = publisher['software_publisher']
        #         )
        #         print(f'\nPublisher Exists {publisher}')
        # except Publisher.DoesNotExist:
        #     for publisher in software_data:
        #         print(f'\nCreating New Publisher {publisher}')
        #         # print(f'\nCreating New Publisher {publisher["software_publisher"]}')
        #         publisher = Publisher.objects.get_or_create(
        #             publisher_name = publisher['software_publisher']
        #         )
        #         print(f'\n{publisher}\n')


        # for publisher in software_data:
        #     publisher, created = Publisher.objects.update_or_create(
        #         publisher_name = publisher['software_publisher']
        #     )
        # if created == False:
        #     print(f'\nUpdated {publisher.publisher_name}')
        # else:
        #     print(f'\nCreated {publisher.publisher_name}')
        # publisher_list = []
        for software in software_data:
            software, created = Software.objects.update_or_create(
                software_name = software['software_name'],
                software_version = software['software_version'],
                software_publisher = Publisher.objects.get(publisher_name=software['software_publisher'])
            )
            print(f'\n{software.software_publisher.id} | {software.software_publisher} | {software.software_name} | {software.software_version} ')
            # publisher_list.append(software.software_publisher.id)
            # print(publisher_list)
            server.server_software.add(software)

        # print(f'\nSERVER_NAME {server.server_name}')
        # print(f'\nSERVER_STATUS {server.server_status}')
        # print(f'\nSOFTWARE_DATA {software.software_publisher} | {software.software_name} | {software.software_version}')
        # print(f'\nSOFTWARE {software}')
        # print(f'\nSERVER_STATUS {server.server_software}')
        # server.save()
        # software.save()
        serializer = ServerSerializer(server)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)