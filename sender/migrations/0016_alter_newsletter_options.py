# Generated by Django 4.2.7 on 2024-02-05 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sender', '0015_newsletter_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'permissions': [('set_is_active', 'Can activate and deactivate newsletters')], 'verbose_name': 'newsletter', 'verbose_name_plural': 'newsletters'},
        ),
    ]
