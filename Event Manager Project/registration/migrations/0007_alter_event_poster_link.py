# Generated by Django 4.0 on 2022-01-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_event_poster_link_alter_participant_no_of_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='poster_link',
            field=models.URLField(default=''),
        ),
    ]
