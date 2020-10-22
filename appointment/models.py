from django.db import models
from enum import IntEnum
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

    def __str__(self):
        return str(self.startTime) + "-" + str(self.endTime)


class AppointmentDetails(models.Model):
    app_date = models.DateField('Appointment Date')
    app_slot = models.ForeignKey(TimeSlots, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return str(self.app_date) + " " + str(self.app_slot.id)

    @classmethod
    def createAppointment(cls, date, slot, service, number):
        if date < datetime.datetime.today() or date.weekday() == CLOSED_DAY:
            return None
        return cls.objects.create(app_date=date, app_slot_id=slot, service_id=service, phone=number)
