# Generated by Django 5.0.5 on 2024-05-07 01:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_arenda_date_from_car_photos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='photos',
        ),
        migrations.AddField(
            model_name='arenda',
            name='date_from',
            field=models.DateField(default=datetime.date(2024, 5, 7)),
        ),
        migrations.AlterField(
            model_name='arenda',
            name='date_to',
            field=models.DateField(default='2024-05-08'),
        ),
    ]
