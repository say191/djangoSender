# Generated by Django 5.0.1 on 2024-01-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0003_alter_newsletter_time_send'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='time_send',
            field=models.CharField(max_length=5, verbose_name='time_send (in format HH:MM)'),
        ),
    ]
