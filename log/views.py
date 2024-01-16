from log.models import Log
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

from log.apps import LogConfig

app_name = LogConfig.name


class LogListView(ListView):
    model = Log


class LogDeleteView(DeleteView):
    model = Log
    success_url = reverse_lazy('log:log_list')