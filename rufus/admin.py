from django.contrib import admin

# Register your models here.
from .models import ContactInfo, BookExample

admin.site.register(ContactInfo)

# class BookExampleAdmin(admin.ModelAdmin):
#     list_display = ('name',)


# admin.site.register(BookExample, BookExampleAdmin)

class BookExampleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['detail_text']}),
        (None, {'fields': ['detail_json']}),
        ('JSON', {'fields': ['detail_json_formatted']}),
    ]
    list_display = ('name',)
    readonly_fields = ('detail_json_formatted',)
    # readonly_fields = ['detail_json_formatted']


admin.site.register(BookExample, BookExampleAdmin)