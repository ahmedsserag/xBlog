from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post, User
from .forms import EmailPostForm, NewPost
from django.core.paginator import Paginator, EmptyPage
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Home View
def home(request):
    post_list = Post.objects.filter(status='Published')
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'posts': posts})

# Single Post Detials View
def single(request, year, month, slug):
    try:
        post = Post.objects.get(slug=slug, publish__year=year, publish__month=month, status='Published')
    except Post.DoesNotExist:
        raise Http404("Post Not Found :/")
    
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            post_url = request.build_absolute_uri(post.get_absolute_url())
            email = request.POST['email']
            subject = f"{request.POST['name']} recommends you a post"
            message = f"Read {post.title} at {post_url} \n{request.POST['name']}'s comments: {request.POST['comment']}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False,)
            sent = True
    else:
        form = EmailPostForm()
    
    context = {
        'post': post,
        'form': form,
        'sent': sent,
    }
    return render(request, 'single.html', context)

# Create New Post View
def new(request):
    if request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            form.save()
            messages.success(request, f'{title} Post Saved Successfully')
            form = NewPost()
    else:
        form = NewPost()
    return render(request, 'new.html', {'form': form})

# Contact Us View
def contact_us(request):
    sent = False
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = f"Name: {name}: \nEmail: {email}\n Message: {request.POST['message']}"

        send_mail(subject, message, settings.EMAIL_HOST_USER, ['support@xBlog.com'],)
        sent = True
        print('Sent :)')

    return render(request, 'contact-us.html', {'sent': sent})