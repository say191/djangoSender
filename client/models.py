from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.CharField(max_length=100, verbose_name='email', unique=True)
    fio = models.CharField(max_length=150, verbose_name='fio')
    comment = models.CharField(**NULLABLE, max_length=100, verbose_name='comment')

    def __str__(self):
        return f"{self.fio} - {self.email}"

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
