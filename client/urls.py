from django.urls import path
from client.apps import ClientConfig
import client.views

app_name = ClientConfig.name
urlpatterns = [
    path('clients/', client.views.ClientListView.as_view(), name='client_list'),
    path('clients/create/', client.views.ClientCreate.as_view(), name='client_create'),
    path('clients/delete/<int:pk>/', client.views.ClientDeleteView.as_view(), name='client_delete'),
    path('clients/view/<int:pk>/', client.views.ClientDetailView.as_view(), name='client_view'),
    path('clients/edit/<int:pk>/', client.views.ClientUpdateView.as_view(), name='client_update')
]
