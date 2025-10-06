from django import forms
from django_select2.forms import Select2Widget, Select2MultipleWidget
from django.utils import timezone
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

    def clean_datetime(self):
        datetime_field = self.cleaned_data.get('datetime')

        if datetime_field and datetime_field < timezone.now():
            raise forms.ValidationError('Data de agendamento inválida.')
        return datetime_field



