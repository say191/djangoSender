from django.contrib import admin
from sender.models import Newsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('theme_message', 'text_message', 'time_send', 'time_stop', 'periodicity',
                    'status')
    list_filter = ('time_send',)
    search_fields = ('theme_message', 'text_message')
