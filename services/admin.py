from django.contrib import admin
from services.models import Service
#from services.forms import ServiceForm

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration', 'get_formatted_description',)
    search_fields = ('name', 'price', 'duration',)
    ordering = ('-name',)
    #form = ServiceForm

    @admin.display(description='Description')
    def get_formatted_description(self, obj):
        if len(obj.description) > 100:
            obj.description = f'{obj.description[:100]}'
        return obj.description

admin.site.register(Service, ServiceAdmin)
