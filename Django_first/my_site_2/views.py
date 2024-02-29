from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Post, Category


class PostView(View):
    # Вывод записей
    def get(self, request):
        posts = Post.objects.get(id=1)
        return render(request, "blog/blog.html", {"posts": posts})


class PostView_1(View):
    # Вывод записей
    def get(self, request):
        posts = Post.objects.get(id=2)
        return render(request, "blog/blog.html", {"posts": posts})
