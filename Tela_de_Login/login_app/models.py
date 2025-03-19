from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class UsuarioManager(BaseUserManager):
    def create_user(self, email, senha=None, **extra_fields):
        if not email:
            raise ValueError("O usuário deve ter um endereço de e-mail")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_senha(senha)  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, senha=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, senha, **extra_fields)

class Usuario(AbstractBaseUser):
    nome = models.CharField(max_length=191)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['nome']  

    objects = UsuarioManager()

    def set_senha(self, senha):
        """Hash da senha antes de salvar."""
        self.password = make_password(senha)  

    def verificar_senha(self, senha):
        """Verifica se a senha digitada é correta."""
        return check_password(senha, self.password)  

    def __str__(self):
        return self.nome
