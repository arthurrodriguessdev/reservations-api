from django.shortcuts import render
from rest_framework import generics
from staff.serializers import StaffSerializer
from staff.models import Staff

class CreateListStaff(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class UpdateDeleteDetailStaff(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
