from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return unicode(self.name)


class Enterprise(Service):

    def __unicode__(self):
        return unicode(self.name)


class Message(models.Model):
    mail = models.EmailField()
    text = models.CharField(max_length=500)
    phone = models.CharField(max_length=14)
    date_send = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return unicode(self.date_send)
