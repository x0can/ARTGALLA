from django.db import models

# Create your models here.
class Category (models.Model):
    title = models.CharField(max_length = 30)

    def __str__(self):
        return self.title

    def save_category(self):
        self.save()

    def display_category(self):
        category = Category.objects.all()
        return category


    def delete_category(self):
        category = Category.objects.filter().delete()
        return category


        
    # @classmethod
    # def art_search(cls,search_term):
    #     art = cls.objects.filter(title__icontains = search_term)
    #     return art


    class Meta:
        ordering = ['title']

class Location (models.Model):

    place = models.CharField(max_length = 30)


    def save_place(self):
        self.save()

    def display_location(self):
        location = Location.objects.all()
        return location                

    def __str__(self):
        return self.place    


class Art(models.Model):
    art_name = models.CharField(max_length = 60)
    art_description = models.TextField()
    art_image = models.ImageField(upload_to = 'art/')
    art_category = models.ForeignKey(Category, on_delete= models.CASCADE)
    art_location = models.ForeignKey(Location, on_delete= models.CASCADE)

    def save_art(self):
        self.save()




    @classmethod
    def art_search_art(cls,art_category):
        art = cls.objects.filter(art_category__title__icontains = art_category)
        return art

    def __str__(self):
        return self.art_name


    @classmethod
    def get_art(cls,art_name):
        art = cls.objects.filter(art_name__icontains=art_name)
        return art

    @classmethod
    def filter_by_location(cls,art_location):
        art = cls.objects.filter(art_location__place__icontains = art_location)
        return art


    class Meta:
        ordering = ['art_name']    