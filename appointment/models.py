from django.db import models
from enum import IntEnum, Enum
import datetime


class Days(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


DATE_FORMAT = "%b. %d, %Y"
ALLDAY = 7
CLOSED_DAY = Days.SUNDAY


class Services(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class TimeSlots(models.Model):
    startTime = models.TimeField()
    endTime = models.TimeField()


class AppointmentDetails(models.Model):
    app_date = models.DateField('Appointment Date')
    app_slot = models.ForeignKey(TimeSlots, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
