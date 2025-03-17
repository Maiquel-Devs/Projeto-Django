from django.db import models

class Criar_Usuario(models.Model):

    nome = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
