from django.http import HttpResponse
from django.shortcuts import render
from posts.models import PostPoem,PostStory


def home(request):
    poems = PostPoem.objects.all()
    storys = PostStory.objects.all()
    print(poems)
    context = {
        'poems':poems,
        'storys':storys
    }
    return render(request,'home.html',context)
     
