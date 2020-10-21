from django.shortcuts import render
from django.http import HttpResponse
from .models import CLOSED_DAY, ALLDAY, DATE_FORMAT, Days
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
    date = request.GET['date']
    date = datetime.datetime.strptime(date, DATE_FORMAT)
    return HttpResponse(str(date))
