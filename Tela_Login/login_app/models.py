from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=150, unique=True)
    senha = models.CharField(max_length=128)  

    def __str__(self):
        return self.usuario

