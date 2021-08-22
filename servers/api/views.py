from servers.models import Publisher, Software, Server#, CarPlan, CarSpecs
from .serializers import (
    PublisherCreateUpdateSerializer,
    PublisherDetailSerializer,
    PublisherListSerializer,
    SoftwareCreateUpdateSerializer,
    SoftwareCreateUpdateSerializerCustom,
    SoftwareDetailSerializer,
    SoftwareListSerializer,
    PublisherSerializer,
    SoftwareSerializer,
    ServerSerializer,
    ServerCreateUpdateSerializer,
    ServerDetailSerializer,
    ServerListSerializer,
    SoftwareDetailSerializerCustom,
    SoftwareListSerializerCustom,
    #CarSpecsSerializer
)
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def server_software_publisher_api_home(request, format=None):
    return Response(
        {
            "servers": reverse("server_list_api", request=request, format=format),
            "software": reverse("software_list_api", request=request, format=format),
            "publisher": reverse("publisher_list_api", request=request, format=format),
            "custom_software": reverse("custom_software_list_api", request=request, format=format),
        }
    )

# Begin API Views ------------------------------------

class PublisherCreateAPIView(CreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherCreateUpdateSerializer


class PublisherDetailAPIView(RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherDetailSerializer
    lookup_field = 'slug'


class PublisherListAPIView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherListSerializer
    lookup_field = 'slug'

# Custom ------------------------------------

class SoftwareCreateAPIViewCustom(APIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareCreateUpdateSerializerCustom

    # def get_queryset(self):
    #     software = Software.objects.all()
    #     return software

    # def get(self, request, *args, **kwargs):
        
    #     try:
    #         id = request.query_params["id"]
    #         if id != None:
    #             software = Software.objects.get(id=id)
    #             serializer = SoftwareCreateAPIViewCustom(software)
    #     except:
    #         software = self.get_queryset()
    #         serializer = SoftwareCreateAPIViewCustom(software, many=True)

    #     return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     software_data = request.data
    #     new_publisher = Publisher.objects.create(publisher=software_data["publisher"])
    #     new_publisher.save()

    #     new_software = Software.objects.create(name=software_data["name"], status=software_data[
    #         "status"], version=software_data["version"])

    #     new_software.save()

    #     serializer = SoftwareCreateAPIViewCustom(new_software)

    #     return Response(serializer.data)

class SoftwareDetailAPIViewCustom(RetrieveAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareDetailSerializerCustom
    lookup_field = 'slug'
    
class SoftwareListAPIViewCustom(ListAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareListSerializerCustom

# Custom ------------------------------------





class SoftwareCreateAPIView(CreateAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareCreateUpdateSerializer


class SoftwareDetailAPIView(RetrieveAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareDetailSerializer
    lookup_field = 'slug'


class SoftwareListAPIView(ListAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareListSerializer
    lookup_field = 'slug'


class ServerCreateAPIView(CreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerCreateUpdateSerializer


class ServerDetailAPIView(RetrieveAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerDetailSerializer
    lookup_field = 'slug'


class ServerListAPIView(ListAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerListSerializer
    lookup_field = 'slug'

# End API Views ------------------------------------

# Begin Viewsets ------------------------------------


class PublisherViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    PublisherViewSet
    """

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = 'slug'


class SoftwareViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    SoftwareViewSet
    """

    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    lookup_field = 'slug'


class ServerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    ServerViewSet
    """

    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    lookup_field = 'slug'


# class CarSpecsViewset(viewsets.ModelViewSet):
#     serializer_class = CarSpecsSerializer
#     # throttle_scope = "first_app"
    
#     def get_queryset(self):
#         car_specs = CarSpecs.objects.all()
#         return car_specs

    # def retrieve(self, request, *args, **kwargs):
    #     params = kwargs
    #     print(params['pk'])
    #     params_list = params['pk'].split('-')
    #     cars = CarSpecs.objects.filter(
    #         car_brand=params_list[0], car_model=params_list[1])
    #     serializer = CarSpecsSerializer(cars, many=True)
    #     return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        car_data = request.data

        new_car = CarSpecs.objects.create(car_plan=CarPlan.objects.get(plan_name=car_data["car_plan"]), car_brand=car_data["car_brand"], car_model=car_data[
            "car_model"], production_year=car_data["production_year"], car_body=car_data["car_body"], engine_type=car_data["engine_type"])

        new_car.save()
 
        serializer = CarSpecsSerializer(new_car)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            car = self.get_object()
            car.delete()
            response_message = {"message": "Item has been deleted"}
        else:
            response_message = {"message": "Not Allowed"}

        return Response(response_message)

    def update(self, request, *args, **kwargs):
        car_object = self.get_object()
        data = request.data

        car_plan = CarPlan.objects.get(plan_name=data["plan_name"])

        car_object.car_plan = car_plan
        car_object.car_brand = data["car_brand"]
        car_object.car_model = data["car_model"]
        car_object.production_year = data["production_year"]
        car_object.car_body = data["car_body"]
        car_object.engine_type = data["engine_type"]

        car_object.save()

        serializer = CarSpecsSerializer(car_object)

        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        car_object = self.get_object()
        data = request.data

        try:
            car_plan = CarPlan.objects.get(plan_name=data["plan_name"])
            car_object.car_plan = car_plan
        except KeyError:
            pass

        car_object.car_brand = data.get("car_brand", car_object.car_brand)
        car_object.car_model = data.get("car_model", car_object.car_model)
        car_object.production_year = data.get("production_year", car_object.production_year)
        car_object.car_body = data.get("car_body", car_object.car_body)
        car_object.engine_type = data.get("engine_type", car_object.engine_type)

        car_object.save()

        serializer = CarSpecsSerializer(car_object)

        return Response(serializer.data)
# End ViewSets ------------------------------------
