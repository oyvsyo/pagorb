from django.contrib import admin
from .models import Service, Enterprise


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['enterprise__name']


class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

my_models = [ServiceAdmin, EnterpriseAdmin]

admin.site.register(Service, ServiceAdmin)
admin.site.register(Enterprise, EnterpriseAdmin)
