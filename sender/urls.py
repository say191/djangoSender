from django.urls import path
from sender.apps import SenderConfig
import sender.views

app_name = SenderConfig.name
urlpatterns = [
    path('', sender.views.HomePageView.as_view(), name='homepage'),
    path('newsletters/', sender.views.NewsletterListView.as_view(), name='newsletter_list'),
    path('create/', sender.views.NewsletterCreate.as_view(), name='newsletter_create'),
    path('view/<int:pk>/', sender.views.NewsletterDetailView.as_view(), name='newsletter_view'),
    path('delete/<int:pk>/', sender.views.NewsletterDeleteView.as_view(), name='newsletter_delete'),
    path('edit/<int:pk>/', sender.views.NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('deactivate/<int:pk>/', sender.views.deactivate_newsletter, name='deactivate_newsletter'),
    path('activate/<int:pk>/', sender.views.activate_newsletter, name='activate_newsletter')
    ]
