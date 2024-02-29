from django.contrib import admin
from .models import Post, Category

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["categoria"]
