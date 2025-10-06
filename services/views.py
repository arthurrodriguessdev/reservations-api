from django.shortcuts import render
from rest_framework import generics
from services.serializers import ServiceSerializer
from services.models import Service

class CreateListServices(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class UpdateDeleteDetailServices(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
