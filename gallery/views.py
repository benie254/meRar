from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt


# Create your views here.
def gallery_today(request):
    """
    gallery view function
    :param request: http request
    :return: images for a particular day
    """
    date = dt.date.today()

    day = convert_dates(date)

    html = f"""
"""
    return HttpResponse(html)


def convert_dates(dates):
    """
    :param dates: date of the week
    :return: weekday for the date
    """

    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

    # return the actual day of the week
    day = days[day_number]

    return day


def past_days_gallery(request,past_date):
    """
    :param request: http request
    :param past_date: date from the url
    :return: galleries from a past date
    """

    # convert data from the string url
    date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    day = convert_dates(date)
    html = f"""
"""

    return HttpResponse(html)
