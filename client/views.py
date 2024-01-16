from client.models import Client
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse
from client.apps import ClientConfig

app_name = ClientConfig.name


class ClientListView(ListView):
    model = Client


class ClientCreate(CreateView):
    model = Client
    fields = ('fio', 'email', 'comment')
    success_url = reverse_lazy('client:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client:client_list')


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('fio', 'email', 'comment')
    # success_url = reverse_lazy('client:view')

    def get_success_url(self):
        return reverse('client:client_view', args=[self.object.pk])