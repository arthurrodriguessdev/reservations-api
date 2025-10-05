from django import forms
from clients.models import Client

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        if email and "@" not in email:
            self.add_error('email', 'Insira um endereço de e-mail válido.')
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.name = instance.name.title()
        instance.email = instance.email.strip().lower()
        instance.phone_number = instance.phone_number.strip()

        if commit:
            instance.save()
        return instance