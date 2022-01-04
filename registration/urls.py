from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='event'),
    path('register/', views.events_register, name='event_register'),
]
