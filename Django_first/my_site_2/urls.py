from django.urls import path
from . import views

urlpatterns = [path("", views.my_blog), path("topic", views.my_blog_topic)]
