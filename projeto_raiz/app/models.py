from django.db import models

class Pessoa(models.Model):
    nome = models.CharField()
    idade = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nome