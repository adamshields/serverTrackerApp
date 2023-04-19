from django.db import models
from polymorphic.models import PolymorphicModel

class Resource(PolymorphicModel):
    active_record = models.IntegerField(verbose_name="Active Record")

    class Meta:
        verbose_name = "Resource"
        verbose_name_plural = "Resources"

class ServerResource(Resource):
    cpu = models.IntegerField(verbose_name="CPU Cores")
    memory = models.IntegerField(verbose_name="Memory (GB)")
    domain = models.CharField(max_length=255, verbose_name="Domain")

    class Meta:
        verbose_name = "Server Resource"
        verbose_name_plural = "Server Resources"

class SANResource(Resource):
    storage_capacity = models.IntegerField(verbose_name="Storage Capacity (GB)")
    redundancy_level = models.IntegerField(verbose_name="Redundancy Level")

    class Meta:
        verbose_name = "SAN Resource"
        verbose_name_plural = "SAN Resources"

class GTMResource(Resource):
    load_balancing_method = models.CharField(max_length=255, verbose_name="Load Balancing Method")
    dns_zone = models.CharField(max_length=255, verbose_name="DNS Zone")

    class Meta:
        verbose_name = "GTM Resource"
        verbose_name_plural = "GTM Resources"

class LTMResource(Resource):
    virtual_servers = models.IntegerField(verbose_name="Number of Virtual Servers")
    pool_size = models.IntegerField(verbose_name="Pool Size")

    class Meta:
        verbose_name = "LTM Resource"
        verbose_name_plural = "LTM Resources"
