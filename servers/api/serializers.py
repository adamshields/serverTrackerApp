from rest_framework import serializers, request
from rest_framework.reverse import reverse
from servers.models import Server, Software, Publisher
from drf_writable_nested.serializers import *

from django.utils.text import slugify




class PublisherSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Publisher
        fields = [
            'url',
            'id',
            'name',
            'status',
            ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
            # 'name': {'validators': []},
        }


class SoftwareSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Software
        fields = [
            'url',
            'id',
            'name',
            'status',
            'version',

            ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
            # 'name': {'validators': []},
        }


# WritableNestedModelSerializer
class ServerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Server
        fields = [
            'url',
            'id',
            'name',
            'status', 
            ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
            # 'name': {'validators': []},
            # 'slug': {'validators': []}
        }
