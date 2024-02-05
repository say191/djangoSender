from django.contrib import admin
from sender.models import Newsletter


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('theme_message', 'owner', 'text_message', 'start_date', 'stop_date', 'next_date',
                    'periodicity', 'status')
    list_filter = ('start_date',)
    search_fields = ('theme_message', 'text_message')
