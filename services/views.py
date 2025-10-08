from django.shortcuts import render
from rest_framework import generics
from services.serializers import ServiceModelSerializer
from services.models import Service

class CreateListServices(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceModelSerializer

class UpdateDeleteDetailServices(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceModelSerializer
