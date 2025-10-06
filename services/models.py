from django.db import models

class Service(models.Model):
    name = models.CharField(blank=False, null=False, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)
    duration = models.PositiveIntegerField(help_text='A duração precisa ser inserida em minutos.')
    description = models.TextField(max_length=500, help_text='Breve descrição do serviço.')

    def __str__(self):
        return self.name

