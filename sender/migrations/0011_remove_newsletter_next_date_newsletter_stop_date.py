# Generated by Django 4.2.7 on 2024-02-04 22:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0010_remove_newsletter_time_send_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='next_date',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='stop_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='stop_date'),
        ),
    ]
