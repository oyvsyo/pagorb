from django.db import models


class Enterprise(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def services(self):
        return self.service_set.all()

    def __unicode__(self):
        return unicode(self.name)


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    enterprise = models.ForeignKey(Enterprise, default=0)

    def __unicode__(self):
        return unicode(self.name)
