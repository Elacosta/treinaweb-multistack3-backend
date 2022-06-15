from django.db import models

# definição do modelo
class Pet(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200)
    history = models.TextField(blank=False, null=False)
    photo = models.URLField(blank=False, null=False)
