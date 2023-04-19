from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import (
    WebServer,
    DatabaseServer,
    HighPerformanceSAN,
    HighCapacitySAN,
    GeoDNS,
    LoadBalancer,
)

class VersionedModelAdmin(VersionAdmin, admin.ModelAdmin):
    pass

@admin.register(WebServer)
class WebServerAdmin(VersionedModelAdmin):
    list_display = ('id', 'active_record', 'cpu', 'memory', 'domain')

@admin.register(DatabaseServer)
class DatabaseServerAdmin(VersionedModelAdmin):
    list_display = ('id', 'active_record', 'cpu', 'memory', 'database_type')

@admin.register(HighPerformanceSAN)
class HighPerformanceSANAdmin(VersionedModelAdmin):
    list_display = ('id', 'active_record', 'storage_capacity', 'iops')

@admin.register(HighCapacitySAN)
class HighCapacitySANAdmin(VersionedModelAdmin):
    list_display = ('id', 'active_record', 'storage_capacity', 'redundancy_level')

@admin.register(GeoDNS)
class GeoDNSAdmin(VersionedModelAdmin):
    list_display = ('id', 'active_record', 'load_balancing_method', 'dns_zone')

@admin.register(LoadBalancer)
class LoadBalancerAdmin(VersionedModelAdmin):
    list_display = ('id', 'active_record', 'virtual_servers', 'pool_size')
