# Generated by Django 5.0.1 on 2024-01-16 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_rename_clients_log_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='try_date',
            field=models.CharField(verbose_name='try_date'),
        ),
    ]