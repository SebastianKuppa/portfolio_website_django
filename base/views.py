from django.shortcuts import render

from .models import Post

def home(request):
    return render(request, 'index.html')


def post(request):
    return render(request, 'post.html')


def posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts.html', context)


def profile(request):
    return render(request, 'profile.html')
