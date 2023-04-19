from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from reversion.admin import VersionAdmin
from .models import Resource, ServerResource, SANResource, GTMResource, LTMResource


class ResourceChildAdmin(PolymorphicChildModelAdmin, VersionAdmin):
    base_model = Resource
    show_in_index = True


class ServerResourceAdmin(ResourceChildAdmin):
    pass


class SANResourceAdmin(ResourceChildAdmin):
    pass


class GTMResourceAdmin(ResourceChildAdmin):
    pass


class LTMResourceAdmin(ResourceChildAdmin):
    pass


class ResourceAdmin(PolymorphicParentModelAdmin, VersionAdmin):
    base_model = Resource
    child_models = (ServerResource, SANResource, GTMResource, LTMResource)
    list_display = ('id', 'polymorphic_ctype', 'active_record')
    list_filter = ('polymorphic_ctype', 'active_record')


admin.site.register(Resource, ResourceAdmin)
admin.site.register(ServerResource, ServerResourceAdmin)
admin.site.register(SANResource, SANResourceAdmin)
admin.site.register(GTMResource, GTMResourceAdmin)
admin.site.register(LTMResource, LTMResourceAdmin)
