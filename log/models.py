from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Log(models.Model):
    try_date = models.DateTimeField(verbose_name="try_date")
    try_status = models.CharField(verbose_name='try_status')
    try_response = models.CharField(verbose_name='try_status')
    email = models.CharField(**NULLABLE, verbose_name='email')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='owner', **NULLABLE)

    def __str__(self):
        return f"{self.try_date} - {self.try_response} - {self.try_status}"

    class Meta:
        verbose_name = 'log'
        verbose_name_plural = 'logs'
