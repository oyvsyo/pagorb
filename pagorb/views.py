from django.shortcuts import render
from django.http import HttpResponse
from service.models import Enterprise
from service.forms import MessageForm


def home(request):
    enterprise_list = Enterprise.objects.all()
    context = {'enterprise_list': enterprise_list}
    return render(request, 'index.html', context)


def message(request):
    form = MessageForm(request.POST or None)
    context = {
        'form': form
    }

    return render(request, 'forms.html', context)
