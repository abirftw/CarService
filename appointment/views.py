from django.shortcuts import render
from enum import Enum
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import CLOSED_DAY, ALLDAY, DATE_FORMAT, Days, TimeSlots, Services, AppointmentDetails
import datetime
# Create your views here.

BAD_ATTEMPT = 1
SUCCESS = 2
DEFAULT = 3
messages = {
    BAD_ATTEMPT: "Something went wrong, try again",
    SUCCESS: "Your appointment was booked successfully.",
    DEFAULT: "Good day."
}


def home(request, message_id=DEFAULT):
    ap_dates = []
    for i in range(ALLDAY):
        day = (datetime.datetime.now() + datetime.timedelta(i))
        if day.weekday() != CLOSED_DAY:
            ap_dates.append(day)
    context = {'ap_dates': ap_dates, 'closed_day': Days(
        CLOSED_DAY).name, 'message': messages[message_id]}
    return render(request, 'appointment/book.html', context)


def slotsOpen(request):
    try:
        date = request.GET['date']
    except(KeyError):
        return HttpResponseRedirect(reverse('rhome', args=(BAD_ATTEMPT,)))
    date = datetime.datetime.strptime(date, DATE_FORMAT)
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
    try:
        date = request.POST['curdate']
        slot_id = request.POST['slot']
        service_id = request.POST['service']
        p_number = request.POST['phone']
    except(KeyError):
        return HttpResponseRedirect(reverse('rhome', args=(BAD_ATTEMPT,)))
    date = datetime.datetime.strptime(date, DATE_FORMAT)
    if AppointmentDetails.objects.filter(
            app_date=date, app_slot_id=slot_id).exists():
        return HttpResponseRedirect(reverse('rhome', args=(BAD_ATTEMPT,)))
    elif AppointmentDetails.createAppointment(date, slot_id, service_id, p_number) == None:
        return HttpResponseRedirect(reverse('rhome', args=(BAD_ATTEMPT,)))
    return HttpResponseRedirect(reverse('rhome', args=(SUCCESS,)))
