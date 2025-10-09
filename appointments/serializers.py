from rest_framework import serializers
from django.shortcuts import get_object_or_404
from datetime import date, timedelta, datetime
from django.utils import timezone
from appointments.models import Appointment
from clients.models import Client

class AppointmentSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Appointment
        fields = ('id', 'datetime', 'date', 'client', 'service', 'staff')

    def validate_datetime(self, value):
        if value and value < timezone.now():
            raise serializers.ValidationError('Data de agendamento inválida')
        if value:
            get_client = self.initial_data.get('client')
            get_staff = self.initial_data.get('staff')

            client_name = get_object_or_404(Client, pk=get_client)

            if get_staff:
                appointments_staff = Appointment.objects.filter(staff__in=get_staff)

                if self.instance:
                    appointments_staff = appointments_staff.exclude(pk=self.instance.pk)

                for staff in appointments_staff:
                    if staff.datetime == value or abs(staff.datetime - value) <= timedelta(hours=1):
                        raise serializers.ValidationError('Funcionários já possuem serviço próximo agendado')

            if get_client:
                appointments = Appointment.objects.filter(client=get_client)
                if self.instance:
                    appointments = appointments.exclude(pk=self.instance.pk)

                for client in appointments:
                    if client.datetime == value or abs(client.datetime - value) <= timedelta(hours=1):
                        raise serializers.ValidationError(f'Cliente: {client_name.name} já possui agendamento próximo agendado')
        return value

    def get_date(self, obj):
        if obj.datetime:
            return f'{obj.datetime.strftime("%d/%m/%Y")} - {obj.datetime.strftime("%H:%M")}'
        return None