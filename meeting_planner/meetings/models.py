from django.db import models
from datetime import time


# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50)
    floor_number = models.IntegerField(default=2)
    room_number = models.IntegerField(default=2)


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(4))
    duration = models.IntegerField(default=2)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=1)
