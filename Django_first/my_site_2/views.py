from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Post, Category
from .form import CommentsForm


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


class AddComments(View):
    # Добавление комментариев
    def post(self, request):
        form = CommentsForm(request.POST)
        if form.is_valid:
            form = form.save(commit=False)
        return redirect("/")


# class PostDeitail(View):
#     # Отдельная страница записей
#     def get(self, request, pk):
#         post = Post.objects.get(id=pk)
#         return render(request, "blog/blog_detail.html", {"post": post})
