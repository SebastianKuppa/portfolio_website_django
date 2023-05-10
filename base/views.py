from django.shortcuts import render

from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    context = {'posts': posts}
    return render(request, 'index.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'post.html', context)


def posts(request):
    posts = Post.objects.filter(active=True)
    context = {'posts': posts}
    return render(request, 'posts.html', context)


def profile(request):
    return render(request, 'profile.html')


# CRUD Views
def createPost(request):
    form = PostForm()
    context = {'form': form}
    return render(request, 'post_form.html', context)

