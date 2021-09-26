from rest_framework import serializers, request
from rest_framework.reverse import reverse
from restify.models import Server, Software, Publisher
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin

from django.utils.text import slugify


# # """
# # Test Code
# # from servers.api.serializers import PublisherCreateUpdateSerializer
# # serializer = PublisherCreateUpdateSerializer()
# # print(repr(serializer))
# # """




# # Begin Publisher ------------------------------------

# class PublisherCreateUpdateSerializer(serializers.ModelSerializer):
#     """
#     Test Code
#     from servers.api.serializers import PublisherCreateUpdateSerializer
#     serializer = PublisherCreateUpdateSerializer()
#     print(repr(serializer))
#     """

#     class Meta:

#         model = Publisher
#         fields = [
#             'id',
#             'publisher_name',
#             'publisher_status', 
#             ]
#         # lookup_field = 'slug'
#         # extra_kwargs = {
#         #     'url': {'lookup_field': 'slug'},
#         #     # 'name': {'validators': []},
#         #     # 'slug': {'validators': []}
#         # }


# class PublisherDetailSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField("publisher_detail_api", lookup_field='slug')
#     """
#     Test Code
#     from servers.api.serializers import PublisherDetailSerializer
#     serializer = PublisherDetailSerializer()
#     print(repr(serializer))
#     """

#     class Meta:

#         model = Publisher
#         fields = [
#             'url',
#             'id',
#             'publisher_name',
#             'publisher_status',
#             'publisher_software_set', # Reversed
#             ]
#         lookup_field = 'publisher_slug'
#         # extra_kwargs = {
#         #     'url': {'lookup_field': 'slug'},
#         #     # 'name': {'validators': []},
#         #     # 'slug': {'validators': []}
#         # }
#         depth = 1


# class PublisherListSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField("publisher_detail_api", lookup_field='publisher_slug')
#     """
#     Test Code
#     from servers.api.serializers import PublisherListSerializer
#     serializer = PublisherListSerializer()
#     print(repr(serializer))
#     """

#     class Meta:

#         model = Publisher
#         fields = [
#             'url',
#             'id',
#             'publisher_name',
#             'publisher_status', 
#             'publisher_software_set', # Reversed
#             ]
#         # lookup_field = 'slug'
#         # extra_kwargs = {
#         #     'url': {'lookup_field': 'slug'},
#         #     # 'name': {'validators': []},
#         #     # 'slug': {'validators': []}
#         # }
#         depth = 1

# # End Publisher ------------------------------------

# # Begin Software ------------------------------------

# class SoftwareCreateUpdateCustomSerializer(serializers.Serializer):
#     """
#     Test Code
#     from servers.api.serializers import SoftwareCreateUpdateCustomSerializer
#     serializer = SoftwareCreateUpdateCustomSerializer()
#     print(repr(serializer))
#     """

#     class Meta:

#         model = Software
#         fields = [
#             'software_name',
#             'software_status',
#             'software_version',
#             'software_publisher',
#             ]
#         # lookup_field = 'slug'
#         # extra_kwargs = {
#         #     'url': {'lookup_field': 'slug'},
#         #     # 'name': {'validators': []},
#         #     # 'slug': {'validators': []}
#         # }







# class SoftwareCreateUpdateSerializer(serializers.ModelSerializer):
#     """
#     Test Code
#     from servers.api.serializers import SoftwareCreateUpdateSerializer
#     serializer = SoftwareCreateUpdateSerializer()
#     print(repr(serializer))
#     """
#     class Meta:

#         model = Software
#         fields = [
#             'software_name',
#             'software_status',
#             'software_version',
#             'software_publisher',
#             ]
#         # lookup_field = 'slug'
#         # extra_kwargs = {
#         #     'url': {'lookup_field': 'slug'},
#         #     # 'name': {'validators': []},
#         #     # 'slug': {'validators': []}
#         # }



# class SoftwareDetailSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField("software_detail_api", lookup_field='software_slug')
#     """
#     Test Code
#     from servers.api.serializers import SoftwareDetailSerializer
#     serializer = SoftwareDetailSerializer()
#     print(repr(serializer))
#     """
#     class Meta:

#         model = Software
#         fields = [
#             'url',
#             'id',
#             'software_name',
#             'software_slug',
#             'software_status',
#             'software_version',
#             ]
#         lookup_field = 'software_slug'
#         # extra_kwargs = {
#         #     'url': {'lookup_field': 'slug'},
#         #     # 'name': {'validators': []},
#         #     # 'slug': {'validators': []}
#         # }


# class SoftwareListSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField("software_detail_api", lookup_field='software_slug')
#     """
#     Test Code
#     from servers.api.serializers import SoftwareListSerializer
#     serializer = SoftwareListSerializer()
#     print(repr(serializer))
#     """
#     class Meta:

