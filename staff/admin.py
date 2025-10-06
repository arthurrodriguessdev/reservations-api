from django.contrib import admin
from staff.models import Staff
from staff.forms import StaffForm

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'role',)
    search_fields = ('name', 'role',)
    ordering = ('-name',)
    form = StaffForm

admin.site.register(Staff, StaffAdmin)