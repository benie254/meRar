from django.test import TestCase
from .models import Editor,Image,tags
import datetime as dt


# Create your tests here.
class EditorTestClass(TestCase):

    # set up method
    def setUp(self):
        self.benie = Editor(first_name='Benie',last_name='Langat',email='benie@gmail.com',phone='0712345678')

    # test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.benie,Editor))

    # test the save method
    def test_save_method(self):
        self.benie.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)


class ImageTestClass(TestCase):

    def setUp(self):
        # create a new editor & save
        self.benie = Editor(first_name='Benie',last_name='Langat',email='benie@gmail.com',phone='0712345678')
        self.benie.save_editor()

        # create a new tag & save it
        self.new_tag = tags(name='tester')
        self.new_tag.save()

        self.new_image = Image(title='Ozura',description='The landscape of heaven',editor=self.benie)
        self.new_image.save()

        self.new_image.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Image.objects.all().delete()

    def test_get_gallery_today(self):
        today_gallery = Image.todays_gallery()
        self.assertTrue(len(today_gallery) > 0)

    def test_get_gallery_by_date(self):
        test_date = '2022-05-26'
        date = dt.datetime.strptime(test_date,'%Y-%m-%d').date()
        gallery_by_date = Image.days_gallery(date)

        self.assertTrue(len(gallery_by_date) == 0)
