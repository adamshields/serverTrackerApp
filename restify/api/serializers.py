from rest_framework import serializers, request
from rest_framework.reverse import reverse
from restify.models import Device, Software, Publisher, Ait, Project, Environment
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

class SoftwareDeviceAPIRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Device.objects.get(device_name=data)

class DeviceRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Device.objects.get(device_name=data)


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

class AitDeviceAPISerializerRelatedfield(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Device.objects.get(device_name=data)

class BaseHyperlinkedDevice(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Device

        fields = [
            'url',
            'device_name',
            'device_status',
            ]
        
        extra_kwargs = {
            'url': {'lookup_field': 'device_slug'},
        }



class PublisherSoftwareSerializer(serializers.HyperlinkedModelSerializer):

    device = BaseHyperlinkedDevice(many=True, source='device_set')

    class Meta:

        model = Software

        fields = [
            'url',
            'software_name',
            'software_version',
            'device',

            ]

        extra_kwargs = {
            'url': {'lookup_field': 'software_slug'},
        }


class PublisherSerializer(serializers.HyperlinkedModelSerializer):

    software = PublisherSoftwareSerializer(many=True, source='software_set')

    class Meta:

        model = Publisher

        fields = [
            'url',
            'publisher_name',
            'publisher_status',
            'software',
            ]

        extra_kwargs = {
            'url': {'lookup_field': 'publisher_slug'},
        }

        
class SoftwareAPISerializer(serializers.HyperlinkedModelSerializer):

    software_publisher = PublisherAPIRelatedField(queryset=Publisher.objects.all(), many=False)
    device = BaseHyperlinkedDevice(many=True, source='device_set')

    class Meta:

        model = Software

        fields = [
            'url',
            'software_publisher',
            'software_name',
            'software_version',
            'device',
            ]

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

        extra_kwargs = {
            # 'software_name': {'validators': []},
            # 'software_slug': {'validators': []},
            # 'software_publisher': {'validators': []},
        }

        
class DeviceSerializer(serializers.HyperlinkedModelSerializer):

    device_ait          = AitRelatedField(queryset=Ait.objects.all())
    device_project      = ProjectRelatedField(queryset=Project.objects.all())
    device_environment  = EnvironmentRelatedField(queryset=Environment.objects.all())
    device_software     = SoftwareSerializer(many=True)

    class Meta:

        model = Device

        fields = [
            'url',
            'device_name',
            'device_status', 
            'device_ait',
            'device_project',
            'device_environment',
            'device_software', 
            ]

        extra_kwargs = {
            'url': {'lookup_field': 'device_slug'},
        }


class EnvironmentSerializer(serializers.HyperlinkedModelSerializer):

    environment_project      = ProjectRelatedField(queryset=Project.objects.all())
    environment_devices      = BaseHyperlinkedDevice(many=True, source='device_set')

    class Meta:

        model = Environment

        fields = [
            'url',
            'environment_name',
            'environment_project',
            'environment_devices',
            ]

        extra_kwargs = {
            'url': {'lookup_field': 'environment_slug'},
        }


class ProjectEnvironmentSerializer(serializers.HyperlinkedModelSerializer):

    environment_devices      = BaseHyperlinkedDevice(many=True, source='device_set')
    
    class Meta:

        model = Environment

        fields = [
            'url',
            'environment_name',
            'environment_devices',
            ]

        extra_kwargs = {
            'url': {'lookup_field': 'environment_slug'},
        }

class ProjectSerializer(serializers.ModelSerializer):

    project_ait              = AitRelatedField(queryset=Ait.objects.all())
    environment_project      = ProjectEnvironmentSerializer(many=True, source='environment_set')

    class Meta:

        model = Project
        fields = [
            'url',
            'project_ait',
            'project_name',
            'environment_project',

            ]
        lookup_field = 'project_slug'
        depth = 1
        extra_kwargs = {
            'url': {'lookup_field': 'project_slug'},
        }


class AitEnvironmentSerializer(serializers.ModelSerializer):

    device  = BaseHyperlinkedDevice(many=True, source='device_set')
    
    class Meta:

        model = Environment
        fields = [
            'url',
            'environment_name',
            'device',
            ]

        extra_kwargs = {
            'url': {'lookup_field': 'environment_slug'},
        }

class AitProjectSerializer(serializers.HyperlinkedModelSerializer):

    environment  = AitEnvironmentSerializer(many=True, source='environment_set')

    class Meta:

        model = Project

        fields = [
            'url',
            'project_name',
            'environment',
            ]

        extra_kwargs = {
            'url': {'lookup_field': 'project_slug'},
        }


class AitSerializer(serializers.HyperlinkedModelSerializer):
    
    project = AitProjectSerializer(many=True, source='project_set')
    
    class Meta:

        model = Ait

        fields = [
            'url',
            'ait_number',
            'project',
            ]

        extra_kwargs = {
            'url': {'lookup_field': 'ait_slug'},
        }
