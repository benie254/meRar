from django.contrib import admin
from .models import Editor,Image,tag


class ImageAdmin(admin.ModelAdmin):
    filter_horizontal=('tags',)


# Register your models here.
admin.site.register(Editor)
admin.site.register(Image,ImageAdmin)
admin.site.register(tag)
