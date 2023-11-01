# models.py
from django.db import models

class Text(models.Model):
    id = models.IntegerField(primary_key=True)
    action = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}: {self.action}'
