from django.shortcuts import render

from .models import Post


def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    context = {'posts': posts}
    return render(request, 'index.html', context)


def post(request):
    return render(request, 'post.html')


def posts(request):
    posts = Post.objects.filter(active=True)
    context = {'posts': posts}
    return render(request, 'posts.html', context)


def profile(request):
    return render(request, 'profile.html')
