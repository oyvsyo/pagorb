from django.shortcuts import render
from django.http import HttpResponse
from service.models import Enterprise
from service.forms import MessageForm


def home(request):
    enterprise_list = Enterprise.objects.all()
    parity = [i % 2 for i in range(len(enterprise_list))]
    context = {
        'enterprise_list': enterprise_list,
        'parity': parity
               }
    return render(request, 'home.html', context)


def message(request):
    form = MessageForm(request.POST or None)
    context = {
        'form': form
    }

    return render(request, 'forms.html', context)
