from django.shortcuts import render
from django.http import HttpResponse
from .models import Service


def index(request):
    latest_service_list = Service.objects.all()
    context = {'latest_service_list': latest_service_list}
    return render(request, 'index.html', context)


def detail(request, service_id):
    context = {

    }
    return render(request, 'service/service.html', context)
