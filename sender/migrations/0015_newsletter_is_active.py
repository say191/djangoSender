# Generated by Django 4.2.7 on 2024-02-05 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0014_alter_newsletter_next_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
    ]