from django import forms
from staff.models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.name = instance.name.title()

        if commit:
            instance.save()
        return instance
