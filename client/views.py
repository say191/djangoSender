from client.models import Client
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse
from client.apps import ClientConfig
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.contrib.auth.mixins import PermissionRequiredMixin

app_name = ClientConfig.name


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get(self, request):
        if self.request.user.is_staff and not self.request.user.is_superuser:
            raise Http404
        return super().get(request)


class ClientCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Client
    fields = ('fio', 'email', 'comment')
    permission_required = 'client.add_client'
    success_url = reverse_lazy('client:client_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('client:client_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('fio', 'email', 'comment')

    def get_success_url(self):
        return reverse('client:client_view', args=[self.object.pk])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object