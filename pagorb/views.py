from django.shortcuts import render, redirect
from django.http import HttpResponse
from service.models import Enterprise
from service.forms import MessageForm


def home(request):
    enterprise_list = Enterprise.objects.all()
    form = MessageForm(request.GET)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.send()
            return redirect('home')

    context = {
        'enterprise_list': enterprise_list,
        'form': form,
               }
    return render(request, 'home.html', context)
