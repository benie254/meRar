from django.shortcuts import render,redirect
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

    return render(request,'galleries/today-galleries.html',{"date":date})


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
        assert False

    if date == dt.date.today():
        return redirect(gallery_today)

    return render(request,'galleries/past-gallery.html',{"date":date})
