from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Category, PostPoem,PostStory


def home(request):
    poems = PostPoem.objects.all()
    category = Category.objects.all()
    storys = PostStory.objects.all()
    print(poems)
    context = {
        'poems':poems,
        'storys':storys,
        'category':category
    }
    return render(request,'home.html',context)
     
