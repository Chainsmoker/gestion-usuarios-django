from django.db import models
from django.contrib.auth.models import AbstractUser
from roles.models import Rol

# Create your models here.
class Usuario(AbstractUser):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
