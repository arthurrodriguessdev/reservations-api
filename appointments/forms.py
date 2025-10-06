from django import forms
from django_select2.forms import Select2Widget, Select2MultipleWidget
from django.utils import timezone
from datetime import timedelta
from appointments.models import Appointment
from clients.models import Client
from services.models import Service
from staff.models import Staff

class AppointmentForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        required=True,
        queryset = Client.objects.all(),
        widget=Select2Widget(
            attrs={
                'data-placeholder': 'Select client'
            },
        ),
    )

    service = forms.ModelChoiceField(
        required=True,
        queryset = Service.objects.all(),
        widget=Select2Widget(
            attrs={
                'data-placeholder': 'Select service'
            },
        ),
    )

    staff = forms.ModelMultipleChoiceField(
        queryset=Staff.objects.all(),
        widget=Select2MultipleWidget(
            attrs={
                'data-placeholder': 'Select staff'
            },
        ),
    )

    class Meta:
        model = Appointment
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        datetime_field = cleaned_data.get('datetime')
        client = cleaned_data.get('client')
        staff = cleaned_data.get('staff')

        for appointment in Appointment.objects.filter(client=client).exclude(pk=self.instance.pk):
            if appointment.datetime == datetime_field or abs(appointment.datetime - datetime_field) <= timedelta(hours=1):
                raise forms.ValidationError('O cliente já possui agendamentos em mesma data e/ou próximas.')
        
        for appointment in Appointment.objects.filter(staff__in=staff).exclude(pk=self.instance.pk):
                if appointment.datetime == datetime_field or abs(appointment.datetime - datetime_field) <= timedelta(hours=1):
                    raise forms.ValidationError('Os profissionais já possuem um serviço com datas próximas.')

        if datetime_field and datetime_field < timezone.now():
            raise forms.ValidationError('Data de agendamento inválida.')
        
        return cleaned_data



