from rest_framework import serializers, request
from rest_framework.reverse import reverse
from servers.models import Server, Software, Publisher#, CarPlan, CarSpecs
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


# class PublisherSerializer(serializers.HyperlinkedModelSerializer):
#     """
#     Test Code
#     from servers.api.serializers import PublisherSerializer
#     serializer = PublisherSerializer()
#     print(repr(serializer))
#     """
#     class Meta:
#         model = Publisher
#         fields = [
#             'url',
#             'id',
#             'name',
#             'status',
#             ]
#         lookup_field = 'slug'
#         extra_kwargs = {
#             'url': {'lookup_field': 'slug'},
#             # 'name': {'validators': []},
#         }


class PublisherSoftwareSerializer(serializers.Serializer):
    """
    Test Code
    from servers.api.serializers import PublisherSoftwareSerializer
    serializer = PublisherSoftwareSerializer()
    print(repr(serializer))
    """
    name = serializers.CharField(required=True)
    # class Meta:
    #     model = Publisher
    #     fields = [
    #         # 'url',
    #         # 'id',
    #         # 'name',
    #         # 'status',
    #         ]
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'url': {'lookup_field': 'slug'},
            # 'name': {'validators': []},
        # }
# End Publisher ------------------------------------

# Begin Software ------------------------------------


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

# Custom ------------------------------------

# WritableNestedModelSerializer
# class SoftwareCreateUpdateSerializerCustom(serializers.Serializer):
# class SoftwareCreateUpdateSerializerCustom(WritableNestedModelSerializer, serializers.ModelSerializer):
class SoftwareCreateUpdateSerializerCustom(serializers.ModelSerializer):
    """
    Test Code
    from servers.api.serializers import SoftwareCreateUpdateSerializerCustom
    serializer = SoftwareCreateUpdateSerializerCustom()
    print(repr(serializer))
    """
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True)
    # slug = serializers.SlugField(read_only=True)
    # status = serializers.BooleanField(required=False)
    # version = serializers.CharField(required=False)
    # publisher = serializers.PrimaryKeyRelatedField(queryset = Publisher.objects.all(), source='publisher.name')
    # publisher = PublisherSoftwareSerializer(required=True)
    # publisher = serializers.CharField(source='publisher.name')
    # publisher = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    class Meta:
        model = Software
        fields = [
            'name',
            'status',
            'version',
            'publisher',
            ]

        extra_kwargs = {
            'name': {'validators': []},
            # 'slug': {'validators': []}
        }
    # def create(self, validated_data):
    #     return Software.objects.create(**validated_data)
    # def create(self, validated_data):

    #     name = validated_data.get('publisher')
    #     a_name = validated_data.get('publisher.name')
    #     print(a_name)
    #     publisher_name = name['name']


    #     publisher, created = Publisher.objects.get_or_create(
    #         name = publisher_name,
    #         defaults={'status': False},
    #     )
    #     # publisher.software_set.add(publisher)
    #     if created == False:
    #         print(f'Updated {publisher_name} name')
    #         print(f'Updated {publisher} name')
    #     else:
    #         print(f'Created {publisher_name} name') 
        # print(f'\nVALIDATED DATA\n\n----------------------\n{validated_data}\n ----------------------\n\n\n')
        # if Publisher.objects.filter(name=publisher_name).values_list('id', flat=True).exists() == True:
        #     print(f'\n\nPUBLISHER NAME\n----------------------\n{publisher_name}\n----------------------')
        # publisher, created = Publisher.objects.update_or_create(
        #     defaults={
        #         'name': publisher_name,
        #     })
 
    #     # publisher_data = validated_data.get('publisher')
    #     # name = validated_data.get('publisher')
    #     # publisher_name = name['name']
    #     # print(name)
    #     # print(publisher_name)
    #     # # CREATE/UPDATE SOFTWARENAME
    #     # # publisher, created = Publisher.objects.update_or_create(
    #     # #     name=publisher[0],
    #     # #     )
    #     # # publisher.software.add(publisher)
    #     # if created == False:
    #     #     print(f'Updated {publisher_name} name')
    #     #     print(f'Updated {publisher} name')
    #     # else:
    #     #     print(f'Created {publisher_name} name')   
        
        # CREATE/UPDATE SOFTWARENAME
        # if Publisher.objects.filter(name=publisher_name).values_list('id', flat=True).exists() == True:
        #     Publisher.objects.update(name=publisher_name)
            # if created == False:
            #     print(f'Updated {publisher} name')
            # else:
            #     print(f'Created {publisher} name')      
        
        
        # CREATE/UPDATE SOFTWARENAME
        # software, created = Software.objects.update_or_create(
        #     name = validated_data.get('name', None),
        #     defaults={
        #         'name': validated_data.get('name', None),
        #         'status': validated_data.get('status', None),
        #     })
        # publisher.software.add(publisher)
        # # software.publisher.add(software)
        # # publisher.software_set.add(publisher)
        # if created == False:
        #     print(f'Updated {software} name')
        # else:
        #     print(f'Created {software} name')

    #     # for software in software_data:
    #     #     software, created = Software.objects.update_or_create(
    #     #         name=software['name'],
    #     #         version=software['version'],
    #     #         install_date=software['install_date']
    #     #         )
    #     #     server.software.add(software)
    #     # if created == False:
    #     #     print(f'Updated {software.name} name')
    #     # else:
    #     #     print(f'Created {software.name} name')

        # return software

    
    
