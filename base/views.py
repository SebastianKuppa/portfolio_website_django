from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def post(request):
    return render(request, 'post.html')


def posts(request):
    posts = [
        {'headline': 'test',
         'subheadline': 'context'},
        {'headline': 'test',
         'subheadline': 'context'},
        {'headline': 'test',
         'subheadline': 'context'},
    ]
    context = {'posts': posts}
    return render(request, 'posts.html', context)


def profile(request):
    return render(request, 'profile.html')
