from rest_framework import serializers, request
from rest_framework.reverse import reverse
from restify.models import Device, Software, Publisher, Ait, Project, Environment
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin, NestedUpdateMixin

from django.utils.text import slugify


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = [
            'id',
            'publisher_name',
            'publisher_status',
            ]
        lookup_field = 'publisher_slug'
        extra_kwargs = {
            'url': {'lookup_field': 'publisher_slug'},
            'publisher_name': {'validators': []},
            'publisher_slug': {'validators': []},
        }


class PublisherRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Publisher.objects.get(publisher_name=data)
        
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

class DeviceSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    device_ait          = AitRelatedField(queryset=Ait.objects.all())
    device_project      = ProjectRelatedField(queryset=Project.objects.all())
    device_environment  = ProjectRelatedField(queryset=Environment.objects.all())
    device_software     = SoftwareSerializer(many=True)
    class Meta:

        model = Device
        fields = [
            'device_name',
            'device_status', 
            'device_ait',
            'device_project',
            'device_environment',
            'device_software', 
            ]
        lookup_field = 'device_slug'



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
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    project_ait = ProjectAitSerializer(many=False)
    class Meta:

        model = Project
        fields = [
            'url',
            'project_name',
            'project_ait',

            ]
        lookup_field = 'project_slug'
        depth = 1
        extra_kwargs = {
            'url': {'lookup_field': 'project_slug'},
        }

class EnvironmentSerializer(serializers.HyperlinkedModelSerializer):
    environment_project = ProjectSerializer()
    class Meta:

        model = Environment
        fields = [
            'url',
            'id',
            'environment_project',
            'environment_name',

            ]
        lookup_field = 'environment_slug'
        depth = 1
        extra_kwargs = {
            'url': {'lookup_field': 'environment_slug'},
        }
class AitDeviceProjectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Device
        fields = [
            'url',
            # 'id',
            'device_name',
            # 'project_ait',
            # 'device_set',

            ]
        lookup_field = 'device_slug'
        extra_kwargs = {
            'url': {'lookup_field': 'device_slug'},
        }

class AitDeviceSerializer(serializers.ModelSerializer):

    class Meta:

        model = Device
        fields = [
            'device_name',
            'device_status', 
            ]
        lookup_field = 'device_slug'

class AitProjectSerializer(serializers.ModelSerializer):
    device_set = AitDeviceProjectSerializer(many=True)
    # environment_set = EnvironmentRelatedField(read_only=True)
    # environment_set  = ProjectRelatedField(queryset=Environment.objects.all(), many=True)
    # location = serializers.SerializerMethodField('get_alternate_name')
    project_environments = serializers.SerializerMethodField('get_project_environments')

    class Meta:

        model = Project
        fields = [
            # 'id',
            'url',
            # 'location',
            'project_name',
            'project_environments',
            
            # 'environment_set',
            'device_set',

            ]
        lookup_field = 'project_slug'
        # depth = 1
        extra_kwargs = {
            'url': {'lookup_field': 'project_slug'},
        }
    # def get_alternate_name(self, obj):
    #     return str(obj.project_ait)
    def get_project_environments(self, obj):
        project_environments = obj.environment_set.all() # will return product query set associate with this category
        response = AitProjectSerializer(project_environments, many=True).data
        return response

#    def get_products(self, obj):
#        project_environments = obj.environment_set.all() # will return product query set associate with this category
#        response = EnvironmentSerializer(environment_name, many=True).data
#        return response

class AitSerializer(serializers.HyperlinkedModelSerializer):
    project_set = AitProjectSerializer(many=True)
    # device_set = AitDeviceSerializer(many=True)
    class Meta:

        model = Ait
        fields = [
            'url',
            'id',
            'ait_number',
            # 'project_environments',
            'project_set',
            # 'device_set',

            ]
        lookup_field = 'ait_slug'
        extra_kwargs = {
            'url': {'lookup_field': 'ait_slug'},
        }

