from rest_framework import serializers, request
from rest_framework.reverse import reverse
from restify.models import Server, Software, Publisher
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

        

class ServerSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
    server_software = SoftwareSerializer(many=True)
    class Meta:

        model = Server
        fields = [
            'server_name',
            'server_status', 
            'server_software', 
            ]
        lookup_field = 'server_slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'server_slug'},
        #     'server_name': {'validators': []},
        #     'server_slug': {'validators': []},
        # }

    # def create(self, validated_data):
    #     software_data = validated_data.pop('server_software')
    #     server, created = Server.objects.update_or_create(
    #         server_name = validated_data.get('server_name', None),
    #         defaults={
    #             'server_status': validated_data.get('server_status', None),
    #         })
            
    #     for publisher in software_data:
    #         publisher, created = Publisher.objects.create(
    #             publisher_name = publisher['software_publisher'],
    #         )
    #     if created == False:
    #         print(f'Updated {publisher.publisher_name} ')
    #     else:
    #         print(f'Created {publisher.publisher_name} ')

    #     for software in software_data:
    #         software, created = Software.objects.update_or_create(
    #             software_name = software['software_name'],
    #             defaults={
    #                 'software_version': software['software_version'],
    #                 'software_publisher': Publisher.objects.get(publisher_name=software['software_publisher'])
    #             })
    #         print(f'\n{software.software_publisher} | {software.software_name} | {software.software_version} ')
    #         server.server_software.add(software)
    #     if created == False:
    #         print(f'Updated {software.name} name')
    #     else:
    #         print(f'Created {software.name} name')
    #     return server