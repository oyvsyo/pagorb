from django.shortcuts import render
from django.http import HttpResponse
from service.models import Enterprise


def home(request):
    enterprise_list = Enterprise.objects.all()
    context = {'enterprise_list': enterprise_list}
    return render(request, 'index.html', context)
