from django import forms
from .models import Service, Enterprise # ,Message


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ['name', 'description']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description']


class MessageForm(forms.Form):
    mail = forms.EmailField()
    text = forms.CharField(max_length=500)
    phone = forms.CharField(max_length=14)
    # date_send = forms.DateTimeField(auto_now=False, auto_now_add=True)

    # class Meta:
    #     model = Message
    #     fields = ['mail', 'text', 'phone', ]