class SoftwareDetailSerializerCustom(serializers.Serializer):
    """
    Test Code
    from servers.api.serializers import SoftwareDetailSerializerCustom
    serializer = SoftwareDetailSerializerCustom()
    print(repr(serializer))
    """
    publisher = serializers.CharField(source='publisher.name')
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    slug = serializers.SlugField(read_only=True)
    status = serializers.BooleanField(required=False)
    version = serializers.CharField(required=False)
    # publisher = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    # publisher = serializers.CharField()
    

class SoftwareListSerializerCustom(serializers.Serializer):
    """
    Test Code
    from servers.api.serializers import SoftwareListSerializerCustom
    serializer = SoftwareListSerializerCustom()
    print(repr(serializer))
    """
    # publisher_id = serializers.CharField(source='publisher.id')
    publisher = serializers.CharField(source='publisher.name')
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    slug = serializers.SlugField(read_only=True)
    status = serializers.BooleanField(required=False)
    version = serializers.CharField(required=False)
    # publisher = serializers.CharField()

# Custom ------------------------------------

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



# class SoftwareSerializer(serializers.ModelSerializer):
#     """
#     Test Code
#     from servers.api.serializers import SoftwareSerializer
#     serializer = SoftwareSerializer()
#     print(repr(serializer))
#     """

#     class Meta:
#         model = Software
#         fields = [
#             'publisher',
#             'url',
#             'id',
#             'name',
#             'slug',
#             'status',
#             'version',

#             ]
#         lookup_field = 'slug'
#         extra_kwargs = {
#             'url': {'lookup_field': 'slug'},
#             # 'name': {'validators': []},
#         }
#         depth = 1
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

# class ServerSerializer(serializers.HyperlinkedModelSerializer):
#     """
#     Test Code
#     from servers.api.serializers import ServerListSerializer
#     serializer = ServerListSerializer()
#     print(repr(serializer))
#     """
#     class Meta:

#         model = Server
#         fields = [
#             'url',
#             'id',
#             'name',
#             'status', 
#             ]
#         lookup_field = 'slug'
#         extra_kwargs = {
#             'url': {'lookup_field': 'slug'},
#             # 'name': {'validators': []},
#             # 'slug': {'validators': []}
#         }





class SoftwareSerializer(serializers.ModelSerializer):
    # software_publisher = PublisherSerializer()
    """
    Test Code
    from servers.api.serializers import SoftwareSerializer
    serializer = SoftwareSerializer()
    print(repr(serializer))
    """

    class Meta:
        model = Software
        fields = [
            # 'software_publisher',
            'publisher',
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
        # depth = 1

class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    software_set = SoftwareSerializer(many=True, read_only=True)
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
            'software_set',
            ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
            # 'name': {'validators': []},
        }


        
class ServerSerializer(serializers.HyperlinkedModelSerializer):
    # children = serializers.SerializerMethodField(read_only=True)
    # publisher = PublisherDetailSerializer()
    software = SoftwareSerializer(many=True)
    # publisher = PublisherSerializer(many=False)

    # def get_children(self, instance):
    #     #queryset = instance.get_children()
    #     queryset = Software.objects.filter(publisher__pk=instance.pk)
    #     print(f'\n\nThis is QUERYSET \n-------------------------------\n{queryset}\n-------------------------------\n\n')
    #     serializer = ServerSoftwareSerializer(queryset, context={"request": instance}, many=True)
    #     return serializer.data


    class Meta:

        model = Server
        fields = [
            # 'url',
            'id',
            'name',
            'status', 
            'software',
            # 'publisher',
            ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
            # 'name': {'validators': []},
            # 'slug': {'validators': []}
        }


# End Server ------------------------------------


# class CarSpecsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = CarSpecs
#         fields = ['id', 'car_plan', 'car_brand', 'car_model',
#                   'production_year', 'car_body', 'engine_type']
#         depth = 1
