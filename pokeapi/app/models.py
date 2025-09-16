from django.db import models

class Pokemon(models.Model):
    id_pokemon = models.CharField()
    name = models.CharField()
    types = models.CharField()
    height = models.CharField()
    weight = models.CharField()