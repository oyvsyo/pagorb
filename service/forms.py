from django import forms
from .models import Service, Message, Enterprise


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ['name', 'description']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['mail', 'text', 'phone', ]
