from django.contrib import admin
from .models import Service, Enterprise, Message


my_models = [Service, Enterprise, Message]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    form = Service


class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    form = Enterprise


class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'mail', 'phone')
    form = Message

admin.site.register(my_models)

