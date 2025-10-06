from django.contrib import admin
from datetime import datetime
from appointments.models import Appointment
from appointments.forms import AppointmentForm

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('service', 'client', 'get_formatted_datetime',)
    search_fields = ('service', 'client', 'datetime',)
    ordering = ('-service',)
    form = AppointmentForm

    @admin.display(description='Datetime')
    def get_formatted_datetime(self, obj):
        return f'{obj.datetime.strftime("%d/%m/%Y")} - {obj.datetime.strftime("%H:%M")}'

admin.site.register(Appointment, AppointmentAdmin)