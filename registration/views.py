import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EventForm, ParticipantForm, EventDashboardForm
from .models import Event, Participant


def events(request):
    return render(request, 'index.html')

def events_register(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            eve = Event(event_name=cleaned['event_name'], description=cleaned['description'], location=cleaned['location'], from_date=cleaned['from_date'], from_time=cleaned['from_time'], to_date=cleaned['to_date'], to_time=cleaned['to_time'], registration_end_date=cleaned['registration_end_date'], registration_end_time=cleaned['registration_end_time'], host_email=cleaned['host_email'], host_password=cleaned['host_password'], status=cleaned['status'], poster_link=cleaned['poster_link'])
            eve.save()
            form = EventForm()
    else:
        form = EventForm()

    return render(request, 'event_register.html', {'form': form})


def show_events(request):
    if request.method == 'POST':
        participant_form = ParticipantForm(request.POST)
        if participant_form.is_valid():
            cleaned = participant_form.cleaned_data
            participant = Participant(name=cleaned['name'], mobile_number=cleaned['mobile_number'], email=cleaned['email'], event=cleaned['event'], registration_type=cleaned['registration_type'], no_of_people=cleaned['no_of_people'])
            participant.save()
            participant_form = ParticipantForm()
    else:
        participant_form = ParticipantForm()
        
    return render(request, 'show_events.html', {
        'events': Event.objects.all(),
        'form': participant_form,
    })


def event_dashboard(request):
    all_participants = []
    if request.method == 'POST':
        dashboard_form = EventDashboardForm(request.POST)
        if dashboard_form.is_valid():
            cleaned = dashboard_form.cleaned_data
            if len(Event.objects.filter(id=cleaned['event_ID'])) > 0:
                event_details = Event.objects.filter(id=cleaned['event_ID'])[0]
                for participant in Participant.objects.all():
                    if participant.event == event_details:
                        all_participants.append(participant)
    else:
        dashboard_form = EventDashboardForm()

    return render(request, 'event_dashboard.html', {
        'form': dashboard_form,
        'participants': all_participants,
    })
