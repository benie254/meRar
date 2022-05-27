from django.db import models
import datetime as dt
from location_field.models.plain import PlainLocationField


# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10,blank=True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['first_name']


class tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=30,choices=[('Food','Food'),('Entertainment','Entertainment')])

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()


class Location(models.Model):
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()



class Image(models.Model):
    pic = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=60)
    description = models.TextField()
    editor = models.ForeignKey(Editor,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tag)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True)


    @classmethod
    def todays_gallery(cls):
        today = dt.date.today()
        gallery = cls.objects.filter(published__date=today)

        return gallery

    @classmethod
    def days_gallery(cls,date):
        gallery = cls.objects.filter(published__date=date)

        return gallery

    @classmethod
    def search_by_description(cls,search_term):
        gallery = cls.objects.filter(description__icontains=search_term)

        return gallery

    @classmethod
    def search_by_category(cls, search_term):
        gallery = cls.objects.filter(category__icontains=search_term)

        return gallery

