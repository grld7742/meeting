# Generated by Django 5.0.4 on 2024-04-19 18:31

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('floor_number', models.IntegerField(default=2)),
                ('room_number', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('start_time', models.TimeField(default=datetime.time(4, 0))),
                ('duration', models.IntegerField(default=2)),
                ('room', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='meetings.room')),
            ],
        ),
    ]
