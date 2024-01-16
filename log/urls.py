from django.urls import path
from log.apps import LogConfig
import log.views

app_name = LogConfig.name
urlpatterns = [
    path('logs/', log.views.LogListView.as_view(), name='log_list'),
    path('logs/delete/<int:pk>/', log.views.LogDeleteView.as_view(), name='log_delete')
]