from django.forms import ModelForm
from django import forms
from .models import Event

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class EventForm(forms.ModelForm):   
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'from_date': DateInput,
            'to_date': DateInput,
            'registration_end_date': DateInput,
            'from_time':TimeInput,
            'to_time':TimeInput,
            'registration_end_time':TimeInput
        }