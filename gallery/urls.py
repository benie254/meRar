from django.urls import re_path as url
from . import views


urlpatterns = [
    url('^today/$',views.gallery_today,name='galleryToday')
]