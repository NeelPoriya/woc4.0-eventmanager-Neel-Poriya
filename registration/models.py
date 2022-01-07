from django.db import models
import datetime


class Event(models.Model):
    event_name = models.CharField(max_length=30)
    description = models.TextField(max_length=400)
    location = models.CharField(max_length=30)
    from_date = models.DateField()
    from_time = models.TimeField()
    to_date = models.DateField()
    to_time = models.TimeField()
    registration_end_date = models.DateField()
    registration_end_time = models.TimeField()
    host_email = models.EmailField()
    host_password = models.CharField(max_length=30)
    status = models.IntegerField()
    poster_link = models.CharField(max_length=100000)

    def __str__(self):
        return self.event_name

    def get_foreign_fields(self):
        return [getattr(self, f.name) for f in self._meta.fields if type(f) == models.fields.related.ForeignKey]


class Participant(models.Model):
    name = models.CharField(max_length=30)
    mobile_number = models.IntegerField()
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_type = models.CharField(max_length=30, default='Choose Participation Type',choices=(
        ('Individual', 'Individual'),
        ('Group', 'Group'),
    ))
    no_of_people = models.IntegerField()

    def __str__(self):
        return self.name

    
    