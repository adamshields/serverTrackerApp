from rest_framework import serializers, request
from rest_framework.reverse import reverse
from servers.models import Server, Software, Publisher
from drf_writable_nested.serializers import *

from django.utils.text import slugify


# Begin Publisher ------------------------------------

class PublisherCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Publisher
        fields = [
            'id',
            'name',
            'status', 
            ]
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'},
        #     # 'name': {'validators': []},
        #     # 'slug': {'validators': []}
        # }


class PublisherDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField("publisher_detail_api", lookup_field='slug')
    class Meta:

        model = Publisher
        fields = [
            'url',
            'id',
            'name',
            'status',
            'software_set', # Reversed
            ]
        lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'},
        #     # 'name': {'validators': []},
        #     # 'slug': {'validators': []}
        # }
        depth = 1


class PublisherListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField("publisher_detail_api", lookup_field='slug')
    class Meta:

        model = Publisher
        fields = [
            'url',
            'id',
            'name',
            'status', 
            'software_set', # Reversed
            ]
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'},
        #     # 'name': {'validators': []},
        #     # 'slug': {'validators': []}
        # }
        depth = 1


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
# End Publisher ------------------------------------

# Begin Software ------------------------------------

class SoftwareCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Software
        fields = [
            'name',
            'status',
            'version',
            ]
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'},
        #     # 'name': {'validators': []},
        #     # 'slug': {'validators': []}
        # }


class SoftwareDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField("software_detail_api", lookup_field='slug')
    class Meta:

        model = Software
        fields = [
            'url',
            'id',
            'name',
            'slug',
            'status',
            'version',
            ]
        lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'},
        #     # 'name': {'validators': []},
        #     # 'slug': {'validators': []}
        # }


class SoftwareListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField("software_detail_api", lookup_field='slug')
    class Meta:

        model = Software
        fields = [
            'url',
            'id',
            'slug',
            'name',
            'status',
            'version',
            ]
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'},
        #     # 'name': {'validators': []},
        #     # 'slug': {'validators': []}
        # }



class SoftwareSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Software
        fields = [
            'url',
            'id',
            'name',
            'slug',
            'status',
            'version',

            ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
            # 'name': {'validators': []},
        }

# End Software ------------------------------------


# Begin Server ------------------------------------

# WritableNestedModelSerializer
class ServerCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:

        model = Server
        fields = [
            'id',
            'name',
            'status', 
            'software', 
            ]
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'},
        #     # 'name': {'validators': []},
        #     # 'slug': {'validators': []}
        # }


class ServerDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField("server_detail_api", lookup_field='slug')
    class Meta:

        model = Server
        fields = [
            'url',
            'id',
            'name',
            'status', 
            ]
        lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'},
        #     # 'name': {'validators': []},
        #     # 'slug': {'validators': []}
        # }


class ServerListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField("server_detail_api", lookup_field='slug')
    class Meta:

        model = Server
        fields = [
            'url',
            'id',
            'name',
            'status', 
            'software', 
            ]
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'},
        #     # 'name': {'validators': []},
        #     # 'slug': {'validators': []}
        # }
        depth = 2

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


# End Server ------------------------------------