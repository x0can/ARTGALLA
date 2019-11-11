from django.shortcuts import render,redirect
from .models import Art,Category,Location
# Create your views here.
def index(request):
    art = Art.objects.all()
    location = Location.objects.all()
    category = Category.objects.all()
    return render(request,'art/index.html',{'art':art,'location':location,'category':category})

# def display_category(request):
#     art = Art.art_display_by_category()
#     return render(request,'art/index.html',{'art':art})
    

def search_results(request):
    if 'category' in request.GET and request.GET['category']:
        category = request.GET.get("category")
        searched_art = Art.art_search_art(category) or Art.filter_by_location(art_location='art')
        message = f'{category}'
        return render (request,'art/search.html',{"message":message,"art":searched_art})

    else:
        message = "You haven't searched for any name"

        return render(request,'art/search.html',{'message':message})

def location(request):
    located_art =[]
    if 'location' in request.GET and request.GET['location']:
        location = request.GET.get('location')
        located_art = Art.filter_by_location(location)

    return render(request,'art/location.html',{'art':located_art})

def get_art(request):
    art = []
    if 'art' in request.GET and request.GET['art']:
        art_details = request.GET.get('art')
        art = Art.get_art(art)

    return render(request,'art/art.html',{'art':art})    
    

    
