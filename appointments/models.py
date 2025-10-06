from django.db import models
from clients.models import Client
from services.models import Service
from staff.models import Staff

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='appointment', blank=False, null=False)
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='appointment', blank=False, null=False)
    staff = models.ManyToManyField(Staff, related_name='appointment')
    datetime = models.DateTimeField()

    def __str__(self):
        return f'{self.service} - {self.datetime}'

