from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from sender.models import Newsletter
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, View
from django.urls import reverse_lazy
from sender.apps import SenderConfig
from sender.forms import NewsletterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from blog.models import Blog
import random
from client.models import Client


app_name = SenderConfig.name


class NewsletterListView(LoginRequiredMixin, ListView):
    model = Newsletter


class NewsletterDetailView(LoginRequiredMixin, DetailView):
    model = Newsletter

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if (self.object.owner != self.request.user and not self.request.user.is_superuser
                and not self.request.user.is_staff):
            raise Http404
        return self.object


class NewsletterCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Newsletter
    form_class = NewsletterForm
    permission_required = 'sender.add_newsletter'
    success_url = reverse_lazy('sender:newsletter_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('sender:newsletter_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('sender:newsletter_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_superuser:
            raise Http404
        return self.object

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


@login_required
@permission_required('sender.set_is_active', login_url='sender:newsletter_list')
def deactivate_newsletter(request, pk):
    user = Newsletter.objects.get(pk=pk)
    user.is_active = False
    user.save()
    return redirect(reverse('sender:newsletter_list'))


@login_required
@permission_required('sender.set_is_active', login_url='sender:newsletter_list')
def activate_newsletter(request, pk):
    user = Newsletter.objects.get(pk=pk)
    user.is_active = True
    user.save()
    return redirect(reverse('sender:newsletter_list'))


class HomePageView(ListView):
    model = Newsletter
    template_name = 'sender/homepage.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mail_count'] = len(Newsletter.objects.all())
        context_data['active_mail_count'] = len(Newsletter.objects.filter(is_active=True))
        context_data['clients_count'] = len(Client.objects.all())
        blogs = list(Blog.objects.all())
        random.shuffle(blogs)
        context_data['blogs'] = blogs[:3]
        return context_data
