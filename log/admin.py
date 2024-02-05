from django.contrib import admin
from log.models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('try_date', 'try_status', 'try_response', 'email')
    list_filter = ('try_date',)
    search_fields = ('email',)
