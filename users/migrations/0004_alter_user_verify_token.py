# Generated by Django 4.2.7 on 2024-02-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verify_token',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='verify_token'),
        ),
    ]