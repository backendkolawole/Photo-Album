from unicodedata import category
from django.shortcuts import render, redirect
from .models import Category, Photo
# Create your views here.


def gallery(request):
    category = request.GET.get('category')
    
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name = category)
        
 
    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    '''view all photos'''
    return render(request, 'photoshare_app/gallery.html', context)


def photo(request, pk):
    '''view a particular photo'''
    photo = Photo.objects.get(id=pk)
    return render(request, 'photoshare_app/photo.html', {'photo': photo})


def add(request):
    '''view for adding a photo'''
    categories = Category.objects.all()
    
    if request.method == "POST":
        data = request.POST
        image = request.FILES.get('image')
        
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name= data['category_new'])
        else:
            category = None
            
        photo = Photo.objects.create(
            category= category,
            description = data['description'],
            image= image,
        )
        
        return redirect('gallery')
        
    
    context = {'categories': categories}


    return render(request, 'photoshare_app/add.html', context)


