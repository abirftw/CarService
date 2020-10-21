from django.contrib import admin
from .models import TimeSlots, Services, AppointmentDetails
# Register your models here.
admin.site.register(Services)
admin.site.register(TimeSlots)
admin.site.register(AppointmentDetails)
