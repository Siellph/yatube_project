from multiprocessing import context
from re import template
from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context: dict = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def group_posts(request):
    context: dict = {
        'description': 'Здесь будет информация о группах проекта Yatube'
    }
    template: str = 'posts/group_list.html'
    return render(request, template, context)
