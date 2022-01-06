from django.forms import ModelForm
from django import forms
from .models import Event, Participant


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class EventForm(forms.ModelForm):
    from_date_on_focus = "this.type=data"   
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
            'status': forms.TextInput(attrs={'placeholder':'Status'}),
            'poster_link': forms.TextInput(attrs={'placeholder':'Poster Link'}),
        }


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'mobile_number': forms.TextInput(attrs={'placeholder': 'Mobile Number'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email ID'}),
            'event': forms.Select(attrs={'placeholder':'Event'}),
            'regestration_type': forms.Select(attrs={'placeholder':'Registration Type'}),
            'no_of_people': forms.TextInput(attrs={'placeholder': 'No. of people'}),
        }


class EventDashboardForm(forms.Form):
    event_ID = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Event ID'}))
    host_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))


