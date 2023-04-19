from django.contrib import admin

# Register your models here.
from .models import Approval, Design

admin.site.register(Approval)
admin.site.register(Design)