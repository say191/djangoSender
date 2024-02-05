from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, ListView
from users.models import User
from users.forms import UserForm, UserVerifyForm, UserProfileForm, UserChangePassForm, UserForgotPassForm
from django.urls import reverse_lazy, reverse
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission
from django.conf import settings


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users:verify')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        new_user.verify_token = str(random.randint(10001, 99999))
        new_user.save()
        message = MIMEMultipart()
        message['Subject'] = "Congratulations for registration on Newsletter's service!"
        message.attach(MIMEText(f"Your verify token:\n{new_user.verify_token}", 'plain'))
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=settings.EMAIL_HOST, password=settings.PASSWORD_HOST)
        connection.sendmail(from_addr=settings.EMAIL_HOST, to_addrs=new_user.email, msg=message.as_string())
        connection.close()
        return super().form_valid(form)


def verify(request):
    if request.POST:
        form = UserVerifyForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['verify_token']
            try:
                user = User.objects.get(verify_token=token)
                user.is_active = True
                permission_add_newsletter = Permission.objects.get(codename="add_newsletter")
                user.user_permissions.add(permission_add_newsletter)
                permission_add_client = Permission.objects.get(codename="add_client")
                user.user_permissions.add(permission_add_client)
                user.save()
                return render(request, 'users/register_success.html')
            except User.DoesNotExist:
                return render(request, 'users/register_fail.html')
    else:
        form = UserVerifyForm()
    return render(request, 'users/verify.html', {'form': form})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def change_password(request):
    if request.POST:
        form = UserChangePassForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password1']
            request.user.set_password(new_password)
            request.user.save()
            return redirect(reverse('users:login'))
    else:
        form = UserChangePassForm()
    return render(request, 'users/change_password.html', {'form': form})


def forgot_password(request):
    if request.POST:
        form = UserForgotPassForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                new_password = ''.join([random.choice('123456789qwerosgijklasfnbkdbfsaxzv') for _ in range(8)])
                user.set_password(new_password)
                user.save()
                message = MIMEMultipart()
                message['Subject'] = "Your new password on Newsletter's service"
                message.attach(MIMEText(f"Your password:\n{new_password}", 'plain'))
                connection = smtplib.SMTP('smtp.gmail.com')
                connection.starttls()
                connection.login(user=settings.EMAIL_HOST, password=settings.PASSWORD_HOST)
                connection.sendmail(from_addr=settings.EMAIL_HOST, to_addrs=user.email, msg=message.as_string())
                connection.close()
                return redirect(reverse('users:login'))
            except User.DoesNotExist:
                return render(request, 'users/forgot_password_failed.html')
    else:
        form = UserForgotPassForm()
        return render(request, 'users/forgot_password.html', {'form': form})


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'users.view_user'


def block_user(request, pk):
    user = User.objects.get(pk=pk)
    user.is_active = False
    user.save()
    return redirect(reverse('users:user_list'))


def activate_user(request, pk):
    user = User.objects.get(pk=pk)
    user.is_active = True
    user.save()
    return redirect(reverse('users:user_list'))
