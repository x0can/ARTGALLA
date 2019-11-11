from django.test import TestCase
from .models import Category,Art,Location
# Create your tests here.


class CategoryTestCase(TestCase):

    def setUp(self):
        self.cat = Category(title ='title')

    def test_instance(self):
        self.assertTrue(isinstance(self.cat,Category))    

    def test_save_method(self):
        self.cat.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category)>0)

    def test_display_category(self):
        
        self.category = Category.display_category(self)

    def test_delete_editor(self):
        self.category = Category.delete_category(self)


        
        
            