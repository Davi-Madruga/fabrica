from django.db import models

class Pokemon(models.Model):
    id_pokemon = models.CharField()
    name = models.CharField()
    types = models.CharField()
    height = models.CharField()
    weight = models.CharField()
    image_url = models.URLField()
    
    def __str__(self):
        return f"#{self.id_pokemon}|{self.name}"