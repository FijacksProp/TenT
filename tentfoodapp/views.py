from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):

    return render(request, 'front/index.html')

def menupage(request):
    menu = Menu.objects.all()
    menusnacks = Menusnacks.objects.all()
    menubakery = Menubakery.objects.all()
    menuswallow = Menuswallow.objects.all()
    menuforeign = Menuforeign.objects.all()

    context = {
        'menu': menu,
        'menusnacks': menusnacks,
        'menubakery': menubakery,
        'menuswallow': menuswallow,
        'menuforeign': menuforeign,
    }
    return render(request, 'front/menu.html', context)

def blogpost(request):
    blog = Blog.objects.all()
    comment = Comment.objects.all()
    like = Like.objects.all()
    dislike = Dislike.objects.all()

    context = {
        'blog': blog,
        'comment': comment,
        'like': like,
        'dislike': dislike,
    }

    return render(request, 'front/bloghtml.html', context)

