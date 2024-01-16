from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Log(models.Model):
    try_date = models.CharField(verbose_name='try_date')
    try_status = models.CharField(verbose_name='try_status')
    try_response = models.CharField(verbose_name='try_status')
    email = models.CharField(**NULLABLE, verbose_name='email')

    def __str__(self):
        return f"{self.try_date} - {self.try_response} - {self.try_status}"

    class Meta:
        verbose_name = 'log'
        verbose_name_plural = 'logs'
