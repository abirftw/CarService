from django.shortcuts import render
from django.http import HttpResponse
from .models import CLOSED_DAY, ALLDAY, DATE_FORMAT, Days, TimeSlots
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
    ap_list = TimeSlots.objects.filter(appointmentdetails__app_date=date)
    avail_list = list(
        filter(lambda x: x not in ap_list, TimeSlots.objects.all()))
    context = {
        'available_slot': avail_list
    }
    return render(request, 'appointment/slotsAvailable.html', context)
