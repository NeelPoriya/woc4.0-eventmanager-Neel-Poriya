# Generated by Django 4.0 on 2022-01-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_alter_participant_mobile_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='poster_link',
            field=models.URLField(default='nolink.com'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='no_of_people',
            field=models.IntegerField(default=1),
        ),
    ]
