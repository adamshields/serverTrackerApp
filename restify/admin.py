from django.contrib import admin
from .models import Server, Publisher, Software

# admin.site.register(Server)
# admin.site.register(Software)
# admin.site.register(Version)


class PublisherTabularInline(admin.TabularInline):
    model = Publisher
class SoftwareTabularInline(admin.StackedInline):
    model = Software
    readonly_fields = ['software_slug']


class SoftwareAdmin(admin.ModelAdmin):
    # list_display = [
    #     "id",
    #     "name",
    #     "ip_address",	
    #     "fqdn",	
    #     "status",	
	# 			]
    # list_display_links = [
    #     'id', 
    #     'name'
    #     ]
    readonly_fields = ['software_slug']

    class Meta:
        model = Software

admin.site.register(Software, SoftwareAdmin)

class ServerAdmin(admin.ModelAdmin):
    # list_display = [
    #     "id",
    #     "name",
    #     "ip_address",	
    #     "fqdn",	
    #     "status",	
	# 			]
    # list_display_links = [
    #     'id', 
    #     'name'
    #     ]
    readonly_fields = ['server_slug']

    class Meta:
        model = Server

admin.site.register(Server, ServerAdmin)


class PublisherAdminAdmin(admin.ModelAdmin):
    inlines = [SoftwareTabularInline]
    # list_display = [
    #     "id",
    #     "name",
    #     "version",	
    #     "status",	
	# 			]
    # list_display_links = [
    #     'id', 
    #     'name'
    #     ]
    readonly_fields = ['publisher_slug']

    class Meta:
        model = Publisher

admin.site.register(Publisher, PublisherAdminAdmin)