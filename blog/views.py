from django.shortcuts import render, get_object_or_404
#1. cargar lista de post con un import
from .models import Post, Category

# Create your views here.


def blog(request):
    #2. creo el queryset
    posts = Post.objects.all()    
    return  render(request,"blog/blog.html", {'posts' : posts})


def category(request, category_id):
    # primera forma:
    # category = Category.objects.get(id = category_id)
    # segunda forma:
    category = get_object_or_404(Category, id=category_id)
    #category de la parte izquierda es el del modelo
    posts = Post.objects.filter(category=category_id)
    return render(request, "blog/category.html", {'category': category , 'posts': posts})



