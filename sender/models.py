from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Newsletter(models.Model):
    PERIODICITY = [
        ('Once a day', 'Once a day'),
        ('Once a week', 'Once a week'),
        ('Once a month', 'Once a month')
    ]
    STATUS = [
        ('Created', 'Created'),
        ('Launched', 'Launched'),
        ('Finished', 'Finished')
    ]
    theme_message = models.CharField(max_length=150, verbose_name='theme_message')
    text_message = models.TextField(verbose_name='text_message')
    time_send = models.CharField(max_length=5, verbose_name='time_send (in format HH:MM)')
    time_stop = models.CharField(max_length=5, verbose_name='time_stop (in format HH:MM)', default='00:00')
    periodicity = models.CharField(choices=PERIODICITY, verbose_name='periodicity', default='Once a day')
    status = models.CharField(choices=STATUS, verbose_name='status', default='Created')
    clients = models.ManyToManyField('client.Client', verbose_name='clients')

    def __str__(self):
        return f"{self.theme_message}"

    class Meta:
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'
