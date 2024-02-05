from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=30, verbose_name='title')
    content = models.TextField(max_length=500, verbose_name='content')
    preview = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='preview')
    view_count = models.IntegerField(default=0, verbose_name='view_count')
    date_publicised = models.DateField(verbose_name='date_created')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
