from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='event'),
    path('register/', views.events_register, name='event_register'),
    path('show_events/', views.show_events, name='participant-registration'),
    path('dashboard/', views.event_dashboard, name='event-dashboard')
]
