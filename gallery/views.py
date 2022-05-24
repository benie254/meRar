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
    html = f"""
"""
    return HttpResponse(html)
