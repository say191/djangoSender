from django.urls import path
from client.apps import ClientConfig
import client.views
from django.views.decorators.cache import cache_page

app_name = ClientConfig.name
urlpatterns = [
    path('', client.views.ClientListView.as_view(), name='client_list'),
    path('create/', client.views.ClientCreate.as_view(), name='client_create'),
    path('delete/<int:pk>/', client.views.ClientDeleteView.as_view(), name='client_delete'),
    path('view/<int:pk>/', cache_page(60)(client.views.ClientDetailView.as_view()), name='client_view'),
    path('edit/<int:pk>/', client.views.ClientUpdateView.as_view(), name='client_update')
]
