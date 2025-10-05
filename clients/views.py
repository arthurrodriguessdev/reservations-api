from django.shortcuts import render
from rest_framework import generics
from clients.models import Client
from clients.serializers import ClientSerializer

class CreateListClients(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class UpdateDeleteDetailClients(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