#         model = Software
#         fields = [
#             'url',
#             'id',
#             'software_slug',
#             'software_name',
#             'software_status',
#             'software_version',
#             ]
#         # lookup_field = 'slug'
#         # extra_kwargs = {
#         #     'url': {'lookup_field': 'slug'},
#         #     # 'name': {'validators': []},
#         #     # 'slug': {'validators': []}
#         # }
# # End Software ------------------------------------


# # Begin Server ------------------------------------

# # WritableNestedModelSerializer
# class ServerCreateUpdateSerializer(serializers.ModelSerializer):
#     """
#     Test Code
#     from servers.api.serializers import ServerCreateUpdateSerializer
#     serializer = ServerCreateUpdateSerializer()
#     print(repr(serializer))
#     """

#     class Meta:

#         model = Server
#         fields = [
#             'id',
#             'server_name',
#             'server_status', 
#             'server_software', 
#             ]
#         # lookup_field = 'slug'
#         # extra_kwargs = {
#         #     'url': {'lookup_field': 'slug'},
#         #     # 'name': {'validators': []},
#         #     # 'slug': {'validators': []}
#         # }


# class ServerDetailSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField("server_detail_api", lookup_field='server_slug')
#     """
#     Test Code
#     from servers.api.serializers import ServerDetailSerializer
#     serializer = ServerDetailSerializer()
#     print(repr(serializer))
#     """
#     class Meta:

#         model = Server
#         fields = [
#             'url',
#             'id',
#             'server_name',
#             'server_status', 
#             'server_software', 
#             ]
#         lookup_field = 'server_slug'
#         # extra_kwargs = {
#         #     'url': {'lookup_field': 'slug'},
#         #     # 'name': {'validators': []},
#         #     # 'slug': {'validators': []}
#         # }
#         depth = 1

# class ServerListSerializer(serializers.ModelSerializer):
#     # url = serializers.HyperlinkedIdentityField("server_detail_api", lookup_field='server_slug')
#     """
#     Test Code
#     from servers.api.serializers import ServerListSerializer
#     serializer = ServerListSerializer()
#     print(repr(serializer))
#     """
#     class Meta:

#         model = Server
#         fields = [
#             # 'url',
#             'id',
#             'server_name',
#             'server_status', 
#             'server_software', 
#             ]
#         lookup_field = 'server_slug'
#         # extra_kwargs = {
#         #     'url': {'lookup_field': 'slug'},
#         #     # 'name': {'validators': []},
#         #     # 'slug': {'validators': []}
#         # }
#         depth = 2


# Viewsets ------------------------------------        
# # # https://stackoverflow.com/questions/64048863/how-to-display-field-value-instead-of-id-for-foreign-key-in-django-rest-framewor


class PublisherSerializer(serializers.ModelSerializer):
    """
    Test Code
    from servers.api.serializers import PublisherSerializer
    serializer = PublisherSerializer()
    print(repr(serializer))
    """
    class Meta:
        model = Publisher
        fields = [
            # 'url',
            'id',
            'publisher_name',
            'publisher_status',
            # 'software_set',
            ]
        lookup_field = 'publisher_slug'
        extra_kwargs = {
            'url': {'lookup_field': 'publisher_slug'},
            'publisher_name': {'validators': []},
        }
        # depth = 1


# class SoftwarePublisherSerializer(serializers.HyperlinkedModelSerializer):
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
#             'publisher_name',
#             'publisher_status',
#             ]
#         lookup_field = 'publisher_slug'
#         extra_kwargs = {
#             'url': {'lookup_field': 'publisher_slug'},
#             'publisher_name': {'validators': []},
#         }

# class CustomPublisherSerializer(serializers.ModelSerializer):
#     """
#     Test Code
#     from servers.api.serializers import PublisherSerializer
#     serializer = PublisherSerializer()
#     print(repr(serializer))
#     """
#     class Meta:
#         model = Publisher
#         fields = [
#             'publisher_name',
#             ]

        # depth = 1
# # # https://stackoverflow.com/questions/55161052/instead-of-primary-key-send-different-field-in-django-rest-framework
# class GenreRelatedField(serializers.RelatedField):
#     def display_value(self, instance):
#         return instance

#     def to_representation(self, value):
#         return str(value)

#     def to_internal_value(self, data):
#         return Genre.objects.get(name=data)


# class MovieSerializer(serializers.ModelSerializer):
#     genre = GenreRelatedField(
#         queryset=Genre.objects.all(),
#         many=True
#     )

#     class Meta:
#         model = Movie
#         fields = (
#             'popularity',  
#             'director',     
#             'genre',                         
#             'imdb_score',
#             'name',
#         )   
class PublisherRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Publisher.objects.get(publisher_name=data)
        
class SoftwareSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
# class SoftwareSerializer(serializers.ModelSerializer):
    software_publisher = PublisherRelatedField(queryset=Publisher.objects.all(), many=False)
    class Meta:
        model = Software
        fields = [
            'software_publisher',
            'software_name',
            'software_slug',
            'software_status',
            'software_version',

            ]
        lookup_field = 'software_slug'
        extra_kwargs = {
            'software_name': {'validators': []},
            'software_slug': {'validators': []},
            'software_publisher': {'validators': []},
        }
    # def create(self, validated_data):
    #     genre = validated_data.pop('genre',[])
    #     movie = super().create(validated_data)
    #     genre_qs = Genre.objects.filter(name__in=genre)
    #     movie.genre.add(*genre_qs)
    #     return movie

    # def create(self, validated_data):
    #     print(f'\nVALIDATED_DATA | {validated_data}')
    #     software_publisher = validated_data.pop('software_publisher')
    #     print(f'\nSOFTWARE_PUBLISHER | {software_publisher}')
    #     publisher, created = Publisher.objects.update_or_create(
    #         publisher_name = software_publisher
    #     )
    #     if created == False:
    #         print(f'Updated {publisher.name} name')
    #     else:
    #         print(f'Created {publisher.name} name')

    #     # software = super().create(validated_data)
    #     # publisher_qs = Publisher.objects.filter(software_name__in=software_publisher)
    #     # software.software_publisher.add(*publisher_qs)
    #     return software

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['software_publisher'] = instance.software_publisher.publisher_name
    #     return rep

    # def create(self, validated_data):
    #     print(f'\n\nValidated Data \n\n-----------------------------\n{validated_data}\n-----------------------------')
    #     software_publisher = validated_data.pop('software_publisher')
    #     # x = Publisher.objects.filter(publisher_name=publisher_name).values_list('id', flat=True)
    #     a = Publisher.objects.filter(publisher_name=software_publisher).values_list('id', flat=True).exists()
    #     x = Publisher.objects.only('id').get(publisher_name=software_publisher).id
    #     if a is False:
    #         Publisher.objects.create(publisher_name=software_publisher)
    #         print(x)
    #         print(a)
    #     else:
    #         # publisher = Publisher.objects.update(
    #         #     publisher_name = software_publisher)
    #         print(x)
    #         print(a)
    #     # publisher, created = Publisher.objects.update_or_create(
    #     #     publisher_name = publisher_name,
    #     # )

    #     # print(f'\n\nSoftware_data Data \n\n-----------------------------\n{publisher_id}\n-----------------------------')
    #     # publisher_data = software_data['publisher']
    #     # print(f'\n\npublisher_data Data \n\n-----------------------------\n{publisher_data}\n-----------------------------')
    #     software, created = Software.objects.update_or_create(
    #         software_name = validated_data.get('software_name', None),
    #         defaults={
    #             'software_status': validated_data.get('software_status', None),
    #             'software_publisher': validated_data.pop('software_publisher', None),
    #         })
    #     return software           

    # def create(self, validated_data):
    #     print(f'\n\nValidated Data \n\n-----------------------------\n{validated_data}\n-----------------------------')
    #     software_data = validated_data.pop('software')
    #     print(f'\n\nsoftware_data Data \n\n-----------------------------\n{software_data}\n-----------------------------')

    #     publisher_data = validated_data.pop('publisher')
    #     print(f'\n\npublisher_data Data \n\n-----------------------------\n{publisher_data}\n-----------------------------')
    #     publisher, created = Publisher.objects.update_or_create(
    #         name = validated_data.get('name', None),
    #         defaults={
    #             'name': validated_data.get('name', None),
    #             'status': validated_data.get('status', None),
    #         })
        

# class ServerSerializer(serializers.HyperlinkedModelSerializer):
class ServerSerializer(WritableNestedModelSerializer, serializers.HyperlinkedModelSerializer):
# class ServerSerializer(serializers.HyperlinkedModelSerializer):
    server_software = SoftwareSerializer(many=True)
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
            'server_name',
            'server_status', 
            'server_software', 
            ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'server_slug'},
            'server_name': {'validators': []},
            'server_slug': {'validators': []},
        }


    # def create(self, validated_data):
    #     print(f'\n\nValidated Data \n\n-----------------------------\n{validated_data}\n-----------------------------')
    #     # publisher_data = software_data['publisher']
    #     # print(f'\n\npublisher_data Data \n\n-----------------------------\n{publisher_data}\n-----------------------------')
    #     server, created = Server.objects.update_or_create(
    #         server_name = validated_data.get('server_name', None),
    #         defaults={
    #             'server_status': validated_data.get('server_status', None),
    #         })
            
    #     software_data = validated_data.pop('server_software')
    #     # print(f'\n\nsoftware_data Data \n\n{software_data}\n')
    #     for publisher in software_data:
    #         print(f'\nPUBLISHER DATA -----> {publisher}')
    #         software_publisher = publisher['software_publisher']
    #         print(f'\nPublisher Name -----> {software_publisher}')
    #         publisher, created = Publisher.objects.update_or_create(
    #             publisher_name = publisher['software_publisher']
    #         )

    #         # try:
    #         #     publisher = Publisher.objects.get(publisher_name = publisher['software_publisher'])
    #         #     publisher

    #         # except Publisher.DoesNotExist:
    #         #     publisher = Publisher.objects.create(publisher_name = publisher['software_publisher'])

    #         # Publisher.objects.get(publisher_name = publisher['software_publisher'])
    #         # publisher = Publisher.objects.get(publisher_name = publisher['software_publisher'])
    #         # print(f'\nPublisher Object ID -----> {pub.id}')
    #         # print(f'\nPublisher Object Name -----> {pub.publisher_name}')


    #     for software in software_data:
    #         print(f'\nSoftware Data -----> {software}')
    #         software_name = software['software_name']
    #         print(f'\nSoftware Name -----> {software_name}')
    #         software, created = Software.objects.update_or_create(
    #             software_name = software['software_name'],
    #             defaults={
    #                 'software_version': software['software_version'],
    #                 'software_status': software['software_status'],
    #                 'software_publisher': Publisher.objects.get(publisher_name=software['software_publisher'])
    #                 # 'software_publisher': Publisher.objects.get(publisher_name=publisher_name)
    #             })
    #         server.server_software.add(software)
    #     # if created == False:
    #     #     print(f'Updated {software.name} name')
    #     # else:
    #     #     print(f'Created {software.name} name')
    #     return server
# # End Software ------------------------------------

# {'server_name': 'Server-002', 'server_status': True, 
# 'server_software': 
# [OrderedDict([('software_publisher', <Publisher: Python Software Foundation>), ('software_name', 'Python 3a.6.12'), ('software_status', True), ('software_version', '3.6.6')]), 
# OrderedDict([('software_publisher', <Publisher: Microsoft>), ('software_name', 'IIS Cors Maodule 1.2.3'), ('software_status', True), ('software_version', '1.2.3')])]}








#     def create(self, validated_data):
#         print(f'\n\nValidated Data \n\n-----------------------------\n{validated_data}\n-----------------------------')
#         software_data = validated_data.pop('server_software')
#         print(f'\n\nsoftware_data Data \n\n-----------------------------\n{software_data}\n-----------------------------')
#         # publisher_data = software_data['publisher']
#         # print(f'\n\npublisher_data Data \n\n-----------------------------\n{publisher_data}\n-----------------------------')
#         server, created = Server.objects.update_or_create(
#             server_name = validated_data.get('server_name', None),
#             defaults={
#                 'server_status': validated_data.get('server_status', None),
#             })
            
#         for publisher in software_data:
#             print(f'\nPUBLISHER DATA -----> {publisher}')
#             publisher_name = publisher['software_publisher'],
#             print(f'\nPublisher Name -----> {publisher_name}')
#             # Publisher.objects.get(publisher_name = publisher['software_publisher'])
#             # publisher = Publisher.objects.get(publisher_name = publisher['software_publisher'])
#             # print(f'\nPublisher Object ID -----> {pub.id}')
#             # print(f'\nPublisher Object Name -----> {pub.publisher_name}')
#             publisher, created = Publisher.objects.update_or_create(
#                 publisher_name = publisher['software_publisher'],
#             )


#         for software in software_data:
#             print(f'\nSoftware Data -----> {software}')
#             software_name = software['software_name']
#             print(f'\nSoftware Name -----> {software_name}')
#             software, created = Software.objects.update_or_create(
#                 software_name = software['software_name'],
#                 defaults={
#                     'software_version': software['software_version'],
#                     'software_status': software['software_status'],
#                 })
#             server.server_software.add(software)
#         # if created == False:
#         #     print(f'Updated {software.name} name')
#         # else:
#         #     print(f'Created {software.name} name')
#         return server
# # # End Software ------------------------------------

# # {'server_name': 'Server-002', 'server_status': True, 
# # 'server_software': 
# # [OrderedDict([('software_publisher', <Publisher: Python Software Foundation>), ('software_name', 'Python 3a.6.12'), ('software_status', True), ('software_version', '3.6.6')]), 
# # OrderedDict([('software_publisher', <Publisher: Microsoft>), ('software_name', 'IIS Cors Maodule 1.2.3'), ('software_status', True), ('software_version', '1.2.3')])]}