from django.db import models


# Banco de dados que recebem em JSON
class Nome(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
