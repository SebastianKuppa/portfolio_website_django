from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def post(request):
    return render(request, 'post.html')


def posts(request):
    return render(request, 'posts.html')


def profile(request):
    return render(request, 'profile.html')
