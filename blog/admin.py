from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'preview', 'view_count', 'date_publicised')
    list_filter = ('date_publicised',)
    search_fields = ('title', 'content')
