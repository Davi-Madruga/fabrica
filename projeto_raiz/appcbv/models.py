from django.db import models

# Create your models here.
class Cachorro(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    raca = models.CharField(max_length=30)
    instagram = models.CharField(max_length=32)

    def __str__(self):
        return self.nome + '-' + self.instagram 