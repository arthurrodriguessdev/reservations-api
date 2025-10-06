from django.shortcuts import render
from rest_framework import generics
from appointments.serializers import AppointmentSerializer
from appointments.models import Appointment

class CreateListAppointment(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class UpdateDeleteDetailAppointment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
