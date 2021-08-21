from rest_framework import serializers, request
from rest_framework.reverse import reverse
from servers.models import Server, Software, Publisher
from drf_writable_nested.serializers import *

from django.utils.text import slugify


# """
# Test Code
# from servers.api.serializers import PublisherCreateUpdateSerializer
# serializer = PublisherCreateUpdateSerializer()
# print(repr(serializer))
# """




# Begin Publisher ------------------------------------

class PublisherCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Test Code
    from servers.api.serializers import PublisherCreateUpdateSerializer
    serializer = PublisherCreateUpdateSerializer()
    print(repr(serializer))
    """

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
    """
    Test Code
    from servers.api.serializers import PublisherDetailSerializer
    serializer = PublisherDetailSerializer()
    print(repr(serializer))
    """

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
    """
    Test Code
    from servers.api.serializers import PublisherListSerializer
    serializer = PublisherListSerializer()
    print(repr(serializer))
    """

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
    """
    Test Code
    from servers.api.serializers import PublisherSerializer
    serializer = PublisherSerializer()
    print(repr(serializer))
    """
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

class SoftwareCreateUpdateCustomSerializer(serializers.Serializer):
    """
    Test Code
    from servers.api.serializers import SoftwareCreateUpdateCustomSerializer
    serializer = SoftwareCreateUpdateCustomSerializer()
    print(repr(serializer))
    """

    class Meta:

        model = Software
        fields = [
            'name',
            'status',
            'version',
            'publisher',
            ]
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'},
        #     # 'name': {'validators': []},
        #     # 'slug': {'validators': []}
        # }







class SoftwareCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Test Code
    from servers.api.serializers import SoftwareCreateUpdateSerializer
    serializer = SoftwareCreateUpdateSerializer()
    print(repr(serializer))
    """
    class Meta:

        model = Software
        fields = [
            'name',
            'status',
            'version',
            'publisher',
            ]
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'},
        #     # 'name': {'validators': []},
        #     # 'slug': {'validators': []}
        # }



class SoftwareDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField("software_detail_api", lookup_field='slug')
    """
    Test Code
    from servers.api.serializers import SoftwareDetailSerializer
    serializer = SoftwareDetailSerializer()
    print(repr(serializer))
    """
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
    """
    Test Code
    from servers.api.serializers import SoftwareListSerializer
    serializer = SoftwareListSerializer()
    print(repr(serializer))
    """
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
    """
    Test Code
    from servers.api.serializers import SoftwareSerializer
    serializer = SoftwareSerializer()
    print(repr(serializer))
    """

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
    """
    Test Code
    from servers.api.serializers import ServerCreateUpdateSerializer
    serializer = ServerCreateUpdateSerializer()
    print(repr(serializer))
    """

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
    """
    Test Code
    from servers.api.serializers import ServerDetailSerializer
    serializer = ServerDetailSerializer()
    print(repr(serializer))
    """
    class Meta:

        model = Server
        fields = [
            'url',
            'id',
            'name',
            'status', 
            'software', 
            ]
        lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'},
        #     # 'name': {'validators': []},
        #     # 'slug': {'validators': []}
        # }
        depth = 1

class ServerListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField("server_detail_api", lookup_field='slug')
    """
    Test Code
    from servers.api.serializers import ServerListSerializer
    serializer = ServerListSerializer()
    print(repr(serializer))
    """
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
    """
    Test Code
    from servers.api.serializers import ServerSerializer
    serializer = ServerSerializer()
    print(repr(serializer))
    """
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