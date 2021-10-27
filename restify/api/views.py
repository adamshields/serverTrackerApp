from restify.models import Publisher, Software, Device, Ait, Project, Environment
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import (
    PublisherSerializer,
    SoftwareSerializer,
    SoftwareAPISerializer,
    DeviceSerializer,
    AitSerializer, 
    ProjectSerializer, 
    EnvironmentSerializer
)
from rest_framework import viewsets
import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status



class AitViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    AitViewSet
    """
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ait_number']

    queryset = Ait.objects.all()
    serializer_class = AitSerializer
    lookup_field = 'ait_slug'

class ProjectViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Project
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'project_slug'

class EnvironmentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Project
    """

    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    lookup_field = 'environment_slug'


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
    SoftwareViewSet
    """
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['software_publisher']

    queryset = Software.objects.all()
    serializer_class = SoftwareAPISerializer
    lookup_field = 'software_slug'

class DeviceViewSet(viewsets.ModelViewSet):
    """
    DeviceViewSet
    """
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['device_ait__ait_number', 'device_project__project_name', 'device_environment__environment_name', 'device_software__software_name']

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'device_slug'
    


    def create(self, request, *args, **kwargs):
        
        data = request.data

        ait, created = Ait.objects.update_or_create(
            ait_number = data['device_ait']
        )
        if created == False:
            print(f'\nUpdated AIT: {ait.ait_number}')
        else:
            print(f'\nCreated AIT: {ait.ait_number}')


        project, created = Project.objects.update_or_create(
            project_name = data['device_project'],
            project_ait = Ait.objects.get(ait_number=ait.ait_number)
        )
        if created == False:
            print(f'\nUpdated Project: {project.project_name}')
        else:
            print(f'\nCreated Project: {project.project_name}')


        environment, created = Environment.objects.update_or_create(
            environment_name = data['device_environment'],
            environment_project = Project.objects.get(project_name=project.project_name, project_slug=project.project_slug),
            # environment_slug = slugify(data['device_environment'] + '-' + slugify(project.project_name)),
            
        )
        # environment.environment_project.add(project)
        if created == False:
            print(f'\nUpdated Environment: {environment.environment_name} | {environment.environment_project} | {environment.environment_slug}')
        else:
            print(f'\nCreated Environment: {environment.environment_name} | {environment.environment_project} | {environment.environment_slug}')


        device, created = Device.objects.update_or_create(
            device_name = data['device_name'],
            # device_ait = Ait.objects.get(ait_number=ait.ait_number),
            # device_project = Project.objects.get(project_name=project.project_name, project_slug=project.project_slug),
            # device_environment = Environment.objects.get(environment_name=environment.environment_name, environment_project=environment.environment_project),
            defaults = {
                'device_status': data['device_status'],
                'device_ait': Ait.objects.get(ait_number=ait.ait_number),
                'device_project': Project.objects.get(project_name=project.project_name, project_slug=project.project_slug),
                'device_environment': Environment.objects.get(environment_name=environment.environment_name, environment_project=environment.environment_project),
            }
        )
        software_data = data['device_software']

        for publisher in software_data:

            publisher_name = publisher['software_publisher']
            # Match and strip punctuation with re.sub()
            publisher_name = re.sub(pattern = "[^\w\s]",
                    repl = "",
                    string = publisher_name)
            print(f'This is loop publisher: {publisher_name}')
            publisher, created = Publisher.objects.update_or_create(
                publisher_name = publisher_name
            )
        if created == False:
            print(f'\nUpdated {publisher.publisher_name}')
        else:
            print(f'\nCreated {publisher.publisher_name}')

        for software in software_data:
            publisher_name=software['software_publisher']
            publisher_name = re.sub(pattern = "[^\w\s]",
                    repl = "",
                    string = publisher_name)
            print(f'This is loop publisher: {publisher_name}')
            software, created = Software.objects.update_or_create(
                software_name = software['software_name'],
                software_version = software['software_version'],
                software_publisher = Publisher.objects.get(publisher_name=publisher_name)
            )
            print(f'\n{software.software_publisher} | {software.software_name} | {software.software_version} ')
            device.device_software.add(software)

        serializer = DeviceSerializer(device, context={'request': request})
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def update(self, request, *args, **kwargs):
        
        data = request.data
        
        ait, created = Ait.objects.update_or_create(
            ait_number = data['device_ait']
        )
        if created == False:
            print(f'\nUpdated AIT: {ait.ait_number}')
        else:
            print(f'\nCreated AIT: {ait.ait_number}')


        project, created = Project.objects.update_or_create(
            project_name = data['device_project'],
            project_ait = Ait.objects.get(ait_number=ait.ait_number)
        )
        if created == False:
            print(f'\nUpdated Project: {project.project_name}')
        else:
            print(f'\nCreated Project: {project.project_name}')


        environment, created = Environment.objects.update_or_create(
            environment_name = data['device_environment'],
            environment_project = Project.objects.get(project_name=project.project_name, project_slug=project.project_slug),
            # environment_slug = slugify(data['device_environment'] + '-' + slugify(project.project_name)),
            
        )
        # environment.environment_project.add(project)
        if created == False:
            print(f'\nUpdated Environment: {environment.environment_name} | {environment.environment_project} | {environment.environment_slug}')
        else:
            print(f'\nCreated Environment: {environment.environment_name} | {environment.environment_project} | {environment.environment_slug}')


        device, created = Device.objects.update_or_create(
            device_name = data['device_name'],
            # device_ait = Ait.objects.get(ait_number=ait.ait_number),
            # device_project = Project.objects.get(project_name=project.project_name, project_slug=project.project_slug),
            # device_environment = Environment.objects.get(environment_name=environment.environment_name, environment_project=environment.environment_project),
            defaults = {
                'device_status': data['device_status'],
                'device_ait': Ait.objects.get(ait_number=ait.ait_number),
                'device_project': Project.objects.get(project_name=project.project_name, project_slug=project.project_slug),
                'device_environment': Environment.objects.get(environment_name=environment.environment_name, environment_project=environment.environment_project),
            }
        )
        device.device_software.clear()
        software_data = data['device_software']

        for publisher in software_data:

            publisher_name = publisher['software_publisher']
            # Match and strip punctuation with re.sub()
            publisher_name = re.sub(pattern = "[^\w\s]",
                    repl = "",
                    string = publisher_name)
            print(f'This is loop publisher: {publisher_name}')
            publisher, created = Publisher.objects.update_or_create(
                publisher_name = publisher_name
            )
        if created == False:
            print(f'\nUpdated {publisher.publisher_name}')
        else:
            print(f'\nCreated {publisher.publisher_name}')

        for software in software_data:
            publisher_name=software['software_publisher']
            publisher_name = re.sub(pattern = "[^\w\s]",
                    repl = "",
                    string = publisher_name)
            print(f'This is loop publisher: {publisher_name}')
            software, created = Software.objects.update_or_create(
                software_name = software['software_name'],
                software_version = software['software_version'],
                software_publisher = Publisher.objects.get(publisher_name=publisher_name)
            )
            print(f'\n{software.software_publisher} | {software.software_name} | {software.software_version} ')
            device.device_software.add(software)
        serializer = DeviceSerializer(device)

        serializer = DeviceSerializer(device, context={'request': request})
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    # def update(self, request, *args, **kwargs):
        
    #     data = request.data
        
    #     device, created = Device.objects.update_or_create(
    #         device_name = data['device_name'],
    #         defaults = {
    #             'device_status': data['device_status']
    #         }
    #     )

    #     device.device_software.clear()
        
    #     software_data = data['device_software']
        
    #     for publisher in software_data:
    #         publisher_name = publisher['software_publisher']
    #         # Match and strip punctuation with re.sub()
    #         publisher_name = re.sub(pattern = "[^\w\s]",
    #                 repl = "",
    #                 string = publisher_name)
    #         print(f'This is loop publisher update: {publisher_name}')
    #         publisher, created = Publisher.objects.get_or_create(
    #             publisher_name = publisher_name
    #         )
    #         if created is True:
    #             print(f'\nCreating New Publisher: {publisher}')
    #         else:
    #             print(f'\nExisting Publisher: {publisher}')
                
    #     for software in software_data:
    #         publisher_name=software['software_publisher']
    #         publisher_name = re.sub(pattern = "[^\w\s]",
    #                 repl = "",
    #                 string = publisher_name)
    #         print(f'Software Update Publisher: {publisher_name}')
    #         software, created = Software.objects.get_or_create(
    #             software_name = software['software_name'],
    #             software_version = software['software_version'],
    #             software_publisher = Publisher.objects.get(publisher_name=publisher_name)
    #         )
    #         if created is True:
    #             print(f'\nNew Software: {software.software_publisher.id} | {software.software_publisher} | {software.software_name} | {software.software_version} ')
    #         else:
    #             print(f'\nExisting Software: {software.software_publisher.id} | {software.software_publisher} | {software.software_name} | {software.software_version} ')
            
    #         # software_list.append(device.device_software.software_name)
    #         # device.device_software.add(software_list)
            
    #         device.device_software.add(software)
    #         # print(publisher_list)

    #     serializer = DeviceSerializer(device)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)