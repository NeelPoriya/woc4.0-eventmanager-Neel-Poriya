# Generated by Django 4.0 on 2022-01-04 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_participant_registration_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='mobile_number',
            field=models.IntegerField(),
        ),
    ]
