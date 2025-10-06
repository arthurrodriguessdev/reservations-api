from django import forms
from services.models import Service

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        price = cleaned_data.get('price')
        duration = cleaned_data.get('duration')
        name = cleaned_data.get('name')

        if price and price < 0.0:
            self.add_error('price', 'Insira um valor válido.')
        if duration and duration < 0:
            self.add_error('duration', 'Insira uma duração válida.')
        if name and Service.objects.filter(name=name).exclude(pk=self.pk):
            self.add_error('name', 'Já existe um serviço cadastrado com esse nome.')

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.name = instance.name.capitalize()

        if len(instance.description) == 0:
            instance.description = 'Este serviço não possui descrição'

        if commit:
            instance.save()
        return instance

