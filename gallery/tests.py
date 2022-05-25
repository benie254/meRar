from django.test import TestCase
from .models import Editor,Image,tags


# Create your tests here.
class EditorTestClass(TestCase):

    # set up method
    def setUp(self):
        self.benie = Editor(first_name='Benie',last_name='Langat',email='benie@gmail.com')

    # test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.benie,Editor))

    # test the save method
    def test_save_method(self):
        self.benie.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)