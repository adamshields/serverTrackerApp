from rest_framework import serializers, request
from rest_framework.reverse import reverse
from restify.models import Server, Software, Publisher, Ait, Project, Environment
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin, NestedUpdateMixin

from django.utils.text import slugify

class AitRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Ait.objects.get(ait_number=data)

class ProjectRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Project.objects.get(project_name=data)

class EnvironmentRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Environment.objects.get(environment_project=data)
class SoftwareRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Software.objects.get(software_name=data)

class PublisherAPIRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Publisher.objects.get(publisher_name=data)

class SoftwareServerAPIRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Server.objects.get(server_name=data)

class ServerRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Server.objects.get(server_name=data)


class PublisherRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Publisher.objects.get(publisher_name=data)

class AitProjectAPIRelatedfield(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Project.objects.get(project_name=data)

class AitEnvironmentAPISerializerRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Environment.objects.get(environment_name=data)

class AitServerAPISerializerRelatedfield(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Server.objects.get(server_name=data)

class BaseHyperlinkedServer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Server

        fields = [
            'url',
            'server_name',
            'server_status',
            ]
        
        extra_kwargs = {
            'url': {'lookup_field': 'server_slug'},
        }



class PublisherSoftwareSerializer(serializers.HyperlinkedModelSerializer):
    # software_publisher = PublisherRelatedField(queryset=Publisher.objects.all(), many=False)
    server = BaseHyperlinkedServer(many=True, source='server_set')
    class Meta:
        model = Software
        fields = [
            'url',
            'software_name',
            'software_version',
            'server',

            ]
        lookup_field = 'software_slug'
        extra_kwargs = {
            'url': {'lookup_field': 'software_slug'},
            # 'software_slug': {'validators': []},
            # 'software_publisher': {'validators': []},
        }


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    # software = SoftwareRelatedField(queryset=Software.objects.all(), many=True, source='software_set')
    software = PublisherSoftwareSerializer(many=True, source='software_set')

    class Meta:
        model = Publisher
        fields = [
            'url',
            'id',
            'publisher_name',
            'publisher_status',
            'software',
            ]
        lookup_field = 'publisher_slug'
        extra_kwargs = {
            'url': {'lookup_field': 'publisher_slug'},
            'publisher_name': {'validators': []},
            'publisher_slug': {'validators': []},
        }

        
class SoftwareAPISerializer(serializers.HyperlinkedModelSerializer):
    software_publisher = PublisherAPIRelatedField(queryset=Publisher.objects.all(), many=False)
    server = BaseHyperlinkedServer(many=True, source='server_set')
    class Meta:
        model = Software
        fields = [
            'url',
            'software_publisher',
            'software_name',
            'software_version',
            'server',

            ]
        lookup_field = 'software_slug'
        extra_kwargs = {
            'url': {'lookup_field': 'software_slug'},
        }

        
class SoftwareSerializer(serializers.ModelSerializer):
    software_publisher = PublisherRelatedField(queryset=Publisher.objects.all(), many=False)
    class Meta:
        model = Software
        fields = [
            'software_publisher',
            'software_name',
            'software_version',

            ]
        lookup_field = 'software_slug'
        extra_kwargs = {
            # 'software_name': {'validators': []},
            # 'software_slug': {'validators': []},
            # 'software_publisher': {'validators': []},
        }

        


# class ServerSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
# class ServerSerializer(serializers.ModelSerializer):
class ServerSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(context={'request':request})
    server_ait          = AitRelatedField(queryset=Ait.objects.all())
    server_project      = ProjectRelatedField(queryset=Project.objects.all())
    server_environment  = EnvironmentRelatedField(queryset=Environment.objects.all())
    server_software     = SoftwareSerializer(many=True)
    class Meta:

        model = Server
        fields = [
            'url',
            'server_name',
            'server_status', 
            'server_ait',
            'server_project',
            'server_environment',
            'server_software', 
            ]
        lookup_field = 'server_slug'
        extra_kwargs = {
            'url': {'lookup_field': 'server_slug'},
        }



class ProjectAitSerializer(serializers.ModelSerializer):

    class Meta:

        model = Ait
        fields = [
            'url',
            'ait_number',
            # 'project_ait',

            ]
        lookup_field = 'ait_slug'
        # depth = 1
        extra_kwargs = {
            'url': {'lookup_field': 'ait_slug'},
        }

class ProjectSerializer(serializers.ModelSerializer):
    # project_ait = ProjectAitSerializer(many=False)
    project_ait          = AitRelatedField(queryset=Ait.objects.all())
    project_server       = BaseHyperlinkedServer(many=True, source='server_set')

    class Meta:

        model = Project
        fields = [
            'url',
            'project_ait',
            'project_name',
            'project_server',
            # 'server_set',

            ]
        lookup_field = 'project_slug'
        depth = 1
        extra_kwargs = {
            'url': {'lookup_field': 'project_slug'},
        }

class EnvironmentSerializer(serializers.HyperlinkedModelSerializer):
    environment_project      = ProjectRelatedField(queryset=Project.objects.all())
    environment_servers      = BaseHyperlinkedServer(many=True, source='server_set')
    class Meta:

        model = Environment
        fields = [
            'url',
            'id',
            'environment_name',
            'environment_project',
            'environment_servers',

            ]
        lookup_field = 'environment_slug'

        extra_kwargs = {
            'url': {'lookup_field': 'environment_slug'},
        }



class AitEnvironmentSerializer(serializers.ModelSerializer):
    # environment_project = ProjectSerializer()
    # server  = AitServerAPISerializerRelatedfield(queryset=Server.objects.all(), many=True, source='server_set')
    server  = BaseHyperlinkedServer(many=True, source='server_set')
    class Meta:

        model = Environment
        fields = [
            'url',
            'id',
            # 'environment_project',
            'environment_name',
            'server',

            ]
        lookup_field = 'environment_slug'
        # depth = 1
        extra_kwargs = {
            'url': {'lookup_field': 'environment_slug'},
        }

class AitProjectSerializer(serializers.HyperlinkedModelSerializer):
    # server = AitServerProjectSerializer(many=True, source='server_set')
    # environment_set = EnvironmentRelatedField(read_only=True)
    # environment  = AitEnvironmentAPISerializerRelatedField(queryset=Environment.objects.all(), many=True, source='environment_set')
    environment  = AitEnvironmentSerializer(many=True, source='environment_set')
    class Meta:

        model = Project
        fields = [
            # 'id',
            'url',
            'project_name',
            'environment',
            # 'server',

            ]
        lookup_field = 'project_slug'
        extra_kwargs = {
            'url': {'lookup_field': 'project_slug'},
        }


class AitSerializer(serializers.HyperlinkedModelSerializer):
    project = AitProjectSerializer(many=True, source='project_set')
    
    # server_set = AitServerSerializer(many=True)
    # project = AitProjectAPIRelatedfield(queryset=Project.objects.all(), many=True, source='project_set')
    # server = SoftwareServerAPIRelatedField(queryset=Server.objects.all(), many=True, source='server_set')
    class Meta:

        model = Ait
        fields = [
            'url',
            'id',
            'ait_number',
            'project',
            # 'project',
            # 'server',

            ]
        # lookup_field = 'ait_slug'
        extra_kwargs = {
            'url': {'lookup_field': 'ait_slug'},
        }
