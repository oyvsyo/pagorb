from django.contrib import admin
from .models import Service, Enterprise  #, Message


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['enterprise__name']
    # form = Service


class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    # form = Enterprise


# class MessageAdmin(admin.ModelAdmin):
#     list_display = ('text', 'mail', 'phone')
#     form = Message


my_models = [ServiceAdmin, EnterpriseAdmin]

admin.site.register(Service, ServiceAdmin)
admin.site.register(Enterprise, EnterpriseAdmin)
