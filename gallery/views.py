from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt


# Create your views here.
def gallery_today(request):
    """
    gallery view function
    :param request: http request
    :return: images for a particular day
    """
    date = dt.date.today()

    html = f"""
"""
    return HttpResponse(html)


def past_days_gallery(request,past_date):
    """
    :param request: http request
    :param past_date: date from the url
    :return: galleries from a past date
    """

    try:
        # convert data from the string url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # raise 404 when value error is thrown
        raise Http404()

    html = f"""
"""

    return HttpResponse(html)
