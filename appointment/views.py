from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import CLOSED_DAY, ALLDAY, DATE_FORMAT, Days, TimeSlots, Services, AppointmentDetails
import datetime
# Create your views here.


def home(request):
    ap_dates = []
    for i in range(ALLDAY):
        day = (datetime.datetime.now() + datetime.timedelta(i))
        if day.weekday() != CLOSED_DAY:
            ap_dates.append(day)
    context = {'ap_dates': ap_dates, 'closed_day': Days(CLOSED_DAY).name}
    return render(request, 'appointment/book.html', context)


def slotsOpen(request):
    date = datetime.datetime.strptime(request.GET['date'], DATE_FORMAT)
    avail_list = list(
        filter(lambda x: x not in TimeSlots.objects.filter(appointmentdetails__app_date=date),
               TimeSlots.objects.all()))
    context = {
        'available_slot': avail_list,
        'service_list': Services.objects.all(),
        'curDate': date
    }
    return render(request, 'appointment/slotsAvailable.html', context)


def book(request):
    date = datetime.datetime.strptime(
        request.POST['curdate'], DATE_FORMAT)
    if AppointmentDetails.objects.filter(
            app_date=date, app_slot_id=request.POST['slot']).exists():
        return HttpResponseRedirect(reverse('slots'))
    else:
        AppointmentDetails.objects.create(
            app_date=date, app_slot_id=request.POST['slot'], service_id=request.POST['service'], phone=request.POST['phone'])
    return HttpResponseRedirect(reverse('home'))
