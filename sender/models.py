from django.db import models
from users.models import User
from client.models import Client
from django.utils import timezone

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
    start_date = models.DateTimeField(default=timezone.now, verbose_name="start_date")
    stop_date = models.DateTimeField(default=timezone.now, verbose_name="stop_date")
    next_date = models.DateTimeField(default=timezone.now, verbose_name="next_date")
    periodicity = models.CharField(choices=PERIODICITY, verbose_name='periodicity', default='Once a day')
    status = models.CharField(choices=STATUS, verbose_name='status', default='Created')
    clients = models.ManyToManyField(Client, verbose_name='clients')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='owner', **NULLABLE)
    is_active = models.BooleanField(verbose_name='is_active', default=True)

    def __str__(self):
        return f"{self.theme_message}"

    class Meta:
        verbose_name = 'newsletter'
        verbose_name_plural = 'newsletters'

        permissions = [
            ("set_is_active", "Can activate and deactivate newsletters")
        ]
