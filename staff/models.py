from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} - {self.role}'
