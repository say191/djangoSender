# Generated by Django 4.2.7 on 2024-02-04 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0008_newsletter_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='time_stop',
            field=models.CharField(default='23:59', max_length=5, verbose_name='time_stop (in format HH:MM)'),
        ),
    ]