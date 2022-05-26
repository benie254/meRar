from django.db import models
import datetime as dt


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


class Image(models.Model):
    pic = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=60)
    description = models.TextField()
    editor = models.ForeignKey(Editor,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tag)
    published = models.DateTimeField(auto_now_add=True)

    @classmethod
    def todays_gallery(cls):
        today = dt.date.today()
        gallery = cls.objects.filter(published__date=today)

        return gallery

    @classmethod
    def days_gallery(cls,date):
        gallery = cls.objects.filter(pub_date__date=date)

        return gallery

    @classmethod
    def search_by_description(cls,search_term):
        gallery = cls.objects.filter(description__icontains=search_term)

        return gallery