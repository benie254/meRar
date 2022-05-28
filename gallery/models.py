from django.db import models
import datetime as dt
from location_field.models.plain import PlainLocationField
from django.contrib.postgres.search import SearchVector


# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10,blank=True)
    profile_pic = models.ImageField(upload_to='images/')

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
    city = models.CharField(max_length=255,null=True)
    location = PlainLocationField(based_fields=['city'], zoom=7,null=True)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()



class Image(models.Model):
    pic = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=60)
    description = models.TextField()
    editor = models.ForeignKey(Editor,on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(tag)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True)
    published = models.DateTimeField(auto_now_add=True)

    @classmethod
    def galleries(cls):
        gallery = cls.objects.all()

        return gallery


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
    def search_by_tag(cls, tag_term):
        gallery = cls.objects.filter(tag__name=tag_term)

        return gallery

# class Meta:
#     ordering = ['first_name']
#     search_fields = ['category__pic']
    @classmethod
    def search_by_category(cls, category_term):

        # gallery = cls.objects.filter(category__search=search_term)
        # gallery = cls.objects.annotate(search=SearchVector('category','image_description').filter(search=search_term))

        gallery = cls.objects.filter(category__category=category_term)
        # Find all Articles for any Reporter whose first name is "John".
        # >> > Article.objects.filter(reporter__first_name='John')

        return gallery

    @classmethod
    def search_by_location(cls, location_term):
        gallery = cls.objects.filter(location__location=location_term)

        return gallery

