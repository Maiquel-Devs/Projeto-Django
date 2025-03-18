from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    nome = models.CharField(max_length=191, unique=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    def set_senha(self, senha):
        """Hash da senha antes de salvar."""
        self.senha = make_password(senha)

    def verificar_senha(self, senha):
        """Verifica se a senha digitada é correta."""
        return check_password(senha, self.senha)
    
    def __str__(self):
        return self.nome

