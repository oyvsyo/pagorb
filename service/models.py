from django.db import models


class Service(models.Model):
    service_name = models.CharField(max_length=200)
    service_description = models.CharField(max_length=500)

    def __str__(self):
        return self.service_name
