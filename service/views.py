from django.shortcuts import render
# from django.http import HttpResponse
from .models import Service, Enterprise


def enterprise(request, enterprise_id):
    enterprise_item = Enterprise.objects.get(id=enterprise_id)
    name = enterprise_item.name
    services = enterprise_item.service_set.all()
    description = enterprise_item.description
    context = {
        'name': name,
        'services': services,
        'description': description
    }
    return render(request, 'service/enterprise.html', context)


def service(request, service_id):
    service_item = Service.objects.get(id=service_id)
    name = service_item.name
    description = service_item.description
    enterprise_name = service_item.enterprise.name
    enterprise_id = service_item.enterprise.id
    context = {
        'name': name,
        'description': description,
        'enterprise': enterprise_name,
        'id': enterprise_id
    }
    return render(request, 'service/service.html', context)
