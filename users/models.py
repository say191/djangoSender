from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.CharField(unique=True, verbose_name='email')
    FIO = models.CharField(max_length=30, verbose_name='FIO', **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='phone', **NULLABLE)
    verify_token = models.CharField(max_length=5, verbose_name='verify_token', **NULLABLE)
    is_active = models.BooleanField(verbose_name='is_active', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
