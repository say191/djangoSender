# Generated by Django 5.0.1 on 2024-01-16 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_remove_log_clients_log_clients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='clients',
            new_name='email',
        ),
    ]
