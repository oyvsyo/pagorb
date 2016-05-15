from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    fields = ['service_name', 'service_description']
    list_display = ('service_name', 'service_description')

admin.site.register(Service, ServiceAdmin)

