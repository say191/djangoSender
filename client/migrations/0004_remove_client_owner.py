# Generated by Django 4.2.7 on 2024-02-04 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='owner',
        ),
    ]
