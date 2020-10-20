from django.db import models

# Create your models here.


class Services(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=3, decimal_places=2)


class AppointmentDetails(models.Model):
    app_date = models.DateField('Appointment Date')
    app_slot = models.PositiveIntegerField()
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
