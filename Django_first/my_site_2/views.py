from django.shortcuts import render
from django.http import HttpResponse


def my_blog(request):
    return HttpResponse("Hello from my blog")


def my_blog_topic(request):
    return HttpResponse("Choose a blog topic")
