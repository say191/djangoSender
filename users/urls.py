from django.urls import path
from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, verify, UserUpdateView, change_password, forgot_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/', verify, name='verify'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/change_password/', change_password, name='change_password'),
    path('profile/forgot_password/', forgot_password, name='forgot_password')
]
