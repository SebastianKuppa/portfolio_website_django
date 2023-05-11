from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import PostForm
from .filters import PostFilter


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
    filter = PostFilter(request.GET, queryset=posts)
    posts = filter.qs
    context = {'posts': posts, 'myFilter': filter}
    return render(request, 'posts.html', context)


def profile(request):
    return render(request, 'profile.html')


# CRUD Views
@login_required(login_url='home')
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')
    context = {'form': form}
    return render(request, 'post_form.html', context)


@login_required(login_url='home')
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')
    context = {'form': form}
    return render(request, 'post_form.html', context)


@login_required(login_url='home')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    context = {'post': post}
    return render(request, 'delete.html', context)

