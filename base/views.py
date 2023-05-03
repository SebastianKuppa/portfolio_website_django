from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h2>HOME</h2>')


def post(request):
    return HttpResponse('<h2>POST</h2>')


def posts(request):
    return HttpResponse('<h2>POSTS</h2>')


def profile(request):
    return HttpResponse('<h2>PROFILE</h2>')
