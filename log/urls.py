from django.urls import path
from log.apps import LogConfig
import log.views

app_name = LogConfig.name
urlpatterns = [
    path('', log.views.LogListView.as_view(), name='log_list'),
    path('delete/<int:pk>/', log.views.LogDeleteView.as_view(), name='log_delete')
]