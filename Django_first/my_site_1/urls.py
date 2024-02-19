from django.urls import path
from . import views

urlpatterns = [path("", views.my_shop), path("products", views.my_shop_products)]
