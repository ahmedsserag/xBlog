from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post, User
from django.core.paginator import Paginator, EmptyPage

# Home Views
def home(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'posts': posts})

# Single Post Views
def single(request, year, month, slug):
    try:
        post = Post.objects.get(slug=slug, publish__year=year, publish__month=month, status='Published')
    except Post.DoesNotExist:
        raise Http404("Post Not Found :/")
    
    context = {
        'post': post,
    }
    return render(request, 'single.html', context)