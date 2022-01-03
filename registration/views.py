from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EventForm
from .models import Event

# Create your views here.
def events(request):
    return render(request, 'index.html');


def events_register(request):
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            eve = Event(event_name=cleaned['event_name'], description=cleaned['description'], location=cleaned['location'], from_date=cleaned['from_date'], from_time=cleaned['from_time'], to_date=cleaned['to_date'], to_time=cleaned['to_time'], registration_end_date=cleaned['registration_end_date'], registration_end_time=cleaned['registration_end_time'], host_email=cleaned['host_email'], host_password=cleaned['host_password'], status=cleaned['status'])
            eve.save()
            form = EventForm()
    else:
        form = EventForm()

    return render(request, 'event_register.html', {'form': form})