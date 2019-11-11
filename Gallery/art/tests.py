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


class ArtTestCase(TestCase):

    def setUp(self):
        self.art = Art(art_name ='name',art_description = 'art description')
        self.art.save_art()

        self.new_location = Location(place = 'testing')
        self.new_tag.save()

        self.new_art = Art(art_name = 'Test Article',art_description = 'This is a test',category = self.Category)
        self.new_art.save()

        self.new_art.art_location.add(self.new_art)




    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Art.objects.all().delete()


 
                                        
            