from django.urls import path
from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, verify, block_user, activate_user
from users.views import UserUpdateView, change_password, forgot_password, UserListView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/', verify, name='verify'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/change_password/', change_password, name='change_password'),
    path('profile/forgot_password/', forgot_password, name='forgot_password'),
    path('block/<int:pk>/', block_user, name='block_user'),
    path('activate/<int:pk>/', activate_user, name='activate_user')
]
