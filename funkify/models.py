from django.db import models

class Resource(models.Model):
    active_record = models.IntegerField(verbose_name="Active Record")

    class Meta:
        abstract = True

class ServerResource(Resource):
    cpu = models.IntegerField(verbose_name="CPU Cores")
    memory = models.IntegerField(verbose_name="Memory (GB)")

    class Meta:
        abstract = True

class SANResource(Resource):
    storage_capacity = models.IntegerField(verbose_name="Storage Capacity (GB)")

    class Meta:
        abstract = True

class GTMResource(Resource):
    load_balancing_method = models.CharField(max_length=255, verbose_name="Load Balancing Method")

    class Meta:
        abstract = True

class LTMResource(Resource):
    virtual_servers = models.IntegerField(verbose_name="Number of Virtual Servers")

    class Meta:
        abstract = True

# Specific server resources
class WebServer(ServerResource):
    domain = models.CharField(max_length=255, verbose_name="Domain")

    class Meta:
        verbose_name = "Web Server"
        verbose_name_plural = "Web Servers"

class DatabaseServer(ServerResource):
    database_type = models.CharField(max_length=255, verbose_name="Database Type")

    class Meta:
        verbose_name = "Database Server"
        verbose_name_plural = "Database Servers"

# Specific SAN resources
class HighPerformanceSAN(SANResource):
    iops = models.IntegerField(verbose_name="IOPS")

    class Meta:
        verbose_name = "High Performance SAN"
        verbose_name_plural = "High Performance SANs"

class HighCapacitySAN(SANResource):
    redundancy_level = models.IntegerField(verbose_name="Redundancy Level")

    class Meta:
        verbose_name = "High Capacity SAN"
        verbose_name_plural = "High Capacity SANs"

# Specific GTM resources
class GeoDNS(GTMResource):
    dns_zone = models.CharField(max_length=255, verbose_name="DNS Zone")

    class Meta:
        verbose_name = "GeoDNS"
        verbose_name_plural = "GeoDNS"

# Specific LTM resources
class LoadBalancer(LTMResource):
    pool_size = models.IntegerField(verbose_name="Pool Size")

    class Meta:
        verbose_name = "Load Balancer"
        verbose_name_plural = "Load Balancers"
