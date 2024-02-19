from django.shortcuts import render
from django.http import HttpResponse


def my_shop(request):
    return HttpResponse("Hello from my shop")


def my_shop_products(request):
    return HttpResponse("Products in stock")
