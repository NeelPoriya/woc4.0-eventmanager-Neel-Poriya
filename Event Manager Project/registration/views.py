import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EventForm, ParticipantForm, EventDashboardForm
from .models import Event, Participant
from django.core.mail import send_mail
from Event_Manager import settings
from twilio.rest import Client
from decouple import config

def send_message(mobile, event):
    account_sid = "ACf7dde42890ed5500f12a3a3d336845f0"
    # don't copy this, it is generated new everytime I use😉
    auth_token = "dda32c16798559f5eb498d6878a36e99"
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create(  
                    body=f"""You have registered successfully
Event ID : {event.id}  
Event Password : {event.host_password}
                            """,
                     from_='+14158436176',
                     to=f'+{str(mobile)}' 
                            ) 

def sendMail(to, event):
    send_mail("Thanks for Registration",
    f"""
        Here are the details for the event:
        Event ID: {event.id}
        Event Name: {event.event_name}
        Event Description: {event.description}
        Event Location: {event.location}
        Event Starts from: {event.from_date} {event.from_time}
        Event Ends at: {event.to_date} {event.to_time}
        Event Registration Ends at: {event.registration_end_date} {event.registration_end_time}
        Event Host Email: {event.host_email}
        Event Host Password: {event.host_password}
        Event Status: {event.status}
    """,
    settings.EMAIL_HOST,
    [to],
    fail_silently=False
    )


def events(request):
    return render(request, 'index.html')

def events_register(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            eve = Event(event_name=cleaned['event_name'], description=cleaned['description'], location=cleaned['location'], from_date=cleaned['from_date'], from_time=cleaned['from_time'], to_date=cleaned['to_date'], to_time=cleaned['to_time'], registration_end_date=cleaned['registration_end_date'], registration_end_time=cleaned['registration_end_time'], host_email=cleaned['host_email'], host_password=cleaned['host_password'], status=cleaned['status'], poster_link=cleaned['poster_link'])
            eve.save()
            # sendMail(cleaned['host_email'], eve)
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
            #send_message(participant.mobile_number, participant.event)
            participant_form = ParticipantForm()
    else:
        participant_form = ParticipantForm()
        
    return render(request, 'show_events.html', {
        'events': Event.objects.all(),
        'form': participant_form,
    })


def event_dashboard(request):
    first_time = True
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
            first_time = False

    else:
        dashboard_form = EventDashboardForm()
        first_time = True

    return render(request, 'event_dashboard.html', {
        'form': dashboard_form,
        'participants': all_participants,
        'firsttime' : first_time
    })
