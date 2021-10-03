from django.contrib import admin
from .models import Server, Publisher, Software, Project, Environment, Ait

# admin.site.register(Project)
# admin.site.register(Environment)
# admin.site.register(Ait)


class PublisherTabularInline(admin.TabularInline):
    model = Publisher
class SoftwareTabularInline(admin.StackedInline):
    model = Software
    readonly_fields = ['software_slug']

class AitAdmin(admin.ModelAdmin):
    def projects(self, obj):
        return ', '.join([project.project_name for project in obj.project_set.all()])

    list_display = [
        'id',
        'ait_number',
        'projects',
				]
    list_display_links = [
        'id',
        'ait_number',
        ]
    exclude = ['ait_slug']

    class Meta:
        model = Ait

admin.site.register(Ait, AitAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'project_name',
        'project_ait',
				]
    list_display_links = [
        'id',
        'project_name',
        'project_ait',
        ]
    readonly_fields = ['project_slug']

    class Meta:
        model = Project

admin.site.register(Project, ProjectAdmin)

class EnvironmentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'environment_name',
        'environment_project',
				]
    list_display_links = [
        'id',
        'environment_name',
        'environment_project',
        ]
    readonly_fields = ['environment_slug']

    class Meta:
        model = Environment

admin.site.register(Environment, EnvironmentAdmin)

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
    list_display = [
        'id',
        'server_name',
        'server_ait',
        'server_project',
        'server_environment',
				]
    list_display_links = [
        'id',
        'server_name',
        'server_ait',
        'server_project',
        'server_environment',
        ]
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