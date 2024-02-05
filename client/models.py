from django.db import models
from users.models import User


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.CharField(max_length=100, verbose_name='email', unique=True)
    fio = models.CharField(max_length=150, verbose_name='fio')
    comment = models.CharField(**NULLABLE, max_length=100, verbose_name='comment')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='owner', **NULLABLE)

    def __str__(self):
        return f"{self.fio} - {self.email}"

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
