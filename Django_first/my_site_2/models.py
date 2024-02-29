from django.db import models


class Post(models.Model):
    # Данные о посте
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name="id")
    title = models.CharField("Заголовок записи", max_length=100)
    text = models.TextField("Текст записи")
    author = models.CharField("Имя автора", max_length=100)
    date = models.DateField("Дата публикации")

    def __str__(self):
        return f"{self.title}, {self.author}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Category(models.Model):
    # Категории постов
    categoria = models.CharField("Категория поста")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
