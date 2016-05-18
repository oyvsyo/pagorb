from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<enterprise_id>[0-9]+)/$$', views.enterprise, name='enterprise'),
    url(r'^service/(?P<service_id>[0-9]+)/$$', views.service, name='service'),
]