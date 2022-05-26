from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image


# Create your views here.
def gallery_today(request):
    """
    gallery view function
    :param request: http request
    :return: images for a particular day
    """
    date = dt.date.today()
    gallery = Image.todays_gallery()

    return render(request,'galleries/gallery-today.html',{"date":date,"gallery":gallery})


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

    gallery = Image.days_gallery(date)

    return render(request,'galleries/past-gallery.html',{"date":date,"gallery":gallery})


def search_results(request):

    if 'image' in request.GET and request.get["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_tag(search_term)

        message = f"{search_term}"

        return render(request,'galleries/search.html',{"message":message,"images":searched_images})

    else:
        message = "You haven't searched for a tag yet"

        return render(request,'galleries/search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id=image_id)

    except DoesNotExist:
        raise Http404()

    return render(request,'galleries/image.html',{"image":image})
