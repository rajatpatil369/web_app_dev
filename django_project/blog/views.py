from django.shortcuts import render

posts = [
    {
        'author': 'RajatKP',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 13, 2023',
    },
    {
        'author': 'user2',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'August 12, 2023',
    },
]


def home(request):
    context = {
        'title': 'Home',
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', { 'title': 'About' })
