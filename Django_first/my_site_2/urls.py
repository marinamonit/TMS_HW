from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostView.as_view()),
    path("post2/", views.PostView_1.as_view()),
    path("comments/", views.AddComments.as_view(), name="add_comments"),
    # path("<int:pk>/", views.PostDeitail.as_view())
]
