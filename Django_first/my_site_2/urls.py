from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostView.as_view()),
    path("post2/", views.PostView_1.as_view()),
]
