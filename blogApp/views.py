from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post, User

# Home Views
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

# Single Post Views
def single(request, id):
    try:
        post = Post.objects.get(id=id, status='Published')
    except Post.DoesNotExist:
        raise Http404("Post Not Found :/")
    
    context = {
        'post': post,
    }
    return render(request, 'single.html', context)

# About Views
def about(request):
    return render(request, 'about.html')

# Contact Us Views
def contact(request):
    return render(request, 'contact-us.html')
