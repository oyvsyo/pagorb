from django.shortcuts import render
from django.http import HttpResponse
from .models import Service


def index(request):
    latest_service_list = Service.objects.all()
    context = {'latest_service_list': latest_service_list}
    return render(request, 'service/index.html', context)


def detail(request, service_id):
    return HttpResponse("You're looking at question %s." % service_id)
