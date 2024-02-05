from log.models import Log
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from log.apps import LogConfig

app_name = LogConfig.name


class LogListView(LoginRequiredMixin, ListView):
    model = Log

    def get(self, request):
        if self.request.user.is_staff and not self.request.user.is_superuser:
            raise Http404
        return super().get(request)


class LogDeleteView(LoginRequiredMixin, DeleteView):
    model = Log
    success_url = reverse_lazy('log:log_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object