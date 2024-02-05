# Generated by Django 4.2.7 on 2024-02-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title')),
                ('content', models.TextField(max_length=500, verbose_name='content')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='preview')),
                ('view_count', models.IntegerField(default=0, verbose_name='view_count')),
                ('date_publicised', models.DateField(verbose_name='date_created')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
            },
        ),
    ]