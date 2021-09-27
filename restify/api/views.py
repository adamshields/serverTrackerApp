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
            import re
            publisher_name = publisher['software_publisher']
            # Match and strip punctuation with re.sub()
            updatedpub = re.sub(pattern = "[^\w\s]",
                    repl = "",
                    string = publisher_name)
            # publisher_name = publisher['software_publisher'].replace(',', '')
            # publisher_name = publisher['software_publisher'].strip(",.").upper()
            # publisher_name = publisher['software_publisher'].re.sub(pattern = "[^\w\s]")
            print(f'This is loop publisher: {updatedpub}')
            publisher, created = Publisher.objects.update_or_create(
                publisher_name = updatedpub
            )
        if created == False:
            print(f'\nUpdated {publisher.publisher_name}')
        else:
            print(f'\nCreated {publisher.publisher_name}')

        for software in software_data:
            software, created = Software.objects.update_or_create(
                software_name = software['software_name'],
                software_version = software['software_version'],
                software_publisher = Publisher.objects.get(publisher_name=updatedpub)
            )
            print(f'\n{software.software_publisher} | {software.software_name} | {software.software_version} ')
            server.server_software.add(software)
        serializer = ServerSerializer(server)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    
    def update(self, request, *args, **kwargs):
        
        data = request.data
        
        server, created = Server.objects.update_or_create(
            server_name = data['server_name'],
            defaults = {
                'server_status': data['server_status']
            }
        )

        server.server_software.clear()
        
        software_data = data['server_software']
        
        for publisher in software_data:
            publisher, created = Publisher.objects.get_or_create(
                publisher_name = publisher['software_publisher']
            )
            if created is True:
                print(f'\nCreating New Publisher: {publisher}')
            else:
                print(f'\nExisting Publisher: {publisher}')
                
        for software in software_data:
            software, created = Software.objects.get_or_create(
                software_name = software['software_name'],
                software_version = software['software_version'],
                software_publisher = Publisher.objects.get(publisher_name=software['software_publisher'])
            )
            if created is True:
                print(f'\nNew Software: {software.software_publisher.id} | {software.software_publisher} | {software.software_name} | {software.software_version} ')
            else:
                print(f'\nExisting Software: {software.software_publisher.id} | {software.software_publisher} | {software.software_name} | {software.software_version} ')
            
            # software_list.append(server.server_software.software_name)
            # server.server_software.add(software_list)
            
            server.server_software.add(software)
            # print(publisher_list)

        serializer = ServerSerializer(server)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)