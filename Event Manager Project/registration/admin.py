from django.contrib import admin
from .models import Event, Participant

# Register your models here.
# admin.site.register(Event)
admin.site.register(Participant)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_name', 'description', 'location', 'from_date', 'from_time', 'to_date', 'to_time', 'registration_end_date', 'registration_end_time', 'host_email', 'host_password', 'status', 'poster_link']
