from django.db import models

# Create your models here.
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

    def __str__(self):
        return self.event_name
    