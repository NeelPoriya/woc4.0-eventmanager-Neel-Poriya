from django.forms import ModelForm
from django import forms
from .models import Event, Participant
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class EventForm(forms.ModelForm):
    info = dict()
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'event_name': forms.TextInput(attrs={'placeholder':'Event Name'}),
            'description': forms.Textarea(attrs={'placeholder':'Description'}),
            'location': forms.TextInput(attrs={'placeholder':'Location'}),
            'from_date': forms.TextInput(attrs={'placeholder': 'Event Start Date', 'onfocus':'fun(this.id)'}),
            'to_date': forms.TextInput(attrs={'placeholder': 'Event End Date', 'onfocus':'fun(this.id)'}),
            'registration_end_date': forms.TextInput(attrs={'placeholder': 'Registration End Date', 'onfocus':'fun(this.id)'}),
            'from_time':forms.TextInput(attrs={'placeholder': 'Event Start Time', 'onfocus':'fun2(this.id)'}),
            'to_time': forms.TextInput(attrs={'placeholder': 'Event End Time', 'onfocus':'fun2(this.id)'}),
            'registration_end_time': forms.TextInput(attrs={'placeholder': 'Registration End Time', 'onfocus':'fun2(this.id)'}),
            'host_email': forms.EmailInput(attrs={'placeholder':'Email ID'}),
            'host_password':forms.PasswordInput(attrs={'placeholder':'Email Password'}),
            'status': forms.TextInput(attrs={'placeholder':'Status', 'type':'number'}),
            'poster_link': forms.TextInput(attrs={'placeholder':'Poster Link'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        error_found = False

        event_name = cleaned_data['event_name']
        location = cleaned_data['location']
        from_date = cleaned_data['from_date']
        from_time = cleaned_data['from_time']
        to_date = cleaned_data['to_date'] 
        to_time = cleaned_data['to_time']
        registration_end_date = cleaned_data['registration_end_date']
        registration_end_time = cleaned_data['registration_end_time']


        if len(event_name) < 4:
            self.add_error('event_name', 'Event name should have atleast 4 characters.')
            error_found = True

        if location.lower() != 'online' and location.lower() != 'offline':
            self.add_error('location','Location can either be online or offline')
            error_found = True

        if from_date < datetime.date.today():
            self.add_error('from_date','Event should take place in future')
            error_found = True

        cur_time = str(datetime.datetime.now().strftime("%H:%M:%S"))
        if from_date == datetime.date.today() and str(from_time) < cur_time:
            self.add_error('from_time','Event should take place in future')
            error_found = True

        if to_date < from_date:
            self.add_error('to_date','Event should end after it starts🙂')
            error_found = True

        if from_date == to_date and to_time < from_time:
            self.add_error('to_time','Event should end after it starts🙂')
            error_found = True
            
        if registration_end_date > to_date:
            self.add_error('registration_end_date','Registration should end before ending of event')
            error_found = True
            
        if registration_end_date == to_date and registration_end_time > to_time:
            self.add_error('registration_end_time','Registration should end before ending of event')
            error_found = True

        if error_found:
            raise forms.ValidationError('you cant make one thing right')


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'mobile_number': forms.TextInput(attrs={'placeholder': 'Mobile Number with Country Code', 'type':'number'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email ID'}),
            'registration_type': forms.Select(attrs={'placeholder':'Registration Type'}),
            'no_of_people': forms.TextInput(attrs={'placeholder': 'No. of people', 'type':'number'}),
        }

    def has_unique_mobile_number(self, cleaned_data):
            for participant in Participant.objects.all():
                if participant.mobile_number == cleaned_data['mobile_number']:
                    return False
            return True

    def has_unique_email(self, cleaned_data):
        for participant in Participant.objects.all():
            if participant.email == cleaned_data['email']:
                return False
        return True
    
    def clean(self):
        error_found = False
        cleaned_data = super().clean()
        
        name = cleaned_data['name']
        mobile_number = cleaned_data['mobile_number']
        email = cleaned_data['email']
        event = cleaned_data['event']
        registration_type = cleaned_data['registration_type']
        no_of_people = cleaned_data['no_of_people']

        if len(name) < 4:
            self.add_error('name', 'Name should have atleast 4 characters.')
            error_found = True

        if registration_type == 'Individual' and no_of_people > 1:
            self.add_error('no_of_people', 'Individual registration must have single person.')
            error_found = True

        if mobile_number < 0:
            self.add_error('mobile_number', 'Mobile Numbers cannot be negative')
            error_found = True

        if registration_type == 'Group' and no_of_people <= 1:
            self.add_error('no_of_people', 'No. of members should be greater than 1.')
            error_found = True

        if not self.has_unique_mobile_number(cleaned_data=cleaned_data):
            self.add_error('mobile_number', 'Mobile number should be unique.')

        if not self.has_unique_email(cleaned_data=cleaned_data):
            self.add_error('email', 'Email should be unique.')

        end_date = cleaned_data['event'].registration_end_date
        end_time = cleaned_data['event'].registration_end_time
        reg_end = datetime.datetime(end_date.year, end_date.month, end_date.day, end_time.hour, end_time.minute, end_time.second)
        if datetime.datetime.now() > reg_end:
            self.add_error('event', 'Registration for this event has ended.')

        if error_found:
            raise forms.ValidationError('')

class EventDashboardForm(forms.Form):
    event_ID = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Event ID', 'type':'number'}))
    host_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))


    def clean(self):
        cleaned_data = super().clean()

        event = Event.objects.filter(id=cleaned_data['event_ID'])
        if not event:
            self.add_error('event_ID', 'No Event found')

        if event[0].host_password != cleaned_data['host_password']:
            self.add_error('host_password', 'Incorrect Answer')


