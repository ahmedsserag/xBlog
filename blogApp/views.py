from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post, User

# Home Views
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

# Single Post Views
def single(request, slug):
    try:
        post = Post.objects.get(slug=slug, status='Published')
    except Post.DoesNotExist:
        raise Http404("Post Not Found :/")
    
    context = {
        'post': post,
    }
    return render(request, 'single.html', context)