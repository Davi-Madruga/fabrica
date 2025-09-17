from django.db import models

class Usuario(models.Model):
    nome = models.CharField()
    email = models.CharField()
    idade = models.CharField()

    def __str__(self):
        return f"Nome: {self.nome} | Email: {self.email}"
