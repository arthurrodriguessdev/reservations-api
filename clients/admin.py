from django.contrib import admin
from clients.models import Client
from clients.forms import ClienteForm

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'get_formatted_phone_number',)
    search_fields = ('name', 'email', 'phone_number',)
    ordering = ('-name',)
    form = ClienteForm

    @admin.display(description='Phone Number')
    def get_formatted_phone_number(self, obj):
        if len(obj.phone_number) == 11:
            return f'({obj.phone_number[0:2]}) {obj.phone_number[2:7]}-{obj.phone_number[7:]}'
        elif len(obj.phone_number) == 9:
            return f'{obj.phone_number[0:5]}-{obj.phone_number[5:]}'
        return obj.phone_number

admin.site.register(Client, ClientAdmin)
