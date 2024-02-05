from django.contrib import admin
from client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('fio', 'email', 'comment')
    list_filter = ('fio',)
    search_fields = ('fio',)
