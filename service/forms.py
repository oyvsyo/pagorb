from django import forms
from .models import Service, Enterprise  # ,Message
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = ['name', 'description']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description']


class MessageForm(forms.Form):
    name_at = {"type": "text", "class": "form-control",
               "placeholder": "Your Name *", "id": "name",
               "data-validation-required-message": "Please enter your name.",
               "aria-invalid": "false"}

    mail_at = {"type": "text", "class": "form-control",
               "placeholder": "Your Email *", "id": "email",
               "data-validation-required-message": "Please enter your email.",
               "aria-invalid": "false"}

    phone_at = {"type": "text", "class": "form-control",
                "placeholder": "Your Phone *", "id": "phone",
                "data-validation-required-message": "Please enter your phone.",
                "aria-invalid": "false"}

    text_at = {"type": "text", "class": "form-control",
               "placeholder": "Your Message Here *", "id": "message",
               "data-validation-required-message": "Please enter your message",
               "aria-invalid": "false"}

    name = forms.CharField(max_length=50, required=True,
                           widget=forms.TextInput(attrs=name_at))

    mail = forms.EmailField(required=True,
                            widget=forms.TextInput(attrs=mail_at))

    phone = forms.CharField(max_length=14, required=True,
                            widget=forms.TextInput(attrs=phone_at))

    text = forms.CharField(max_length=500,
                           widget=forms.Textarea(attrs=text_at))

    def send(self):
        subject = 'pagorb message'

        phone = self.cleaned_data['phone']
        text = self.cleaned_data['text']
        mail = self.cleaned_data['mail']
        name = self.cleaned_data['name']

        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]

        contact_message = """
        %s was send a message from site:
        -------------------------------
        %s
        -------------------------------
        there are contact info:
        Email: %s
        Phone: %s
        """ % (name, text, mail, phone)

        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)
