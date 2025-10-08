from django.db import models
from services.models import Service

class Review(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service')
    stars = models.IntegerField()
    comment = models.TextField(help_text='Deixe um comentário sobre a avaliação')

    def __str__(self):
        return self.service


