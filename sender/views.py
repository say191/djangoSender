from sender.models import Newsletter
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from sender.apps import SenderConfig


app_name = SenderConfig.name


class NewsletterListView(ListView):
    model = Newsletter


class NewsletterDetailView(DetailView):
    model = Newsletter


class NewsletterCreate(CreateView):
    model = Newsletter
    fields = ('theme_message', 'text_message', 'time_send', 'time_stop', 'periodicity', 'status', 'clients')
    success_url = reverse_lazy('sender:newsletter_list')


class NewsletterDeleteView(DeleteView):
    model = Newsletter
    success_url = reverse_lazy('sender:newsletter_list')


class NewsletterUpdateView(UpdateView):
    model = Newsletter
    fields = ('theme_message', 'text_message', 'time_send', 'time_stop', 'periodicity', 'status', 'clients')
    success_url = reverse_lazy('sender:newsletter_list')
